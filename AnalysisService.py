import datetime
import os

from dotenv import load_dotenv
from langchain import ConversationChain
from langchain.chat_models import ChatAnthropic
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()


def generate_metadata(labels, score, url):
    metadata = "---\n"
    metadata += "tags: " + labels + "\n"
    metadata += "score: " + score + "\n"
    metadata += "date: " + str(datetime.date.today()) + "\n"
    metadata += "source: " + url + "\n"
    metadata += "status: created\n"
    metadata += "---\n\n"
    return metadata


class AnalysisService:
    @staticmethod
    def analyse(data):
        url, text = data
        print("analyzing url: " + url)
        chat = ChatAnthropic()
        messages = [
            HumanMessage(
                content="Write a summary of the [Text] that retains all important information while reducing the "
                        "word count to a minimum. Ensure that the summary accurately conveys the key points of the "
                        "original text and that the meaning is not lost. Just return the summary in outline-form:"
                        "[Text]=" + text)
        ]
        print("calling claude for summary")
        response = chat(messages)

        llm = ChatOpenAI(temperature=0.9, model_name="gpt-4")
        conversation = ConversationChain(llm=llm, verbose=False)
        title_prompt = "summarize into one short title: " + response.content
        labels_prompt = "Extract at least 10 labels of the [Text] that will be used categorize the text. Just return " \
                        "the labels comma separated and ranked form most general to most specific. " \
                        "[Text]=" + response.content
        one_line_prompt = "summarize into one short line: " + response.content
        score_prompt = "score the relevance of the following text in the field of large language models on a scale of " \
                       "one to ten: " + response.content

        print("calling gpt-4 for title, labels, one-liner and score based on summary")
        title = conversation.predict(input=title_prompt)
        labels = conversation.predict(input=labels_prompt)
        one_liner = conversation.predict(input=one_line_prompt)
        score = conversation.predict(input=score_prompt)

        output_filename = AnalysisService.get_file_path(title)

        metadata = generate_metadata(labels, score, url)

        print("writing to file: " + title)
        with open(output_filename, 'w') as file:
            file.write(metadata)
            file.write(str(one_liner))
            file.write("\n\n")
            file.write(str(response.content))

        return url

    @staticmethod
    def is_running_in_docker() -> bool:
        return os.path.exists('/.dockerenv')

    @staticmethod
    def get_file_path(title: str) -> str:
        if AnalysisService.is_running_in_docker():
            return '/obsidian/' + title + '.md'
        else:
            return os.getenv('OUTPUT_PATH') + title + '.md'

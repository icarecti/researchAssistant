import datetime

from langchain import ConversationChain
from langchain.chat_models import ChatAnthropic
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

from domain.Analysis import Analysis
from services.FilePathService import FilePathService


class AnalysisService:
    @staticmethod
    def analyse(data):
        url, text = data
        analysis = Analysis(url)
        print("analyzing text form: " + url)
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
        summary = response.content
        analysis.set_summary(summary)

        llm = ChatOpenAI(temperature=0.9, model_name="gpt-4")
        conversation = ConversationChain(llm=llm, verbose=False)
        title_prompt = "summarize into one short title: " + summary
        labels_prompt = "Extract at least 10 labels of the [Text] that will be used categorize the text. Just return " \
                        "the labels comma separated and ranked form most general to most specific. " \
                        "[Text]=" + summary
        one_line_prompt = "summarize into one short line: " + summary
        score_prompt = "score the relevance of the following text in the field of large language models on a scale of " \
                       "one to ten: " + summary

        print("calling gpt-4 for title, labels, one-liner and score based on summary")
        title = conversation.predict(input=title_prompt)
        analysis.set_title(title)
        labels = conversation.predict(input=labels_prompt)
        analysis.set_labels(labels)
        one_liner = conversation.predict(input=one_line_prompt)
        analysis.set_one_liner(one_liner)
        score = conversation.predict(input=score_prompt)
        analysis.set_score(score)

        output_filename = FilePathService.get_file_path(title) + ".md"

        print("writing to file: " + title)
        with open(output_filename, 'w') as file:
            file.write(AnalysisService.generate_full_analysis(analysis))

        return analysis

    @staticmethod
    def generate_metadata(labels, score, url):
        metadata = "---\n"
        metadata += "tags: " + labels + "\n"
        metadata += "score: " + score + "\n"
        metadata += "date: " + str(datetime.date.today()) + "\n"
        metadata += "source: " + url + "\n"
        metadata += "status: created\n"
        metadata += "---\n\n"
        return metadata

    @staticmethod
    def generate_full_analysis(analysis: Analysis):
        analysis_text = AnalysisService.generate_metadata(analysis.labels, analysis.score, analysis.url)
        analysis_text += "[source](" + analysis.url + ")"
        analysis_text += "\n\n\n"
        analysis_text += "### in one sentence\n" + str(analysis.one_liner)
        analysis_text += "\n\n"
        analysis_text += "### summary in outline form\n" + str(analysis.summary)
        return analysis_text

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
        url, extracted_text = data
        analysis = Analysis(url)
        print("analyzing text from: " + url)
        chat = ChatAnthropic()
        messages = [
            HumanMessage(
                content=AnalysisService.load_string_from_file("SummaryInOutlineForm.txt").format(text=extracted_text))
        ]
        print("calling claude for summary")
        response = chat(messages)
        summary = response.content
        analysis.set_summary(summary)

        llm = ChatOpenAI(temperature=0.9, model_name="gpt-4")
        conversation = ConversationChain(llm=llm, verbose=False)

        title_prompt = AnalysisService.load_string_from_file("Title.txt").format(summary=summary)
        label_prompt = AnalysisService.load_string_from_file("Labels.txt").format(summary=summary)
        one_line_prompt = AnalysisService.load_string_from_file("InOneSentence.txt").format(summary=summary)
        score_prompt = AnalysisService.load_string_from_file("Score.txt").format(summary=summary)

        print("calling gpt-4 for title, labels, one-liner and score based on summary")
        title = conversation.predict(input=title_prompt)
        analysis.set_title(title)
        labels = conversation.predict(input=label_prompt)
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
        # TODO 03.06.23: add "type" to metadata (tool, blog, repo, video, paper,...)
        metadata = "---\n"
        metadata += "tags: " + labels + "\n"
        metadata += "score: " + score + "\n"
        metadata += "date: " + str(datetime.date.today()) + "\n"
        metadata += "source: " + url + "\n"
        metadata += "status: created\n"
        metadata += "---\n"
        return metadata

    @staticmethod
    def generate_full_analysis(analysis: Analysis):
        analysis_text = AnalysisService.generate_metadata(analysis.labels, analysis.score, analysis.url)
        analysis_text += "[source](" + analysis.url + ")"
        analysis_text += "\n\n\n"
        analysis_text += "### in one sentence\n\n" + str(analysis.one_liner)
        analysis_text += "\n\n"
        analysis_text += "### summary in outline form\n\n" + str(analysis.summary)
        return analysis_text

    @staticmethod
    def load_string_from_file(filename):
        with open("prompts/" + filename, 'r') as file:
            return file.read()

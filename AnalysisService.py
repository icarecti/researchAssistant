from langchain.chat_models import ChatAnthropic
from langchain.schema import HumanMessage


class AnalysisService:
    @staticmethod
    def analyse(data):
        url, text = data
        print("################### before processing ###################")
        print(text)

        chat = ChatAnthropic()
        messages = [
            HumanMessage(
                content="Write a summary of the [Text] that retains all important information while reducing the "
                        "word count to a minimum. Ensure that the summary accurately conveys the key points of the "
                        "original text and that the meaning is not lost. Just return the summary:[Text]=" + text)
        ]

        response = chat(messages)
        print("################### after processing ###################")
        print(response)

        return url

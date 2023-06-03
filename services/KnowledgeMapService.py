from langchain import ConversationChain
from langchain.chat_models import ChatOpenAI

from services.FilePathService import FilePathService


class KnowledgeMapService:
    @staticmethod
    def create_map(data):
        llm = ChatOpenAI(temperature=0.9, model_name="gpt-4")
        conversation = ConversationChain(llm=llm, verbose=True)

        with open("domain/CanvasSpecification.txt", "r") as file:
            specification = file.read()

        canvas_prompt = "Create a canvas for obsidian, just return the json file nothing else. " \
                        "Here is the specification: " + specification + "\n" \
                        + "And here is the data that should be organised on the canvas: " + str(data)
        print("calling gpt-4 for canvas based on data")
        canvas_text = conversation.predict(input=canvas_prompt)

        print(canvas_text)

        output_filename = FilePathService.get_file_path("knowledge_map.canvas")
        with open(output_filename, 'w') as file:
            file.write(canvas_text)

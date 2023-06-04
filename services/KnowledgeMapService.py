import json
import uuid

from domain.Canvas import Canvas
from domain.CanvasNode import CanvasNode
from services.FilePathService import FilePathService


class KnowledgeMapService:
    @staticmethod
    def create_map_from(notes):
        canvas = Canvas()
        y_position = 0
        for note in notes:
            node = CanvasNode("file", note, 400, 400, uuid.uuid4().hex, 0, y_position)
            canvas.add_node(node)
            y_position -= 480
        canvas_dict = canvas.to_dict()
        canvas_text = json.dumps(canvas_dict)

        output_filename = FilePathService.get_file_path("knowledge_map2.canvas")
        with open(output_filename, 'w') as file:
            file.write(canvas_text)

import datetime
import json
import uuid

from domain.Canvas import Canvas
from domain.CanvasNode import CanvasNode
from services.FilePathService import FilePathService


class KnowledgeMapService:
    @staticmethod
    def create_map_from(notes):
        canvas = Canvas()
        node_width = 400
        node_height = 400
        column_spacing = 100
        row_spacing = 100
        columns = 4
        for i, note in enumerate(notes):
            x_position = (i % columns) * (node_width + column_spacing)
            y_position = -(i // columns) * (node_height + row_spacing)
            node = CanvasNode("file", note, node_width, node_height, uuid.uuid4().hex, x_position, y_position)
            canvas.add_node(node)
        canvas_dict = canvas.to_dict()
        canvas_text = json.dumps(canvas_dict)

        map__canvas = "knowledge_map_" + str(datetime.date.today()) + ".canvas"
        output_filename = FilePathService.get_file_path(map__canvas)
        with open(output_filename, 'w') as file:
            file.write(canvas_text)

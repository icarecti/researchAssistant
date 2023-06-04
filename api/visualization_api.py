from typing import List

from flask import Blueprint

from services.FilePathService import FilePathService
from services.KnowledgeMapService import KnowledgeMapService

visualization_api = Blueprint('visualization_api', __name__)


@visualization_api.route('/knowledgeMap', methods=['GET'])
def process_urls() -> tuple[str, int]:
    notes: List[str] = FilePathService.get_markdown_files_in_folder()
    KnowledgeMapService.create_map_from(notes)

    return "canvas was created", 200

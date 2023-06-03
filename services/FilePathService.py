import os

from dotenv import load_dotenv

load_dotenv()


class FilePathService:
    @staticmethod
    def is_running_in_docker() -> bool:
        return os.path.exists('/.dockerenv')

    @staticmethod
    def get_file_path(filename: str) -> str:
        if FilePathService.is_running_in_docker():
            return '/obsidian/' + filename
        else:
            return os.getenv('OUTPUT_PATH') + filename

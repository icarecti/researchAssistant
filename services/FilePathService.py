import os

from dotenv import load_dotenv

load_dotenv()


class FilePathService:
    @staticmethod
    def is_running_in_docker() -> bool:
        return os.path.exists('/.dockerenv')

    @staticmethod
    def get_folder_path() -> str:
        if FilePathService.is_running_in_docker():
            return '/obsidian/'
        else:
            return os.getenv('OUTPUT_PATH')

    @staticmethod
    def get_file_path(filename: str) -> str:
        return FilePathService.get_folder_path() + filename

    @staticmethod
    def get_markdown_files_in_folder() -> list[str]:
        folder_path = FilePathService.get_folder_path()
        return ['researchAssistant/' + f for f in os.listdir(folder_path) if
                os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.md')]

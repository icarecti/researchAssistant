from typing import Optional


class CanvasNode:
    def __init__(self, type: str, file: str, width: int, height: int, id: str, x: Optional[int] = None,
                 y: Optional[int] = None):
        self.type = type
        self.file = file
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Type: {self.type}, File: {self.file}, ID: {self.id}, X: {self.x}, Y: {self.y}, Width: {self.width}, Height: {self.height}"

    def set_file(self, file: str) -> None:
        self.file = file

    def set_id(self, id: str) -> None:
        self.id = id

    def set_x(self, x: int) -> None:
        self.x = x

    def set_y(self, y: int) -> None:
        self.y = y

    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "file": self.file,
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height
        }

from typing import List, Optional


class Analysis:
    def __init__(self, url: str, title: Optional[str] = None, labels: Optional[List[str]] = None,
                 one_liner: Optional[str] = None,
                 score: Optional[str] = None, summary: Optional[str] = None):
        self.url = url
        self.title = title
        self.labels = labels
        self.one_liner = one_liner
        self.score = score
        self.summary = summary

    def __str__(self) -> str:
        return f"URL: {self.url}, Title: {self.title}, Labels: {self.labels}, One-liner: {self.one_liner}, Score: {self.score}, Summary: {self.summary}"

    def set_title(self, title: str) -> None:
        self.title = title

    def set_labels(self, labels: List[str]) -> None:
        self.labels = labels

    def set_one_liner(self, one_liner: str) -> None:
        self.one_liner = one_liner

    def set_score(self, score: str) -> None:
        self.score = score

    def set_summary(self, summary: str) -> None:
        self.summary = summary

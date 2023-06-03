from typing import Optional


class Analysis:
    def __init__(self, url: str, website_type: str, title: Optional[str] = None, labels: Optional[str] = None,
                 one_liner: Optional[str] = None,
                 score: Optional[str] = None, summary: Optional[str] = None):
        self.url = url
        self.website_type = website_type
        self.title = title
        self.labels = labels
        self.one_liner = one_liner
        self.score = score
        self.summary = summary

    def __str__(self) -> str:
        return f"URL: {self.url}, Title: {self.title}, Labels: {self.labels}, One-liner: {self.one_liner}, Score: {self.score}, Summary: {self.summary}, Website Type: {self.website_type}"

    def set_title(self, title: str) -> None:
        self.title = title

    def set_labels(self, labels: str) -> None:
        self.labels = labels

    def set_one_liner(self, one_liner: str) -> None:
        self.one_liner = one_liner

    def set_score(self, score: str) -> None:
        self.score = score

    def set_summary(self, summary: str) -> None:
        self.summary = summary

    def set_website_type(self, website_type: str) -> None:
        self.website_type = website_type

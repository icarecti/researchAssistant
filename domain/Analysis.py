class Analysis:
    def __init__(self, url, title, labels, one_liner, score, summary):
        self.url = url
        self.title = title
        self.labels = labels
        self.one_liner = one_liner
        self.score = score
        self.summary = summary

    def __str__(self):
        return f"Title: {self.title}, Labels: {self.labels}, One-liner: {self.one_liner}, Score: {self.score}, Summary: {self.summary}"

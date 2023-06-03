class ScrapingResult:
    def __init__(self, url: str, website_type: str, extracted_text: str):
        self.url = url
        self.website_type = website_type
        self.extracted_text = extracted_text

    def __str__(self) -> str:
        return f"URL: {self.url}, Website Type: {self.website_type}, Extracted Text: {self.extracted_text}"

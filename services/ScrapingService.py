from urllib.request import urlopen

import tiktoken
from bs4 import BeautifulSoup


class ScrapingService:
    @staticmethod
    def scrape_text(url):
        # make scraping smarter add url check to see what type of url it is (youtube, blog, tool, github repo, pdf etc)
        # if youtube, then get the transcript
        # if image, then get a description
        # if pdf, then get the text
        # if blog, then get the text (with apify)
        print("scraping url: " + url)
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        extracted_text = soup.getText().replace('\n', ' ')
        extracted_text = ' '.join(extracted_text.split())

        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        tokensize = len(encoding.encode(extracted_text))
        print("extracted text with tokensize: " + str(tokensize))

        return url, extracted_text

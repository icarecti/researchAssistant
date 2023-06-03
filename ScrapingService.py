from urllib.request import urlopen

from bs4 import BeautifulSoup


class ScrapingService:
    @staticmethod
    def scrape_text(url):
        # make scraping smarter add url check to see what type of url it is (youtube, blog, tool, github repo, pdf etc)
        # if youtube, then get the transcript
        # if image, then get a description
        # if pdf, then get the text
        # if blog, then get the text (with apify)
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        extracted_text = soup.getText().replace('\n', ' ')
        extracted_text = ' '.join(extracted_text.split())
        return url, extracted_text

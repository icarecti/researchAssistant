from typing import List, Tuple

from flask import Flask, request, jsonify, Response

from AnalysisService import AnalysisService
from ScrapingService import ScrapingService

app = Flask(__name__)


@app.route('/urls', methods=['POST'])
def process_urls() -> tuple[Response, int]:
    urls: List[str] = request.json.get('urls', [])
    extracted_data: List[Tuple[str, str]] = [ScrapingService.scrape_text(url) for url in urls]
    processed_urls: List[str] = [AnalysisService.analyse(data) for data in extracted_data]
    return jsonify(processed_urls), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

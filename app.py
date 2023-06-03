from typing import List, Tuple

from flask import Flask, request, jsonify, Response

from ScrapingService import ScrapingService

app = Flask(__name__)


@app.route('/urls', methods=['POST'])
def process_urls() -> tuple[Response, int]:
    urls: List[str] = request.json.get('urls', [])
    processed_data: List[Tuple[str, str]] = [ScrapingService.scrape_text(url) for url in urls]
    processed_urls: List[str] = [url for url, _ in processed_data]
    return jsonify(processed_urls), 200


if __name__ == '__main__':
    app.run(debug=True)

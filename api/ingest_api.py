from typing import List

from flask import Blueprint, jsonify, request, Response
from tqdm import tqdm

from domain.Analysis import Analysis
from domain.ScrapingResult import ScrapingResult
from services.AnalysisService import AnalysisService
from services.ScrapingService import ScrapingService

ingest_api = Blueprint('ingest_api', __name__)


@ingest_api.route('/urls', methods=['POST'])
def analyse_urls() -> tuple[Response, int]:
    urls: List[str] = request.json.get('urls', [])
    extracted_data: List[ScrapingResult] = [ScrapingService.scrape(url) for url in tqdm(urls)]
    analysis: List[Analysis] = [AnalysisService.analyse(data) for data in tqdm(extracted_data)]
    urls = [a.url for a in analysis]
    return jsonify(urls), 200

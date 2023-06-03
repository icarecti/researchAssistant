from typing import List

from flask import Blueprint, jsonify, Response

from domain.Analysis import Analysis
from services.KnowledgeMapService import KnowledgeMapService

visualization_api = Blueprint('ingest_api', __name__)


@visualization_api.route('/knowledgeMap', methods=['GET'])
def process_urls() -> tuple[Response, int]:
    analysis: List[Analysis] = [
        Analysis(
            "https://www.theverge.com/23733388/microsoft-kevin-scott-open-ai-chat-gpt-bing-github-word-excel-outlook-copilots-sydney",
            "Embracing AI Copilots: Microsoft's Collaborative Approach and Challenges",
            "AI, Copilots, Microsoft, OpenAI, AI platforms, responsible AI, governance, Bing Chatbot, AI infrastructure, safety testing",
            "AI Copilots: Microsoft's Vision, Challenges, and Responsibility",
            "8.5",
            "some summary"),
        Analysis(
            "https://japanbizinsider.blogspot.com/2023/05/unveiling-future-ai-digital-clones_23.html",
            "AI Voice Clones and Digital Afterlife: Opportunities and Concerns",
            "Artificial Intelligence, Voice Replication, Digital Clones, Coemo, Storytelling Speaker, Deceased Loved Ones, AI-generated Videos, Personalized Experiences, Ethical Concerns, Entrepreneurs",
            "AI Voice Clones Bridging Gap Between Life and Afterlife",
            "5",
            "some other summary"),
    ]
    KnowledgeMapService.create_map(analysis)

    urls = [a.url for a in analysis]
    return jsonify(urls), 200

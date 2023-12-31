from fastapi import FastAPI
from words_api import get_today_word
from scorer.similarity_scorer import SimilarityScorer
from fastapi.middleware.cors import CORSMiddleware
from sys import stdout
from scorer.unknown_word_exception import UnknownWordException
from tips import TipsService
from logging.config import dictConfig
import logging
from config import LogConfig

dictConfig(LogConfig().dict())

log = logging.getLogger("contexto")

app = FastAPI()
scorer = SimilarityScorer()
tips_service = TipsService(scorer)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/similarity")
async def get_similarity(guess: str):
    log.info(f"Guess: {guess}")

    today_word = get_today_word()

    if today_word == guess:
        return {
            "similarity": 100
        }

    log.info(f"Compute similarity for '{today_word}' and '{guess}'")

    try:
        similarity = scorer.get_similarity(today_word=today_word, guess=guess)
    except UnknownWordException as e:
        return {
            "unknown_word": e.word
        }

    return {
        "similarity": similarity
    }


@app.get("/tip")
async def get_tip():
    tip, similarity = tips_service.get_tip(get_today_word())
    return {
        "tip": tip,
        "similarity": similarity
    }


@app.get("/giveup")
async def get_tip():
    return {
        "word": get_today_word(),
        "similarity": 100
    }

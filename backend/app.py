from fastapi import FastAPI
import logging as log
from words_api import get_today_word
from scorer.similarity_scorer import SimilarityScorer
from fastapi.middleware.cors import CORSMiddleware
from sys import stdout

app = FastAPI()
scorer = SimilarityScorer()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define logger
logger = log.getLogger('mylogger')

logger.setLevel(log.DEBUG)
logFormatter = log.Formatter("%(name)-12s %(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")
consoleHandler = log.StreamHandler(stdout)
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)


@app.get("/similarity")
async def get_similarity(guess: str):
    log.info(f"Guess: {str}")

    today_word = get_today_word()

    if today_word == guess:
        return {
            "similarity": 100
        }

    log.info(f"Compute similarity for {today_word} and {guess}")

    similarity = scorer.get_similarity(word1=today_word, word2=guess)

    return {
        "similarity": similarity
    }

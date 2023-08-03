from fastapi import FastAPI
import logging as log
from scorer.similarity_scorer import SimilarityScorer
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/similarity")
async def get_similarity(word1: str, word2: str):
    log.info(f"Compute similarity for {word1} and {word2}")
    return {
        "similarity": scorer.get_similarity(word1=word1, word2=word2)
    }

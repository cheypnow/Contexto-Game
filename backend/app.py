from fastapi import FastAPI
from backend.scorer.similarity_scorer import SimilarityScorer

app = FastAPI()
scorer = SimilarityScorer()


@app.get("/similarity")
async def get_similarity(word1: str, word2: str):
    return scorer.get_similarity(word1=word1, word2=word2)

from scorer.similarity_scorer import SimilarityScorer
import logging
import random

log = logging.getLogger("contexto")


class TipsService:

    def __init__(self, scorer: SimilarityScorer):
        self.scorer = scorer

    def get_tip(self, today_word: str):
        log.info(f"Get tip for {today_word}")

        similar_list = self.scorer.get_similar(today_word)
        log.info(f"Similar words for word {today_word}: {similar_list}")

        similar_words = [word for word, score in similar_list]

        tip = random.choice(similar_words)

        tip_similarity = self.scorer.get_similarity(today_word, tip)

        log.info(f"Tip for word {today_word}: Tip: {tip}. Similarity: {tip_similarity}")
        return tip, tip_similarity

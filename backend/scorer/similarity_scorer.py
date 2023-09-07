import gensim
import logging
import gensim.downloader as downloader
import os
from .unknown_word_exception import UnknownWordException

model_path = 'model/glove-twitter-25'
model_name = 'glove-twitter-25'

log = logging.getLogger("contexto")


def download_model():
    # Load pre-trained Word2Vec model if it does not exist
    if not os.path.exists(model_path):
        log.info(f"Model does not exist. Load word2vec model {model_name}")
        model = downloader.load(model_name)
        print("Model loaded")
        log.info("Model loaded")
        model.save(model_path)
        log.info(f"Model loaded to {model_path}")
    else:
        log.info("Skip model downloading")


def round_similarity(similarity):
    if similarity < 0.01:
        return 0.01
    return round(similarity, 2)


class SimilarityScorer:

    def __init__(self):
        log.info('Load word2vec model')
        download_model()
        self.model = gensim.models.KeyedVectors.load(model_path)

    def get_similarity(self, today_word: str, guess: str):
        try:
            similarity = self.model.similarity(today_word, guess).item()
        except KeyError:
            msg = f"KeyError on words: '{today_word}','{guess}'"
            log.error(msg)
            raise UnknownWordException(guess)

        return round(round_similarity(similarity) * 100)

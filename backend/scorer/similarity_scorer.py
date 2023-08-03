import gensim
import logging as log
import gensim.downloader as downloader
import os

model_path = 'model/word2vec-google-news-300'
model_name = 'word2vec-google-news-300'


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


class SimilarityScorer:

    def __init__(self):
        log.info('Load word2vec model')
        download_model()
        self.model = gensim.models.KeyedVectors.load(model_path)

    def get_similarity(self, word1: str, word2: str):
        return self.model.similarity(word1, word2).item()


import gensim.downloader as downloader
import logging as log


class SimilarityScorer:

    def __init__(self):
        log.info('Load word2vec model')
        self.model = downloader.load('word2vec-google-news-300')

    def get_similarity(self, word1: str, word2: str):
        return self.model.similarity(word1, word2)

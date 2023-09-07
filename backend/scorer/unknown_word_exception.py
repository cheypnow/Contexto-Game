class UnknownWordException(Exception):

    def __init__(self, word):
        self.word = word

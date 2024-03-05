def word_count_aggregator():
    wordcount = 0
    def aggregator(sentence):
        nonlocal wordcount
        wordcount += len(sentence.split())
        return wordcount
    return aggregator

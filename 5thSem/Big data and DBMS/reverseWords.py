from pyspark import SparkContext
from pyspark.streaming import StreamingContext

def reverse_words(sentence):
    words = sentence.split(" ")
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

sc = SparkContext("local[2]", "ReverseWordCount")
ssc = StreamingContext(sc, 1)

lines = ssc.socketTextStream("localhost", 9999)

reversed_lines = lines.map(reverse_words)
reversed_lines.pprint()

ssc.start()
ssc.awaitTermination()

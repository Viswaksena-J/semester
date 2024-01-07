from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)

lines = ssc.socketTextStream("localhost", 9999)

words = lines.flatMap(lambda line: line.split(" "))

word_pairs = words.map(lambda word: (word, 1))
word_counts = word_pairs.reduceByKey(lambda x, y: x + y)
pairs = words.map(lambda word: (word, 1))

wordCounts = pairs.reduceByKey(lambda x, y: x + y)
total_word_count = word_counts.reduce(lambda x, y: ("Total", x[1] + y[1]))
wordCounts.pprint()
total_word_count.pprint()

ssc.start()          
ssc.awaitTermination()  

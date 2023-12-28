from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create a local StreamingContext with two working threads and a batch interval of 1 second
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)

# Create a DStream that will connect to hostname:port, like localhost:9999
lines = ssc.socketTextStream("localhost", 9999)

# Split each line into words
words = lines.flatMap(lambda line: line.split(" "))

# Count each word in each batch
word_pairs = words.map(lambda word: (word, 1))
word_counts = word_pairs.reduceByKey(lambda x, y: x + y)
pairs = words.map(lambda word: (word, 1))

# Print the total word count to the console
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
total_word_count = word_counts.reduce(lambda x, y: ("Total", x[1] + y[1]))
wordCounts.pprint()
total_word_count.pprint()

ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate

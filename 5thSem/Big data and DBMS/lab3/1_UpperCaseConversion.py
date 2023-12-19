from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("UpperCaseConversion").getOrCreate()

data = [("Hello",), ("World",), ("Spark",), ("UDF",)]
columns = ["text"]

df = spark.createDataFrame(data, columns)

def convert_to_upper_case(text):
    return text.upper()

convert_to_upper_case_udf = udf(convert_to_upper_case, StringType())

df_upper_case = df.withColumn("upper_case_text", convert_to_upper_case_udf("text"))

df_upper_case.show()

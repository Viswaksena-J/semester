# a. Import a Spark Session into Apache Spark.
from pyspark.sql import SparkSession

# b. Create a Spark Session ‘spark’ using the ‘builder()’ function.
spark = SparkSession.builder.appName("EmployeeData").getOrCreate()

# c. Import the Implicits class into ‘spark’ Session.
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# d. Now create a DataFrame ‘df’ and import data from the ’employee.json’ file.
file_path = "employee.json"  # Replace with the actual path to your 'employee.json' file
df = spark.read.json(file_path)

# e. Print the schema of ‘df’ DataFrame.
df.printSchema()

# f. Display the DataFrame ‘df’.
df.show(5)

# Import necessary classes and functions
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("EmployeeData").getOrCreate()

# Load data from 'employee.json' file into DataFrame 'df'
file_path = "employee1.json"  # Replace with the actual path to your 'employee.json' file
df = spark.read.json(file_path)

# a. Display the DataFrame after incrementing everyone’s age by two years.
df_incremented_age = df.withColumn("age", col("age") + 2)
df_incremented_age.show()

# b. Filter all the employees above age 30 and display the result.
df_above_30 = df.filter(col("age") > 30)
df_above_30.show()

# c. Count the number of people with the same ages. (use the ‘groupBy’ function for the same.)
age_counts = df.groupBy("age").count()
age_counts.show()

# d. Creating a temporary view ’employee’ of ‘df’ DataFrame.
df.createOrReplaceTempView("employee")

# e. Perform a ‘select’ operation on our ’employee’ view to display the table into ‘sqlDF’.
sql_query = "SELECT * FROM employee"
sqlDF = spark.sql(sql_query)

# f. Display the results of ‘sqlDF’.
sqlDF.show()

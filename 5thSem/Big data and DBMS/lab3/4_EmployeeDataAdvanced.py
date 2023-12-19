# Import necessary classes and functions
from pyspark.sql import SparkSession
from pyspark.sql import Row

# Create a Spark session
spark = SparkSession.builder.appName("EmployeeData").getOrCreate()

# a. Create a class 'Employee' to store name and age of an employee.
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# b. Assigning a Dataset 'caseClassDS' to store the record of Andrew.
andrew_record = Employee(name="Andrew", age=28)
caseClassDS = spark.createDataFrame([Row(name=andrew_record.name, age=andrew_record.age)])

# c. Display the Dataset 'caseClassDS'.
print("Dataset 'caseClassDS':")
caseClassDS.show()

# d. Create a primitive Dataset to demonstrate mapping of DataFrames into Datasets.
data = [("John", 30), ("Alice", 25), ("Bob", 35)]
columns = ["name", "age"]
primitiveDS = spark.createDataFrame(data, columns)

# e. Assign the above sequence into an array.
array_of_datasets = [caseClassDS, primitiveDS]

# f. Display the result.
for index, dataset in enumerate(array_of_datasets, start=1):
    print(f"Dataset {index}:")
    dataset.show()

# Stop the Spark session
spark.stop()

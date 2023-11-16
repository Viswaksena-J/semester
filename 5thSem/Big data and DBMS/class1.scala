val dataset =  Seq((0,"hello"),(1,"world")).toDF("id","text")
val upper: String=> String = _.toUpperCase
import org.apache.spark.sql.functions.udf
val upperUDF = udf(upper)
dataset.withColumn("upper",upperUDF('text)).show
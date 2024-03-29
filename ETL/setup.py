import os
import findspark
findspark.init("C:\spark-3.2.4-bin-hadoop3.2")
from pyspark.sql import SparkSession
from pyspark.sql.functions import date_format
import time
start_time = time.time()
import pyspark.sql.functions as F
import datetime
from pyspark.sql.functions import lit, col, concat,format_string, monotonically_increasing_id, \
    split, explode, when, array, size, date_format, dayofweek, month, quarter, year, concat, hour, minute, second, to_timestamp, to_date, dayofmonth
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, DateType, DoubleType, DateType
import pandas as pd

#config
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"
spark = SparkSession.builder.appName('ETL Application').\
    config("spark.driver.bindAddress","localhost").\
    config("spark.ui.port","4040").\
    config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1").\
    getOrCreate()
spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")
spark.sparkContext.setLogLevel("off")
sc = spark.sparkContext

URI = sc._gateway.jvm.java.net.URI
Path = sc._gateway.jvm.org.apache.hadoop.fs.Path 
FileSystem = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
Configuration = sc._gateway.jvm.org.apache.hadoop.conf.Configuration
fs = FileSystem.get(URI("hdfs://localhost:19000"), Configuration())

dwh_tables = ["Dim_Category", "Dim_Product", "Dim_ConfigurableProduct","Dim_Inventory", "Dim_Seller", "Dim_Brand", "Dim_Shipping", \
    "Dim_Gift", "Dim_Url", "Dim_Time_collect_id", "Dim_Time_collect_detail", "Fact_Sales", "Fact_Product"]

collections = ['collection_products_serp', 'collection_products_detail']
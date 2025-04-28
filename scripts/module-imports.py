try:
    from databricks.connect import DatabricksSession
    # Attempt to create a Databricks session
    spark = DatabricksSession.builder.getOrCreate()
    print("Databricks Connect is available. Using DatabricksSession.")
except ImportError:
    from pyspark.sql import SparkSession
    # Optionally configure the SparkSession for local testing
    spark = SparkSession.builder.master("local[*]").getOrCreate()
    print("Databricks Connect is not available. Using local SparkSession.")
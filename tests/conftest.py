import pytest

@pytest.fixture(scope="session")
def get_spark():
    """
    Returns a Spark session.
    If Databricks Connect is available, uses DatabricksSession; 
    otherwise, falls back to SparkSession.
    """
    try:
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.getOrCreate()
    except ImportError:
        from pyspark.sql import SparkSession
        # Optionally configure the SparkSession for local testing
        spark = SparkSession.builder.getOrCreate()
    return spark
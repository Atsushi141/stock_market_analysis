import pytest
import os
import sys
sys.path.append(os.getcwd())


@pytest.fixture()
def get_spark():
  try:
    from pyspark.sql import SparkSession
    return SparkSession.builder.getOrCreate()
  except:
    from databricks.connect import DatabricksSession
    print("Databricks Session is in creation")
    return DatabricksSession.builder.getOrCreate()


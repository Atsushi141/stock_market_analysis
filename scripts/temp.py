from databricks.connect import DatabricksSession

# .databrickscfgファイルに設定がない場合
# spark = DatabricksSession.builder.serverless().profile("DEFAULT").getOrCreate()

# .databrickscfgにserverless_compute_id = autoを設定している場合
spark = DatabricksSession.builder.getOrCreate() 


spark.sql("select 1").show()
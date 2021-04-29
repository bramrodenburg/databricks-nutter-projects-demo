# Databricks notebook source
default_name = "DefaultUnknown"

dbutils.widgets.text("name", default_name, "Enter user name")
user_name = dbutils.widgets.get("name")
if user_name == "DefaultUnknown":
  greeting = "ERROR"
else:
  greeting = f"Hello {user_name}"
  secret = dbutils.secrets.get(scope="cicd", key="mytoken")
  print(secret)  # Will be redacted
  
dbutils.notebook.exit(greeting)

# COMMAND ----------

# Change me: 987654321

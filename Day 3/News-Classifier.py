from transformers import pipeline
import pandas as pd
import os

categories = [
    "sports",
    "politics",
    "technology",
    "business",
    "entertainment"
    ]
print("Model is in loading phase...")
classifier = pipeline ("zero-shot-classification",model = "facebook/bart-large-mnli")
print("Model is Loaded")

def classify_news(text):
  result = classifier(text, candidate_labels =  categories)

  label = result['labels'][0]
  score = result['scores'][0]

  print(f"News: {text}")
  print(f"Lable: {label} with {score}")
  print("-"*20)

classify_news("Pakistan won T20 world cup in 2009")
classify_news("Donald Trumph attacked on Iran")

#Use of CSV file
df = pd.read_csv("/content/sample_data/sample_news.csv")

df["category"] = df["headline"].apply(lambda x: classifier(x, categories) ["labels"][0])
print(df)
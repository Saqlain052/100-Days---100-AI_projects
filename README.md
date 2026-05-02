# 🚀 100 Days of AI

## 📖 About
This repository contains my 100 Days AI journey where I build real-world AI projects daily.

## 🎯 Goals
- Learn AI/ML concepts
- Build real-world projects
- Share progress publicly

## 📅 Progress
| Day | Project |
|-----|--------|
| Day 1 | Spam Detection |
| Day 2 | Coming Soon |

## 🛠 Tech Stack
- Python
- Machine Learning
- NLP
- Transformers

## 📌 Author
Saqlain (Saki)

# 🚀 Day 2 – Toxic Comment Detector  

This project is an advanced Toxic Comment Detection System that uses Natural Language Processing (NLP) and Machine Learning to classify text into multiple toxicity categories. Instead of just detecting whether a comment is toxic or not, this model identifies different types of harmful behavior in text.  

The system preprocesses input text (cleaning, lowercasing, removing noise), converts it into numerical features using TF-IDF, and applies a machine learning model to predict multiple labels for each comment. This makes it useful for real-world moderation systems where different types of toxicity need to be handled separately.  

### 🧠 Toxicity Categories  
- 🤬 Overall Toxicity  
- 💀 Severe Toxicity  
- 🤮 Obscene Language  
- 😡 Threats  
- 👊 Insults  
- 🎯 Identity Attacks  

### 🛠 Tech Stack  
Python, Scikit-learn, Pandas, NumPy, NLP  

### ⚙️ Workflow  
Data → Text Cleaning → Feature Extraction (TF-IDF) → Multi-label Classification → Prediction  

### 📊 Example  
Input: "You are a stupid idiot, I will hurt you"  
Output: Toxic 🤬 | Insult 👊 | Threat 😡  

Input: "Great job, keep going!"  
Output: Non-Toxic ✅ 

# 📰 Day 3 — News Classifier

> **Hugging Face 100 Tasks Roadmap | Saki Edition**

---

## 🚀 Project Overview
This project automatically classifies news headlines into different categories using AI.

It understands the text and predicts the most relevant category without any manual training data.

---

## 📌 Categories Supported
- ⚽ Sports  
- 🏛️ Politics  
- 💻 Technology  
- 💼 Business  
- 🎬 Entertainment  

---

## 🧠 Key Concept — Zero-Shot Learning
Unlike traditional ML models:

### ❌ Normal Approach:
- Dataset required  
- Model training needed  
- Time-consuming process  

### ✅ Zero-Shot Approach:
- Only provide categories  
- Model understands context itself  
- No training required ✨  

---

## ⚔️ Day Comparison

| Feature        | Day 1 (Spam) | Day 2 (Toxic) | Day 3 (News) |
|----------------|-------------|--------------|--------------|
| Task Type      | Binary      | Multi-label  | Multi-class  |
| Model          | DistilBERT  | Detoxify     | BART-MNLI    |
| Special Feature | Classification | Toxic Score | **Zero-Shot AI** |

---

## 🛠️ Tech Stack
- 🤗 Hugging Face Transformers (BART-MNLI)
- 🐍 Python
- 📊 Pandas

---

## ⚙️ Installation

```bash
pip install transformers torch pandas

# 🌐 Urdu ↔ English Translator (CSV Supported)

## 📌 Overview

This project is a simple **Urdu ↔ English translation system** built using Hugging Face Transformers.
It allows you to:

* Translate individual sentences
* Translate entire CSV files (bulk translation)

---

## 🚀 Features

* 🔁 Urdu to English translation
* 🔁 English to Urdu translation
* 📄 CSV file support (bulk processing)
* ⚡ Clean and simple implementation

---

## 🛠️ Technologies Used

* Python
* Transformers (Hugging Face)
* Pandas

---

## 📦 Installation

```bash
pip install transformers pandas sacremoses torch
```

---

## 📂 Project Structure

```
project/
│── main.py
│── sample_translations.csv
│── sample_translations_translated.csv (output)
```

---

## 📄 Input CSV Format

Your CSV file should contain:

```csv
id,urdu_text,english_text
1,پاکستان ایک خوبصورت ملک ہے, Pakistan is a beautiful country
2,مجھے پروگرامنگ پسند ہے, I love programming
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## ⚙️ How It Works

1. Loads pre-trained translation models
2. Reads CSV file
3. Translates:

   * `urdu_text` → English
   * `english_text` → Urdu
4. Saves output in a new CSV file

---

## 📤 Output

A new file will be generated:

```
sample_translations_translated.csv
```

With extra columns:

* `urdu_translated`
* `english_translated`

---

## 🧠 Example Output

| urdu_text  | english_text | urdu_translated | english_translated |
| ---------- | ------------ | --------------- | ------------------ |
| پاکستان... | Pakistan...  | Pakistan...     | پاکستان...         |

---

## ⚠️ Notes

* First run may take time (model download)
* Large files may take longer to process
* GPU can speed up translation

---

## 🎯 Future Improvements

* Streamlit Web App
* Batch Processing (faster)
* Language Auto Detection
* API Deployment

---

## 👨‍💻 Author

**Saqlain (Saki)**
AI Enthusiast | Future AI Engineer 🚀

---

# Text Summarizer using Transformers

## Overview
This project is a simple text summarization tool built using Hugging Face Transformers. It uses the model `sshleifer/distilbart-cnn-12-6` to generate concise summaries from long text.

## Model Used
- sshleifer/distilbart-cnn-12-6

## Features
- Summarizes long text into short, medium, or long versions
- Uses pre-trained transformer model
- Calculates word reduction percentage
- Simple and easy to use function

## Requirements
Install dependencies before running the project:

```bash
pip install transformers torch
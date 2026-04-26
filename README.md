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


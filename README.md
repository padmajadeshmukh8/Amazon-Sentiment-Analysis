#  Amazon Product Review Sentiment Analysis using Deep Learning

## 📌 Overview

This project implements a **Deep Learning-based Sentiment Analysis System** for Amazon product reviews. The objective is to automatically classify customer reviews as **Positive** or **Negative** by analyzing review text using Natural Language Processing (NLP) and multiple Deep Learning architectures.

The project compares the performance of several neural network models, including **CNN, LSTM, BiLSTM, GRU, and BiGRU**, to identify the most effective approach for sentiment classification. Various evaluation metrics such as Accuracy, Precision, Recall, F1-Score, and ROC-AUC are used to assess model performance.

---

## 🎯 Objectives

* Analyze customer opinions from Amazon product reviews.
* Perform sentiment classification using Deep Learning.
* Compare multiple neural network architectures.
* Evaluate models using comprehensive performance metrics.
* Visualize model performance and prediction results.

---

## 📂 Dataset

The project uses an Amazon Product Reviews dataset containing:

| Feature    | Description                |
| ---------- | -------------------------- |
| reviewText | Customer review text       |
| overall    | Product rating (1–5 stars) |

### Sentiment Label Creation

Sentiments are generated from review ratings:

* Ratings > 3 → Positive
* Ratings ≤ 3 → Negative

This converts the problem into a binary sentiment classification task.

---

## ⚙️ Methodology

### 1. Data Preprocessing

The following preprocessing steps were performed:

* Missing value inspection
* Review text extraction
* Sentiment label generation
* Train-test split
* Text tokenization
* Sequence generation
* Sequence padding

---

### 2. Text Vectorization

Customer reviews were converted into numerical sequences using:

* Keras Tokenizer
* Vocabulary Size: 10,000 words
* Maximum Review Length: 200 tokens

---

### 3. Deep Learning Models

The following architectures were implemented and compared:

#### CNN (Convolutional Neural Network)

* Embedding Layer
* Conv1D Layer
* Global Max Pooling
* Dense Layers
* Dropout Regularization

#### LSTM (Long Short-Term Memory)

* Embedding Layer
* LSTM Layer
* Dense Output Layer

#### BiLSTM (Bidirectional LSTM)

* Embedding Layer
* Bidirectional LSTM
* Dense Output Layer

#### GRU (Gated Recurrent Unit)

* Embedding Layer
* GRU Layer
* Dense Output Layer

#### BiGRU (Bidirectional GRU)

* Embedding Layer
* Bidirectional GRU
* Dense Output Layer

---

## 🧠 Deep Learning Pipeline

```text
Amazon Reviews Dataset
          ↓
Data Preprocessing
          ↓
Sentiment Label Creation
          ↓
Train-Test Split
          ↓
Text Tokenization
          ↓
Sequence Padding
          ↓
Embedding Layer
          ↓
Model Training
(CNN, LSTM, BiLSTM, GRU, BiGRU)
          ↓
Model Evaluation
          ↓
Performance Comparison
          ↓
Best Model Selection
```

---

## 📊 Exploratory Data Analysis

### Sentiment Distribution

* Visualized Positive vs Negative reviews using a pie chart.

### Review Length Analysis

* Analyzed distribution of review lengths using histograms.

---

## 📈 Evaluation Metrics

Each model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC Score
* Confusion Matrix

These metrics provide a comprehensive assessment of classification effectiveness.

---

## 📉 Visualizations

The project includes:

### Data Analysis

* Sentiment Distribution Pie Chart
* Review Length Distribution Histogram

### Model Evaluation

* Deep Learning Model Comparison Chart
* Accuracy Ranking Visualization
* ROC Curve Comparison
* Confusion Matrix Heatmap
* Performance Metrics Comparison

---

## 🛠 Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* TensorFlow
* Keras
* Scikit-learn

### Development Environment

* Google Colab
* Jupyter Notebook

---

## 🏆 Key Features

* End-to-end sentiment analysis pipeline.
* Deep Learning-based text classification.
* Multiple neural network architecture comparison.
* Automated sentiment label generation.
* ROC-AUC based model evaluation.
* Visual performance analysis.

---

## 📊 Results

* Successfully classified Amazon reviews into Positive and Negative sentiments.
* Compared CNN, LSTM, BiLSTM, GRU, and BiGRU architectures.
* Evaluated models using multiple performance metrics.
* Generated ROC curves for comparative analysis.
* Identified the best-performing model based on classification accuracy and ROC-AUC.

---

## 💼 Business Applications

* Customer Feedback Analytics
* Product Review Monitoring
* Brand Reputation Management
* Customer Satisfaction Analysis
* E-commerce Intelligence
* Consumer Behavior Analysis

---

## 📁 Project Structure

```text
Amazon-Sentiment-Analysis/
│
├── dataset/
│   └── amazon_reviews.csv
│
├── notebooks/
│   └── amazon_sentiment_analysis.ipynb
│
├── images/
│   ├── sentiment_distribution.png
│   ├── review_length_distribution.png
│   ├── roc_curve.png
│   ├── confusion_matrix.png
│   └── model_comparison.png
│
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/your-username/amazon-sentiment-analysis.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Notebook

```bash
jupyter notebook
```

### Run the Project

Execute all notebook cells sequentially to reproduce the results.


## 👩‍💻 Author

**Padmaja Deshmukh**

Machine Learning | Deep Learning | Natural Language Processing | Data Analytics

---

## 📜 License

This project is intended for educational, academic, and portfolio purposes.

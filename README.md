# 💳 Credit Card Fraud Detection

Credit card fraud is a growing threat in the digital financial landscape, with billions lost annually and customer trust on the line. Detecting fraud accurately — without overwhelming users with false positives — is a complex, high-stakes challenge due to the rarity and evolving nature of fraudulent behavior.

This project investigates **unsupervised anomaly detection techniques** using anonymized real-world credit card transaction data. The models used are particularly suited for **highly imbalanced datasets**, where fraudulent transactions represent less than 0.2% of the data.

---

## 🔍 Project Overview

Using Python and libraries such as `scikit-learn`, `pandas`, and `matplotlib`, the following tasks were performed:

- **Data exploration & visualization**: To understand class distribution and feature behavior
- **Model training & evaluation**:
  - **Isolation Forest**
  - **Local Outlier Factor (LOF)**
  - **One-Class SVM**
- **Feature selection** using Random Forest to improve model efficiency
- **Performance metrics**: Precision, Recall, F1-score, Confusion Matrix
- **Custom visualization** of fraud detection results by model

---

## 🧠 Motivation

Most real-world fraud detection problems are unsupervised in nature, meaning we often don't have reliable labeled data for fraudulent behavior. This project simulates that by testing how well models can learn patterns of "normal" behavior — and flag deviations that might represent fraud.

---

## 📊 Exploratory Data Analysis

The dataset features 28 PCA-transformed variables (`V1` to `V28`), along with `Time`, `Amount`, and the target variable `Class` (0 = valid, 1 = fraud). We used histograms and density plots to visualize feature distributions and class imbalance.


---

## 🔍 Feature Importance (Random Forest)

Random Forest was trained as a supervised baseline to extract top features by importance, guiding the dimensionality reduction for unsupervised models.

---

## 🤖 Model Performance & Verdict Visualization

Each model was evaluated with detailed classification metrics and custom scatterplots that highlight:

- **TP**: Correctly identified fraud  
- **FN**: Missed fraud  
- **FP**: False alarms  
- **TN**: Correctly identified valid transactions  

### Example: SVM Verdict Visualization



## ✅ Key Results & Insights

| Model                | Fraud Recall (%) | Fraud Precision (%) | F1-Score | False Positive Rate |
|---------------------|------------------|----------------------|----------|----------------------|
| Isolation Forest     | 59.5             | 59.0                 | 0.59     | 0.06%               |
| One-Class SVM        | 69.0             | 17.0                 | 0.28     | 0.49%               |
| Local Outlier Factor | ~0.0             | ~0.0                 | ~0.0     | 0.15%               |

- **Isolation Forest** had the best overall balance between fraud recall and false positive rate.
- **One-Class SVM** improved drastically with feature reduction and scaling, but at some cost in precision.
- **LOF** was not well-suited for this dataset without further tuning or context.


# Project Overview: AI Text Detection Model

## Introduction

This project focuses on developing a robust AI model to differentiate between human-generated and AI-generated text. Leveraging datasets translated from English to Korean and various machine learning approaches, our goal is to achieve a performance score of 0.90 or higher in terms of ROC-AUC and F1 score metrics.

## Motivation

- **Dataset Availability:** There is a critical need for diverse datasets to train more effective models; this project contributes by enhancing dataset availability in Korean.
- **Technological Advancement:** Improving detection models can help in identifying AI-generated text, crucial for maintaining the integrity of information on the internet.

## Models and Methods

We experimented with various models and methods across three primary categories:

### 1. Supervised Learning
- **Models Used:**
  - [Ghost Buster](https://arxiv.org/abs/2305.15047)
  - Mistral 7B with Lora Fine Tuning
- **Algorithms:**
  - LightGBM (0.45)
  - Multinomial Naive Bayes (0.45)
  - SGD Classifier (0.1)
- **Hardware:**
  - Nvidia A100 for training

### 2. Unsupervised Learning
- **Weak Labeling Approach:**
  - Thresholds set for human-generated scores (>0.8) and AI-generated scores (<0.2)

### 3. Zero-Shot Inference
- **Models Utilized:**
  - GPT 3.5, GPT 4, GPT 4o
  - Google Gemini 1.0 Pro

## Train Dataset

The project utilizes a [Google translator API](https://cloud.google.com/translate/docs/reference/rest) to create a bilingual dataset: [DAIGT DataSet](https://www.kaggle.com/datasets/thedrcat/daigt-v2-train-dataset)
- **Source:** English dataset
- **Target:** Translated Korean dataset

### Inference Dataset

[university entrance exams in Korea, specifically in the humanities and social sciences](https://www.kaggle.com/datasets/umgeeyo/korean-essay)

## Results

Performance metrics for the models are as follows:
- **Supervised Learning:** Best ROC-AUC of 0.98 with Mistral 7B and F1 score of 0.92 with Ghost Buster.
- **Unsupervised Learning:** Best ROC-AUC of 0.96 with Mistral 7B and F1 score of 0.91.
- **Zero-Shot Learning:** Stable performance across different versions of GPT with an F1 score around 0.85.

## Conclusion

Our results demonstrate the feasibility of using advanced machine learning techniques for distinguishing between human and AI-generated texts in Korean. Ongoing improvements and expansions of the dataset will further enhance the model's accuracy and reliability.



## Model Performance Metrics

| Category    | Metric   | Test  | Ghost Buster | Mistral 7B | Gemini | GPT 3.5 | GPT 4 | GPT 4o |
|-------------|----------|-------|--------------|------------|--------|---------|-------|--------|
| Supervised  | ROC-AUC  | 0.91  | 0.98         | 0.98       | -   | -   |  -   |  -     |
|             | F1       | 0.89  | 0.92         | 0.92       | -   | -   | -   | -     |
| Unsupervised| ROC-AUC  | 0.95  | 0.96         | 0.96       | 0.38   | 0.54    | 0.45  | 0.40   |
|             | F1       | 0.90  | 0.91         | 0.91       | 0.80   | 0.82    | 0.85  | 0.85   |
| Zero shot   | ROC-AUC  | -     | -            | -          | 0.46   | 0.53    | 0.58  | 0.45   |
|             | F1       | -     | -            | -          | 0.78   | 0.85    | 0.85  | 0.85   |
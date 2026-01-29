# fun-with-evaluation

A comprehensive repository for studying and understanding ML/DL evaluation metrics with practical examples.

## 📚 Overview

This repository provides clear explanations and working examples for evaluating machine learning and deep learning models. All examples use mocked data, so you can run them without training actual models.

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Run Examples

```bash
# Classification metrics
python classification/example.py

# Regression metrics
python regression/example.py

# Forecasting metrics
python forecasting/example.py

# Deep learning evaluation
python deep_learning/example.py

# Computer vision metrics
python computer_vision/example.py

# NLP metrics
python nlp/example.py

# Model performance
python model_performance/example.py

# Cross-validation utilities
python utils/cross_validation.py
```

## 📂 Repository Structure

```
fun-with-evaluation/
├── classification/          # Classification metrics (Accuracy, F1, ROC-AUC, etc.)
├── regression/             # Regression metrics (MSE, RMSE, R², etc.)
├── forecasting/            # Time series metrics (MASE, SMAPE, Tracking Signal, etc.)
├── deep_learning/          # Training dynamics & overfitting detection
├── computer_vision/        # IoU, mAP, Dice, PSNR, etc.
├── nlp/                    # BLEU, ROUGE, Perplexity, etc.
├── model_performance/      # Latency, throughput, memory usage
├── utils/                  # Cross-validation & statistical testing
└── requirements.txt        # Dependencies
```

## 📖 Topics Covered

### 1. Classification Metrics
- Accuracy, Precision, Recall, F1-Score
- ROC-AUC, Confusion Matrix
- Multi-class evaluation (macro/micro/weighted)

### 2. Regression Metrics
- MSE, RMSE, MAE
- R² (Coefficient of Determination)
- MAPE (Mean Absolute Percentage Error)

### 3. Forecasting Metrics
- MASE (Mean Absolute Scaled Error)
- SMAPE (Symmetric MAPE)
- Forecast Bias & Tracking Signal
- Directional Accuracy
- Prediction Intervals & Coverage

### 4. Deep Learning Evaluation
- Training & validation loss curves
- Overfitting & underfitting detection
- Learning rate analysis
- Convergence monitoring

### 5. Computer Vision
- **Object Detection**: IoU, mAP
- **Segmentation**: Dice coefficient, Pixel accuracy, mIoU
- **Image Quality**: PSNR, SSIM

### 6. NLP Metrics
- **Translation**: BLEU, METEOR
- **Summarization**: ROUGE
- **Language Models**: Perplexity
- **Embeddings**: Cosine similarity

### 7. Model Performance
- Inference latency & throughput
- Memory usage & model size
- FLOPs count
- Optimization techniques

### 8. Evaluation Utilities
- K-Fold & Stratified cross-validation
- Statistical significance testing
- Bias-variance tradeoff

## 🎯 Key Features

- ✅ **No real models needed** - All examples use mocked data
- ✅ **Practical code** - Ready-to-run Python scripts
- ✅ **Visual outputs** - Generates plots for better understanding
- ✅ **Clear explanations** - Each metric explained with use cases
- ✅ **Best practices** - When to use which metric

## 📊 Example Output

Each example generates:
- Console output with calculated metrics
- Visualization plots saved as PNG files
- Clear interpretation of results

## 🤝 Contributing

This repository is designed to help others learn about ML/DL evaluation. Feel free to:
- Add new evaluation metrics
- Improve explanations
- Add more examples
- Fix issues

## 📝 License

Open for educational purposes.

## 🔗 Resources

- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Deep Learning Book - Regularization](https://www.deeplearningbook.org/contents/regularization.html)
- [Papers with Code - Evaluation Metrics](https://paperswithcode.com/methods/category/evaluation-metrics)

---

**Happy Learning! 🎓**

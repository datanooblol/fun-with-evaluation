# Classification Metrics

## Overview
Classification metrics evaluate how well a model predicts categorical outcomes.

## Key Metrics

### 1. Accuracy
- **Formula**: (TP + TN) / (TP + TN + FP + FN)
- **Use**: Overall correctness
- **Limitation**: Misleading with imbalanced datasets

**Business Use Cases:**
- **Balanced datasets**: Product categorization (equal distribution)
- **Quality control**: Defect detection when defect rate ~50%
- **A/B testing**: When classes are naturally balanced

**When NOT to use:**
- Fraud detection (0.1% fraud rate) - 99.9% accuracy by predicting "no fraud" always
- Rare disease diagnosis - High accuracy doesn't mean good detection

### 2. Precision
- **Formula**: TP / (TP + FP)
- **Use**: How many predicted positives are actually positive

**Business Use Cases:**
- **Email spam filter**: False positives = important emails lost → Use high precision
- **Product recommendations**: Bad recommendations hurt user trust
- **Credit card fraud alerts**: Too many false alarms annoy customers
- **Medical screening**: False positives lead to unnecessary treatments/anxiety

**Real-world scenario**: E-commerce recommendation system - Better to show fewer but accurate recommendations than many irrelevant ones.

### 3. Recall (Sensitivity)
- **Formula**: TP / (TP + FN)
- **Use**: How many actual positives were found

**Business Use Cases:**
- **Cancer detection**: Missing a case (false negative) is life-threatening
- **Fraud detection**: Missing fraud costs money, false alarms are acceptable
- **Security threats**: Better to investigate false alarms than miss real threats
- **Customer churn prediction**: Missing at-risk customers = lost revenue

**Real-world scenario**: Airport security screening - Better to flag innocent people (false positive) than let threats through (false negative).

### 4. F1-Score
- **Formula**: 2 × (Precision × Recall) / (Precision + Recall)
- **Use**: Harmonic mean of precision and recall

**Business Use Cases:**
- **Information retrieval**: Balance between finding all relevant docs and avoiding irrelevant ones
- **Resume screening**: Find qualified candidates without overwhelming HR with bad matches
- **Content moderation**: Remove harmful content while preserving legitimate posts
- **Imbalanced datasets**: When you need both precision and recall

**Real-world scenario**: Job application filtering - Need to find qualified candidates (recall) without flooding recruiters with unqualified ones (precision).

### 5. ROC-AUC
- **Range**: 0 to 1 (0.5 = random, 1 = perfect)
- **Use**: Model's ability to distinguish between classes

**Business Use Cases:**
- **Model comparison**: Choose best model regardless of threshold
- **Credit scoring**: Rank customers by risk, adjust threshold based on business needs
- **Marketing campaigns**: Rank leads by conversion probability
- **Medical diagnosis**: When threshold varies by context (screening vs confirmation)

**Real-world scenario**: Credit card approval - Business can adjust approval threshold based on risk appetite without retraining model. High AUC means good ranking ability.

### 6. Confusion Matrix
- Visual representation of TP, TN, FP, FN
- Shows where model makes mistakes

**Business Use Cases:**
- **Error analysis**: Understand which classes are confused
- **Cost-benefit analysis**: Calculate business impact of each error type
- **Multi-class problems**: See which categories are misclassified

**Real-world scenario**: Customer support ticket routing - See which ticket types are misrouted to understand where to improve.

## Multi-class Metrics

### Macro Average
- **Method**: Average metrics per class (equal weight)
- **Use**: When all classes equally important
- **Example**: Medical diagnosis with rare diseases - each disease matters equally

### Micro Average
- **Method**: Aggregate all classes (favors larger classes)
- **Use**: When larger classes more important
- **Example**: Document classification where common categories matter more

### Weighted Average
- **Method**: Weighted average by class support
- **Use**: Balance between macro and micro
- **Example**: E-commerce product categorization with natural class imbalance

## Decision Framework

**Choose Precision when:**
- False positives are expensive
- Resources to handle positives are limited
- User trust is critical

**Choose Recall when:**
- False negatives are dangerous/expensive
- You can handle false positives
- Missing cases has severe consequences

**Choose F1 when:**
- Need balance
- Imbalanced datasets
- Both errors matter

**Choose ROC-AUC when:**
- Comparing models
- Threshold will be tuned later
- Ranking quality matters

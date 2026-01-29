import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)
import matplotlib.pyplot as plt
import seaborn as sns

# Mock binary classification data
np.random.seed(42)
y_true = np.random.randint(0, 2, 100)
y_pred = y_true.copy()
y_pred[np.random.choice(100, 20, replace=False)] = 1 - y_pred[np.random.choice(100, 20, replace=False)]
y_proba = np.random.rand(100)

print("=== Binary Classification Metrics ===\n")

# Basic metrics
print(f"Accuracy:  {accuracy_score(y_true, y_pred):.3f}")
print(f"Precision: {precision_score(y_true, y_pred):.3f}")
print(f"Recall:    {recall_score(y_true, y_pred):.3f}")
print(f"F1-Score:  {f1_score(y_true, y_pred):.3f}")
print(f"ROC-AUC:   {roc_auc_score(y_true, y_proba):.3f}\n")

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(cm)

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0])
axes[0].set_title('Confusion Matrix')
axes[0].set_ylabel('True Label')
axes[0].set_xlabel('Predicted Label')

fpr, tpr, _ = roc_curve(y_true, y_proba)
axes[1].plot(fpr, tpr, label=f'ROC (AUC={roc_auc_score(y_true, y_proba):.2f})')
axes[1].plot([0, 1], [0, 1], 'k--', label='Random')
axes[1].set_xlabel('False Positive Rate')
axes[1].set_ylabel('True Positive Rate')
axes[1].set_title('ROC Curve')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('classification/binary_metrics.png')
print("\n✓ Saved visualization to 'classification/binary_metrics.png'")

# Multi-class example
print("\n=== Multi-class Classification ===\n")
y_true_multi = np.random.randint(0, 3, 150)
y_pred_multi = y_true_multi.copy()
y_pred_multi[np.random.choice(150, 30, replace=False)] = np.random.randint(0, 3, 30)

print(classification_report(y_true_multi, y_pred_multi, target_names=['Class 0', 'Class 1', 'Class 2']))

import numpy as np
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import accuracy_score

def cross_validate_mock(X, y, n_splits=5):
    """Mock cross-validation"""
    kf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    scores = []
    
    for train_idx, val_idx in kf.split(X, y):
        # Mock predictions
        y_pred = y[val_idx].copy()
        flip_idx = np.random.choice(len(val_idx), size=int(len(val_idx) * 0.1), replace=False)
        y_pred[flip_idx] = 1 - y_pred[flip_idx]
        
        score = accuracy_score(y[val_idx], y_pred)
        scores.append(score)
    
    return scores

def statistical_test(scores1, scores2):
    """Paired t-test for model comparison"""
    from scipy import stats
    t_stat, p_value = stats.ttest_rel(scores1, scores2)
    return t_stat, p_value

print("=== Cross-Validation & Statistical Testing ===\n")

# Mock data
np.random.seed(42)
X = np.random.randn(100, 10)
y = np.random.randint(0, 2, 100)

# Cross-validation
print("--- K-Fold Cross-Validation ---")
scores = cross_validate_mock(X, y, n_splits=5)

print(f"Fold scores: {[f'{s:.3f}' for s in scores]}")
print(f"Mean CV Score: {np.mean(scores):.3f} ± {np.std(scores):.3f}")
print(f"Min: {np.min(scores):.3f}, Max: {np.max(scores):.3f}\n")

# Model comparison
print("--- Statistical Significance Testing ---")
model1_scores = cross_validate_mock(X, y, n_splits=5)
model2_scores = cross_validate_mock(X, y, n_splits=5)

print(f"Model 1: {np.mean(model1_scores):.3f} ± {np.std(model1_scores):.3f}")
print(f"Model 2: {np.mean(model2_scores):.3f} ± {np.std(model2_scores):.3f}")

try:
    from scipy import stats
    t_stat, p_value = statistical_test(model1_scores, model2_scores)
    print(f"\nPaired t-test:")
    print(f"t-statistic: {t_stat:.3f}")
    print(f"p-value: {p_value:.3f}")
    
    if p_value < 0.05:
        print("✓ Difference is statistically significant (p < 0.05)")
    else:
        print("✗ No significant difference (p >= 0.05)")
except ImportError:
    print("\nNote: Install scipy for statistical testing: pip install scipy")

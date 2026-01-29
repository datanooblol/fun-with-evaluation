import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Mock regression data
np.random.seed(42)
y_true = np.random.randn(100) * 10 + 50
y_pred = y_true + np.random.randn(100) * 3

print("=== Regression Metrics ===\n")

# Calculate metrics
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)
mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100

print(f"MSE:   {mse:.3f}")
print(f"RMSE:  {rmse:.3f}")
print(f"MAE:   {mae:.3f}")
print(f"R²:    {r2:.3f}")
print(f"MAPE:  {mape:.2f}%")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].scatter(y_true, y_pred, alpha=0.5)
axes[0].plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2)
axes[0].set_xlabel('True Values')
axes[0].set_ylabel('Predictions')
axes[0].set_title(f'Predictions vs True (R²={r2:.3f})')
axes[0].grid(True)

residuals = y_true - y_pred
axes[1].scatter(y_pred, residuals, alpha=0.5)
axes[1].axhline(y=0, color='r', linestyle='--', lw=2)
axes[1].set_xlabel('Predictions')
axes[1].set_ylabel('Residuals')
axes[1].set_title('Residual Plot')
axes[1].grid(True)

plt.tight_layout()
plt.savefig('regression/regression_metrics.png')
print("\n✓ Saved visualization to 'regression/regression_metrics.png'")

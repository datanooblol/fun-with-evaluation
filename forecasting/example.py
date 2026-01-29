import numpy as np
import matplotlib.pyplot as plt

# Mock time series data (e.g., daily sales)
np.random.seed(42)
n = 100
time = np.arange(n)

# True values with trend and seasonality
trend = 0.5 * time
seasonality = 10 * np.sin(2 * np.pi * time / 7)  # Weekly pattern
y_true = 50 + trend + seasonality + np.random.randn(n) * 2

# Predictions (slightly off)
y_pred = y_true + np.random.randn(n) * 3

print("=== Forecasting Metrics ===\n")

# 1. MASE (Mean Absolute Scaled Error)
mae = np.mean(np.abs(y_true - y_pred))
naive_mae = np.mean(np.abs(y_true[7:] - y_true[:-7]))  # Seasonal naive (7-day)
mase = mae / naive_mae

print(f"--- MASE (Mean Absolute Scaled Error) ---")
print(f"MAE: {mae:.2f}")
print(f"Naive MAE: {naive_mae:.2f}")
print(f"MASE: {mase:.3f}")
print(f"Interpretation: {'Better than naive' if mase < 1 else 'Worse than naive'}\n")

# 2. SMAPE (Symmetric MAPE)
smape = 100 * np.mean(np.abs(y_pred - y_true) / (np.abs(y_true) + np.abs(y_pred)))
print(f"--- SMAPE ---")
print(f"SMAPE: {smape:.2f}%")
print(f"Quality: {'Excellent' if smape < 10 else 'Good' if smape < 20 else 'Moderate'}\n")

# 3. Forecast Bias
bias = np.mean(y_pred - y_true)
print(f"--- Forecast Bias ---")
print(f"Bias: {bias:.2f}")
print(f"Direction: {'Over-forecasting' if bias > 0 else 'Under-forecasting' if bias < 0 else 'Unbiased'}\n")

# 4. Tracking Signal
cumulative_error = np.cumsum(y_pred - y_true)
mad = np.mean(np.abs(y_pred - y_true))
tracking_signal = cumulative_error[-1] / (mad * len(y_true))
print(f"--- Tracking Signal ---")
print(f"Tracking Signal: {tracking_signal:.2f}")
print(f"Status: {'Model OK' if abs(tracking_signal) < 4 else '⚠ Model needs retraining'}\n")

# 5. Directional Accuracy
direction_true = np.diff(y_true) > 0
direction_pred = np.diff(y_pred) > 0
directional_accuracy = np.mean(direction_true == direction_pred) * 100
print(f"--- Directional Accuracy ---")
print(f"Directional Accuracy: {directional_accuracy:.1f}%")
print(f"Quality: {'Good' if directional_accuracy > 60 else 'Poor'}\n")

# 6. Quantile Loss (for 90th percentile)
def quantile_loss(y_true, y_pred, quantile=0.9):
    error = y_true - y_pred
    return np.mean(np.maximum(quantile * error, (quantile - 1) * error))

# Simulate quantile forecasts
y_pred_median = y_pred  # 50th percentile
y_pred_90 = y_pred + 5  # 90th percentile (higher to avoid understocking)

ql_median = quantile_loss(y_true, y_pred_median, quantile=0.5)
ql_90 = quantile_loss(y_true, y_pred_90, quantile=0.9)

print(f"--- Quantile Loss ---")
print(f"Median forecast (τ=0.5): {ql_median:.2f}")
print(f"90th percentile (τ=0.9): {ql_90:.2f}")
print(f"Use case: Inventory with high stockout costs\n")

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Forecast vs Actual
axes[0, 0].plot(time, y_true, label='Actual', linewidth=2)
axes[0, 0].plot(time, y_pred, label='Forecast', alpha=0.7, linewidth=2)
axes[0, 0].set_xlabel('Time')
axes[0, 0].set_ylabel('Value')
axes[0, 0].set_title(f'Forecast vs Actual (MASE={mase:.2f})')
axes[0, 0].legend()
axes[0, 0].grid(True)

# Plot 2: Forecast Error
error = y_pred - y_true
axes[0, 1].plot(time, error, color='red', alpha=0.6)
axes[0, 1].axhline(y=0, color='black', linestyle='--', linewidth=1)
axes[0, 1].axhline(y=bias, color='blue', linestyle='--', linewidth=2, label=f'Bias={bias:.2f}')
axes[0, 1].set_xlabel('Time')
axes[0, 1].set_ylabel('Error')
axes[0, 1].set_title('Forecast Error Over Time')
axes[0, 1].legend()
axes[0, 1].grid(True)

# Plot 3: Error Distribution
axes[1, 0].hist(error, bins=30, edgecolor='black', alpha=0.7)
axes[1, 0].axvline(x=0, color='black', linestyle='--', linewidth=2)
axes[1, 0].axvline(x=bias, color='red', linestyle='--', linewidth=2, label=f'Bias={bias:.2f}')
axes[1, 0].set_xlabel('Error')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Error Distribution')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Cumulative Error (Tracking Signal)
cumulative_error_series = np.cumsum(error)
axes[1, 1].plot(time, cumulative_error_series, linewidth=2)
axes[1, 1].axhline(y=0, color='black', linestyle='--', linewidth=1)
axes[1, 1].fill_between(time, -4*mad*time, 4*mad*time, alpha=0.2, color='green', label='Control limits')
axes[1, 1].set_xlabel('Time')
axes[1, 1].set_ylabel('Cumulative Error')
axes[1, 1].set_title(f'Tracking Signal (TS={tracking_signal:.2f})')
axes[1, 1].legend()
axes[1, 1].grid(True)

plt.tight_layout()
plt.savefig('forecasting/forecasting_metrics.png')
print("✓ Saved visualization to 'forecasting/forecasting_metrics.png'")

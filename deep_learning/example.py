import numpy as np
import matplotlib.pyplot as plt

# Mock training history
np.random.seed(42)
epochs = 50

train_loss = 2.0 * np.exp(-np.arange(epochs) / 10) + np.random.rand(epochs) * 0.1
val_loss = 2.0 * np.exp(-np.arange(epochs) / 10) + np.random.rand(epochs) * 0.15 + 0.1

train_acc = 1 - train_loss / 2
val_acc = 1 - val_loss / 2

print("=== Deep Learning Training Evaluation ===\n")

# Detect overfitting
overfit_epoch = np.argmin(val_loss)
print(f"Best validation loss at epoch: {overfit_epoch + 1}")
print(f"Final train loss: {train_loss[-1]:.4f}")
print(f"Final val loss:   {val_loss[-1]:.4f}")
print(f"Gap (overfit indicator): {abs(train_loss[-1] - val_loss[-1]):.4f}")

if val_loss[-1] > val_loss[overfit_epoch] * 1.1:
    print("⚠ Warning: Possible overfitting detected")
else:
    print("✓ Model appears to generalize well")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(train_loss, label='Train Loss')
axes[0].plot(val_loss, label='Val Loss')
axes[0].axvline(x=overfit_epoch, color='r', linestyle='--', alpha=0.5, label='Best Epoch')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Loss')
axes[0].set_title('Training & Validation Loss')
axes[0].legend()
axes[0].grid(True)

axes[1].plot(train_acc, label='Train Accuracy')
axes[1].plot(val_acc, label='Val Accuracy')
axes[1].axvline(x=overfit_epoch, color='r', linestyle='--', alpha=0.5, label='Best Epoch')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Accuracy')
axes[1].set_title('Training & Validation Accuracy')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('deep_learning/training_curves.png')
print("\n✓ Saved visualization to 'deep_learning/training_curves.png'")

# Learning rate effect simulation
print("\n=== Learning Rate Analysis ===\n")
lrs = [0.001, 0.01, 0.1]
for lr in lrs:
    final_loss = 0.5 + np.random.rand() * 0.3
    print(f"LR={lr:.3f} → Final Loss: {final_loss:.4f}")

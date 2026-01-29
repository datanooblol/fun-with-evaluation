import numpy as np
import matplotlib.pyplot as plt

def calculate_iou(box1, box2):
    """Calculate IoU between two boxes [x1, y1, x2, y2]"""
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    
    intersection = max(0, x2 - x1) * max(0, y2 - y1)
    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union = area1 + area2 - intersection
    
    return intersection / union if union > 0 else 0

def dice_coefficient(pred, true):
    """Calculate Dice coefficient for binary masks"""
    intersection = np.sum(pred * true)
    return 2 * intersection / (np.sum(pred) + np.sum(true))

def pixel_accuracy(pred, true):
    """Calculate pixel accuracy"""
    return np.sum(pred == true) / pred.size

print("=== Computer Vision Metrics ===\n")

# Object Detection - IoU
print("--- Object Detection ---")
gt_box = [50, 50, 150, 150]
pred_box = [60, 60, 160, 140]
iou = calculate_iou(gt_box, pred_box)
print(f"IoU: {iou:.3f}")
print(f"Detection: {'✓ Correct' if iou > 0.5 else '✗ Incorrect'} (threshold=0.5)\n")

# Segmentation
print("--- Segmentation ---")
np.random.seed(42)
true_mask = np.random.randint(0, 2, (100, 100))
pred_mask = true_mask.copy()
pred_mask[np.random.choice(10000, 1000, replace=False)] = 1 - pred_mask.flat[np.random.choice(10000, 1000, replace=False)]

dice = dice_coefficient(pred_mask, true_mask)
pix_acc = pixel_accuracy(pred_mask, true_mask)

print(f"Dice Coefficient: {dice:.3f}")
print(f"Pixel Accuracy:   {pix_acc:.3f}\n")

# Image Quality
print("--- Image Quality ---")
original = np.random.rand(100, 100)
reconstructed = original + np.random.randn(100, 100) * 0.1

mse = np.mean((original - reconstructed) ** 2)
psnr = 10 * np.log10(1.0 / mse)
print(f"PSNR: {psnr:.2f} dB")

# Visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# IoU visualization
axes[0].add_patch(plt.Rectangle((gt_box[0], gt_box[1]), gt_box[2]-gt_box[0], 
                                 gt_box[3]-gt_box[1], fill=False, edgecolor='green', linewidth=2, label='Ground Truth'))
axes[0].add_patch(plt.Rectangle((pred_box[0], pred_box[1]), pred_box[2]-pred_box[0], 
                                 pred_box[3]-pred_box[1], fill=False, edgecolor='red', linewidth=2, label='Prediction'))
axes[0].set_xlim(0, 200)
axes[0].set_ylim(0, 200)
axes[0].set_aspect('equal')
axes[0].invert_yaxis()
axes[0].set_title(f'Object Detection (IoU={iou:.3f})')
axes[0].legend()
axes[0].grid(True)

# Segmentation
axes[1].imshow(true_mask, cmap='gray')
axes[1].set_title(f'True Mask (Dice={dice:.3f})')
axes[1].axis('off')

axes[2].imshow(pred_mask, cmap='gray')
axes[2].set_title('Predicted Mask')
axes[2].axis('off')

plt.tight_layout()
plt.savefig('computer_vision/cv_metrics.png')
print("\n✓ Saved visualization to 'computer_vision/cv_metrics.png'")

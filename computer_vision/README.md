# Computer Vision Metrics

## Overview
Specialized metrics for evaluating computer vision tasks.

## Object Detection

### 1. IoU (Intersection over Union)
- **Formula**: Area of Overlap / Area of Union
- **Range**: 0 to 1 (higher is better)
- **Use**: Measures bounding box accuracy
- **Threshold**: Typically 0.5 for "correct" detection

**Business Use Cases:**

**Autonomous vehicles**: Detect pedestrians/vehicles accurately
- IoU > 0.7: Safe detection, can brake appropriately
- IoU < 0.5: Dangerous - might miss pedestrian or brake unnecessarily
- **Impact**: Safety-critical, liability concerns

**Retail analytics**: Count customers in store zones
- IoU > 0.6: Accurate foot traffic analysis
- IoU < 0.5: Wrong zone attribution, bad business decisions
- **Impact**: Store layout optimization, staffing decisions

**Manufacturing defect detection**: Locate defects on products
- IoU > 0.8: Precise defect location for automated removal
- IoU < 0.6: Might remove good product or miss defect
- **Impact**: Waste reduction, quality assurance

**Security surveillance**: Detect intruders/suspicious objects
- IoU > 0.7: Accurate threat localization
- IoU < 0.5: False alarms or missed threats
- **Impact**: Security effectiveness, false alarm costs

**Real-world scenario**: Warehouse robot picking items. IoU < 0.5 means robot might grab wrong item or miss it entirely. Result: Wrong shipments, customer complaints, returns.

### 2. mAP (mean Average Precision)
- **Definition**: Mean of AP across all classes
- **Use**: Standard metric for object detection
- **Variants**: mAP@0.5, mAP@0.5:0.95 (COCO metric)

**Business Use Cases:**

**Autonomous driving**: Detect multiple object types (cars, pedestrians, signs)
- mAP > 0.8: Production-ready for assisted driving
- mAP < 0.6: Not safe for deployment
- **Impact**: Safety certification, regulatory approval

**Medical imaging**: Detect multiple abnormality types
- mAP > 0.85: Can assist radiologists
- mAP < 0.7: Too many missed detections
- **Impact**: Diagnostic accuracy, patient outcomes

**Agricultural monitoring**: Detect pests, diseases, ripe crops
- mAP > 0.75: Reliable for automated harvesting decisions
- mAP < 0.6: Manual inspection still needed
- **Impact**: Harvest efficiency, crop yield

**Real-world scenario**: Smart city traffic monitoring detecting cars, bikes, pedestrians. mAP = 0.85 means reliable for traffic optimization. mAP = 0.6 means too many missed detections for automated decisions.

### 3. Precision-Recall Curve
- **Precision**: TP / (TP + FP)
- **Recall**: TP / (TP + FN)
- **AP**: Area under PR curve

**Business Use Cases:**
- **Threshold tuning**: Adjust detection confidence based on business needs
- **Cost-benefit analysis**: Balance false positives vs false negatives
- **SLA definition**: Set performance guarantees for customers

**Real-world scenario**: Security camera system. High precision mode (fewer false alarms) for night shift. High recall mode (catch everything) for high-security areas.

## Segmentation

### 1. Pixel Accuracy
- **Formula**: Correct Pixels / Total Pixels
- **Limitation**: Biased toward large objects

**Business Use Cases:**

**Satellite imagery**: Land use classification
- 95% accuracy: Reliable for urban planning
- 85% accuracy: Too many errors for legal boundaries
- **Impact**: Zoning decisions, environmental monitoring

**Medical imaging**: Organ/tumor segmentation
- 98% accuracy: Acceptable for treatment planning
- 90% accuracy: Too risky for surgical guidance
- **Impact**: Treatment precision, patient safety

**When NOT to use**: Small object detection (tumor in large scan) - 99% accuracy by predicting "no tumor" everywhere.

### 2. Dice Coefficient (F1 for segmentation)
- **Formula**: 2 × |A ∩ B| / (|A| + |B|)
- **Range**: 0 to 1 (higher is better)
- **Use**: Overlap between prediction and ground truth

**Business Use Cases:**

**Medical imaging**: Tumor segmentation for radiation therapy
- Dice > 0.9: Safe for treatment planning
- Dice < 0.8: Manual correction needed
- **Impact**: Treatment effectiveness, patient safety
- **Cost**: Manual correction adds 30-60 min per case

**Autonomous vehicles**: Drivable area segmentation
- Dice > 0.85: Safe for autonomous navigation
- Dice < 0.75: Requires human supervision
- **Impact**: Autonomy level, safety

**Agriculture**: Crop/weed segmentation for precision spraying
- Dice > 0.8: Accurate herbicide application
- Dice < 0.7: Waste herbicide or miss weeds
- **Impact**: Chemical costs, crop health

**Real-world scenario**: Brain tumor segmentation. Dice = 0.92 means radiation oncologist can use it with minor adjustments (5 min). Dice = 0.75 means 30 min manual correction. At 20 patients/day, that's 8 hours saved.

### 3. Mean IoU (mIoU)
- **Definition**: Average IoU across all classes
- **Use**: Standard for semantic segmentation

**Business Use Cases:**

**Autonomous driving**: Segment road, sidewalk, vehicles, pedestrians
- mIoU > 0.75: Production-ready
- mIoU < 0.65: Not safe enough
- **Impact**: Safety, regulatory approval

**Fashion e-commerce**: Segment clothing items for virtual try-on
- mIoU > 0.8: Realistic virtual try-on
- mIoU < 0.7: Poor user experience
- **Impact**: Conversion rate, return rate

**Real-world scenario**: Virtual try-on app. mIoU = 0.85 means accurate clothing segmentation, realistic overlay. Result: 15% higher conversion, 20% lower returns.

## Image Quality

### 1. PSNR (Peak Signal-to-Noise Ratio)
- **Range**: Higher is better (typically 20-50 dB)
- **Use**: Image reconstruction quality
- **Limitation**: Doesn't correlate well with human perception

**Business Use Cases:**

**Video streaming**: Compression quality assessment
- PSNR > 40 dB: Excellent quality, minimal compression artifacts
- PSNR < 30 dB: Noticeable quality loss
- **Impact**: User satisfaction, bandwidth costs
- **Tradeoff**: Higher PSNR = more bandwidth = higher costs

**Medical imaging**: Image enhancement/denoising
- PSNR > 35 dB: Diagnostic quality maintained
- PSNR < 30 dB: Details lost, not diagnostic
- **Impact**: Diagnostic accuracy

**Satellite imagery**: Image restoration
- PSNR > 38 dB: Usable for analysis
- PSNR < 32 dB: Too degraded
- **Impact**: Analysis accuracy

**Real-world scenario**: Video conferencing app. PSNR = 35 dB at 2 Mbps vs PSNR = 42 dB at 5 Mbps. Choose based on bandwidth availability and quality requirements.

### 2. SSIM (Structural Similarity Index)
- **Range**: -1 to 1 (1 is identical)
- **Use**: Perceptual image quality
- **Advantage**: Better matches human perception than PSNR

**Business Use Cases:**

**Photo editing apps**: Filter quality assessment
- SSIM > 0.95: Imperceptible changes
- SSIM < 0.85: Noticeable quality loss
- **Impact**: User satisfaction, app ratings

**E-commerce**: Product image compression
- SSIM > 0.9: Maintain product appearance
- SSIM < 0.8: Product looks different, returns increase
- **Impact**: Conversion rate, return rate

**Video games**: Texture compression
- SSIM > 0.92: High quality graphics
- SSIM < 0.85: Noticeable artifacts
- **Impact**: User experience, game reviews

**Real-world scenario**: E-commerce product images. SSIM = 0.95 with 70% compression vs SSIM = 0.85 with 85% compression. First option: Better quality, lower returns. Second: Faster loading, but more returns due to "looks different than photo".

## Decision Framework

**Object Detection:**
- Use IoU for single-class accuracy
- Use mAP for multi-class systems
- Use PR curves for threshold tuning

**Segmentation:**
- Use Dice for medical/critical applications (balanced metric)
- Use mIoU for multi-class segmentation
- Avoid pixel accuracy for imbalanced classes

**Image Quality:**
- Use PSNR for technical benchmarking
- Use SSIM for perceptual quality
- Consider both for compression optimization

## Industry-Specific Recommendations

**Healthcare**: Dice > 0.9, manual review for Dice < 0.85

**Autonomous Vehicles**: mAP > 0.8, mIoU > 0.75 for production

**Retail**: IoU > 0.6 for analytics, SSIM > 0.9 for product images

**Manufacturing**: IoU > 0.8 for defect detection, Dice > 0.85 for precise localization

**Media/Entertainment**: PSNR > 35 dB, SSIM > 0.9 for streaming quality

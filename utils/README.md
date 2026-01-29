# Evaluation Utilities

## Cross-Validation

### K-Fold Cross-Validation
- **Purpose**: Robust performance estimation
- **Method**: Split data into K folds, train on K-1, validate on 1
- **Advantage**: Uses all data for both training and validation
- **Typical K**: 5 or 10

**Business Use Cases:**

**Small datasets**: Medical trials, rare events
- **Problem**: Only 500 samples, single train/test split unreliable
- **Solution**: 5-fold CV gives 5 performance estimates, more reliable
- **Impact**: Confident model selection, avoid overfitting to test set

**Model selection**: Choose best algorithm/hyperparameters
- **Problem**: Which model is truly better?
- **Solution**: CV on multiple folds reduces selection bias
- **Impact**: Better model choice, improved production performance

**Performance estimation**: Report to stakeholders
- **Problem**: Single test score might be lucky/unlucky
- **Solution**: CV mean ± std gives confidence interval
- **Impact**: Realistic expectations, better planning

**Real-world scenario**: Predicting customer churn with 1000 customers. Single split: 85% accuracy. 5-fold CV: 82% ± 3%. Reveals model less reliable than thought. Adjust business expectations accordingly.

**When to use:**
- Dataset < 10,000 samples
- Model selection/comparison
- Need confidence intervals
- Reporting to stakeholders

**When NOT to use:**
- Very large datasets (computationally expensive)
- Time-series data (use time-based splits)
- Severe class imbalance (use stratified)

### Stratified K-Fold
- **Use**: Classification with imbalanced classes
- **Method**: Maintains class distribution in each fold
- **Advantage**: More reliable estimates for imbalanced data

**Business Use Cases:**

**Fraud detection**: 1% fraud rate
- **Problem**: Random split might have 0% fraud in some folds
- **Solution**: Stratified CV ensures each fold has ~1% fraud
- **Impact**: Reliable evaluation, avoid misleading results

**Rare disease diagnosis**: 5% disease prevalence
- **Problem**: Some folds might have no positive cases
- **Solution**: Stratified CV maintains 5% in each fold
- **Impact**: Valid performance estimates, safe deployment

**Customer churn**: 10% churn rate
- **Problem**: Unstratified CV gives high variance estimates
- **Solution**: Stratified CV reduces variance by 50%
- **Impact**: Confident model selection, better ROI

**Real-world scenario**: Credit card fraud (0.5% fraud rate). Regular CV: Fold 1 has 0.3% fraud, Fold 2 has 0.8% fraud. Results vary wildly. Stratified CV: All folds have ~0.5% fraud. Consistent, reliable results.

**Impact on business:**
- Regular CV: Model A scores 92-96% (high variance), Model B scores 94% (consistent)
- Choose Model B, but Model A might actually be better
- Stratified CV: Model A scores 95% ± 0.5%, Model B scores 94% ± 0.3%
- Correctly choose Model A, 1% better performance = $100K/year in fraud prevention

### Leave-One-Out (LOO)
- **Method**: K = N (number of samples)
- **Use**: Small datasets
- **Disadvantage**: Computationally expensive

**Business Use Cases:**

**Clinical trials**: 50 patients
- **Problem**: Too few samples for train/test split
- **Solution**: LOO uses 49 for training, 1 for testing, repeat 50 times
- **Impact**: Maximum data utilization, reliable estimates

**Rare equipment failure**: 30 failure cases
- **Problem**: Can't afford to "waste" data on test set
- **Solution**: LOO trains on 29 cases each time
- **Impact**: Best possible model with limited data

**When to use:**
- N < 100 samples
- Each sample is expensive/rare
- Computational cost acceptable

**When NOT to use:**
- N > 1000 (too slow)
- Time-series data
- When faster methods sufficient

**Real-world scenario**: Predicting rare machine failure with 40 examples. LOO gives most reliable estimate. Takes 2 hours to run, but worth it for $1M machine. Regular CV with 5 folds would be less reliable.

## Statistical Testing

### Paired t-test
- **Use**: Compare two models on same data
- **Null hypothesis**: No difference in performance
- **Interpretation**: p < 0.05 suggests significant difference

**Business Use Cases:**

**Model comparison**: Is new model really better?
- **Scenario**: Model A: 85%, Model B: 87%
- **Question**: Is 2% difference real or random?
- **Solution**: Paired t-test on CV folds
- **Result**: p = 0.03 → Model B significantly better, deploy it
- **Result**: p = 0.15 → No significant difference, keep simpler Model A

**A/B testing**: Production model comparison
- **Scenario**: New model seems 3% better
- **Question**: Worth the deployment cost?
- **Solution**: Statistical test confirms significance
- **Impact**: Confident deployment decision, avoid wasted effort

**Feature engineering**: Do new features help?
- **Scenario**: Added 10 features, accuracy 84% → 85%
- **Question**: Real improvement or noise?
- **Solution**: t-test shows p = 0.08 → not significant
- **Impact**: Don't add features, keep model simple

**Real-world scenario**: E-commerce recommendation system. Model A: 35% CTR, Model B: 37% CTR. Looks better, but t-test shows p = 0.12 (not significant). Difference likely due to random variation. Don't deploy Model B (saves 2 weeks of engineering work).

**Business impact example:**
- Deploying new model costs: $50K (engineering) + $10K/month (compute)
- Model B appears 2% better, but p = 0.20 (not significant)
- Don't deploy → Save $50K + avoid risk of no improvement
- Model C appears 3% better, p = 0.01 (significant)
- Deploy → 3% improvement = $500K/year revenue, worth $50K investment

### McNemar's Test
- **Use**: Compare classifiers on same test set
- **Method**: Tests on disagreements between models
- **Advantage**: Doesn't assume normal distribution

**Business Use Cases:**

**Binary classification**: Spam detection, fraud detection
- **Scenario**: Both models have 95% accuracy
- **Question**: Are they making same mistakes?
- **Solution**: McNemar's test on disagreements
- **Impact**: Choose model with better error pattern

**Medical diagnosis**: Disease detection
- **Scenario**: Model A and B both 90% accurate
- **Question**: Which is truly better?
- **Solution**: McNemar's test shows Model A significantly better (p = 0.02)
- **Impact**: Deploy Model A, better patient outcomes

**Real-world scenario**: Credit approval. Model A and B both approve 80% correctly. But Model A's errors are false rejections (annoyed customers), Model B's errors are false approvals (defaults). McNemar's test helps choose based on error type, not just accuracy.

### Wilcoxon Signed-Rank Test
- **Use**: Non-parametric alternative to t-test
- **When**: Data not normally distributed

**Business Use Cases:**

**Skewed metrics**: Revenue prediction (heavy-tailed distribution)
- **Problem**: t-test assumes normal distribution, invalid here
- **Solution**: Wilcoxon test doesn't assume normality
- **Impact**: Valid statistical conclusions

**Small samples**: Only 10 CV folds
- **Problem**: Can't verify normality with small sample
- **Solution**: Wilcoxon test is safer choice
- **Impact**: Robust conclusions

**Real-world scenario**: Predicting house prices (skewed distribution). t-test says no significant difference (p = 0.08), but Wilcoxon test says significant (p = 0.03). Wilcoxon is more appropriate for skewed data. Deploy new model.

## Bias-Variance Tradeoff

### High Bias (Underfitting)
- Simple model
- High training error
- High validation error

**Business Impact:**

**Missed opportunities**: Model too simple to capture patterns
- **Example**: Linear model for complex pricing
- **Result**: 30% error rate, poor decisions
- **Cost**: Lost revenue, competitive disadvantage

**Real-world scenario**: Retail demand forecasting with linear regression. Can't capture seasonality, promotions, trends. Prediction error = 25%. Result: $2M in excess inventory + $1M in stockouts. Solution: Use more complex model (random forest), error drops to 10%, saves $2M/year.

### High Variance (Overfitting)
- Complex model
- Low training error
- High validation error

**Business Impact:**

**Production failures**: Model works in testing, fails in production
- **Example**: Deep network memorizes training data
- **Result**: 95% training accuracy, 70% production accuracy
- **Cost**: Poor user experience, lost trust

**Real-world scenario**: Customer churn prediction. Complex model achieves 95% on historical data, but only 65% on new customers. Overfit to specific patterns. Result: Wrong retention offers, wasted marketing budget ($500K). Solution: Regularize model, 85% on both train and new data, better ROI.

### Optimal Model
- Balanced complexity
- Low training error
- Low validation error

**Business Value:**
- Reliable predictions
- Good generalization
- Confident deployment
- Positive ROI

**How to find:**
1. Start simple, increase complexity
2. Monitor train vs validation error
3. Stop when validation error stops improving
4. Use cross-validation for reliable estimates
5. Apply regularization if needed

**Real-world scenario**: Fraud detection. Simple model: 80% accuracy (underfitting). Complex model: 95% train, 82% test (overfitting). Optimal model: 88% train, 87% test (balanced). Deployed optimal model, catches 87% of fraud, saves $5M/year.

## Best Practices

### 1. Always use cross-validation for small datasets
**Why**: Single split unreliable
**When**: N < 10,000
**Impact**: Confident model selection
**ROI**: Avoid deploying wrong model (saves weeks of work)

### 2. Hold out test set separate from CV
**Why**: CV for model selection, test for final evaluation
**Method**: 60% train, 20% validation (CV), 20% test
**Impact**: Unbiased performance estimate
**ROI**: Realistic production expectations

### 3. Stratify for classification tasks
**Why**: Maintain class distribution
**When**: Imbalanced classes (< 30% minority class)
**Impact**: Reliable estimates
**ROI**: Correct model selection, better performance

### 4. Report confidence intervals (mean ± std)
**Why**: Single number misleading
**Example**: "85% ± 3%" vs "85%"
**Impact**: Realistic expectations
**ROI**: Better planning, avoid over-promising

### 5. Use statistical tests when comparing models
**Why**: Avoid deploying non-improvements
**When**: Models within 5% of each other
**Impact**: Confident decisions
**ROI**: Avoid wasted deployment effort ($50K+)

### 6. Consider computational cost vs reliability tradeoff
**Why**: More folds = more reliable but slower
**Guideline**: 
  - N < 100: Use LOO or 10-fold
  - N = 100-1000: Use 10-fold
  - N = 1000-10000: Use 5-fold
  - N > 10000: Use single train/val/test split
**Impact**: Efficient use of compute resources
**ROI**: Balance accuracy and speed

## Decision Framework

**Use K-Fold CV when:**
- Small to medium datasets (< 10K samples)
- Need robust performance estimates
- Comparing multiple models
- Reporting to stakeholders

**Use Stratified K-Fold when:**
- Classification with imbalanced classes
- Minority class < 30%
- Need consistent fold distributions

**Use LOO when:**
- Very small datasets (< 100 samples)
- Each sample is valuable
- Computational cost acceptable

**Use Statistical Tests when:**
- Comparing models within 5% performance
- Need confidence in decision
- Justifying deployment costs
- Reporting to executives

## Industry-Specific Recommendations

**Healthcare**: Use stratified CV (rare diseases), statistical tests (safety-critical)

**Finance**: Use time-series CV (temporal data), statistical tests (regulatory requirements)

**E-commerce**: Use stratified CV (imbalanced conversions), A/B tests in production

**Manufacturing**: Use LOO if few failure examples, CV for quality control

**Startups**: Use 5-fold CV (balance speed and reliability), focus on fast iteration

## ROI of Proper Evaluation

**Without proper evaluation:**
- Wrong model selection: 5-10% worse performance
- Overconfident estimates: Production surprises
- Wasted deployments: $50K-200K per failed deployment
- Lost opportunities: Missed better models

**With proper evaluation:**
- Correct model selection: Optimal performance
- Realistic estimates: Accurate planning
- Confident deployments: Fewer failures
- Better ROI: 10-30% improvement in business metrics

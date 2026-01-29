# Regression Metrics

## Overview
Regression metrics evaluate how well a model predicts continuous values.

## Key Metrics

### 1. Mean Squared Error (MSE)
- **Formula**: (1/n) × Σ(y_true - y_pred)²
- **Range**: 0 to ∞ (lower is better)
- **Use**: Penalizes large errors heavily
- **Unit**: Squared units of target variable

**Business Use Cases:**
- **Stock price prediction**: Large errors are disproportionately bad - missing by $50 is much worse than missing by $5
- **Demand forecasting**: Overestimating by 1000 units is catastrophic (excess inventory), worse than 10 errors of 100 units
- **Real estate pricing**: Being off by $100K on a house is much worse than being off by $10K

**Real-world scenario**: Inventory management - Overestimating demand by 500 units causes massive waste. MSE heavily penalizes this large error.

**When NOT to use:**
- When outliers exist (MSE will be dominated by them)
- When errors should be weighted equally regardless of magnitude

### 2. Root Mean Squared Error (RMSE)
- **Formula**: √MSE
- **Range**: 0 to ∞ (lower is better)
- **Use**: Same scale as target variable
- **Advantage**: More interpretable than MSE

**Business Use Cases:**
- **Sales forecasting**: "Our model is off by $5,000 on average" - easy to understand
- **Temperature prediction**: "Average error is 2°C" - interpretable for stakeholders
- **Delivery time estimation**: "Typically off by 15 minutes" - clear business metric
- **Energy consumption**: "Prediction error is 50 kWh" - actionable for planning

**Real-world scenario**: E-commerce delivery time - RMSE of 30 minutes means customers can expect predictions within ±30 min typically. Business can set expectations accordingly.

### 3. Mean Absolute Error (MAE)
- **Formula**: (1/n) × Σ|y_true - y_pred|
- **Range**: 0 to ∞ (lower is better)
- **Use**: Average absolute difference
- **Advantage**: Less sensitive to outliers than MSE

**Business Use Cases:**
- **Budget forecasting**: All errors cost equally - $10K over or under both matter the same
- **Attendance prediction**: Being off by 100 people has linear cost (catering, seating)
- **Taxi fare estimation**: Customers care about average error, not squared error
- **Manufacturing tolerances**: Parts off by 1mm are rejected same as parts off by 5mm

**Real-world scenario**: Restaurant daily customer prediction - Whether you're off by 20 or 50 customers, you adjust staff linearly. MAE gives true average error.

**When to use over RMSE:**
- Outliers are present but shouldn't dominate metric
- Linear cost of errors
- More robust evaluation needed

### 4. R² (Coefficient of Determination)
- **Formula**: 1 - (SS_res / SS_tot)
- **Range**: -∞ to 1 (1 is perfect, 0 is baseline)
- **Use**: Proportion of variance explained
- **Interpretation**: How well model fits data

**Business Use Cases:**
- **Model comparison**: "Model A explains 85% of variance vs Model B's 60%" - clear winner
- **Feature importance**: Adding new features increased R² from 0.7 to 0.9 - features are valuable
- **Marketing ROI**: R² = 0.8 means 80% of sales variance explained by marketing spend
- **Risk assessment**: R² = 0.95 means model captures most risk factors

**Real-world scenario**: Housing price model with R² = 0.85 means 85% of price variation is explained by features (location, size, etc.). Remaining 15% is other factors.

**Interpretation guide:**
- R² > 0.9: Excellent fit
- R² = 0.7-0.9: Good fit
- R² = 0.5-0.7: Moderate fit
- R² < 0.5: Poor fit
- R² < 0: Model worse than predicting mean

### 5. MAPE (Mean Absolute Percentage Error)
- **Formula**: (100/n) × Σ|((y_true - y_pred) / y_true)|
- **Range**: 0 to ∞ (lower is better)
- **Use**: Percentage-based error
- **Limitation**: Undefined when y_true = 0

**Business Use Cases:**
- **Sales forecasting**: "We're 5% off on average" - easy for executives to understand
- **Revenue prediction**: Percentage error matters more than absolute (5% of $1M vs $100K)
- **Growth rate estimation**: Relative error is what matters for planning
- **Cross-product comparison**: Compare forecast accuracy across products with different scales

**Real-world scenario**: Retail chain forecasting - MAPE = 8% means predictions are off by 8% on average. Works for both $100 and $10,000 products.

**When NOT to use:**
- Values near zero (MAPE explodes)
- Asymmetric cost (over-prediction vs under-prediction)
- When absolute error matters more than relative

## Decision Framework

**Choose MSE/RMSE when:**
- Large errors are disproportionately costly
- Outliers should be heavily penalized
- Optimization target (differentiable)

**Choose MAE when:**
- All errors weighted equally
- Outliers present but shouldn't dominate
- More robust metric needed
- Linear cost structure

**Choose R² when:**
- Comparing models on same dataset
- Understanding model fit quality
- Communicating to non-technical stakeholders

**Choose MAPE when:**
- Relative error matters more than absolute
- Comparing across different scales
- Stakeholders think in percentages
- No zero values in target

## Industry-Specific Examples

**Finance**: Use RMSE for price prediction (interpretable), R² for model comparison

**Supply Chain**: Use MAE for demand (linear costs), MAPE for cross-product comparison

**Energy**: Use RMSE for consumption (interpretable units), MSE for optimization

**Real Estate**: Use RMSE for pricing (dollar terms), R² for feature evaluation

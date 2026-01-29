# Forecasting Metrics

## Overview
Time series forecasting requires specialized metrics that account for temporal patterns, trends, and seasonality.

## Key Metrics

### 1. MASE (Mean Absolute Scaled Error)
- **Formula**: MAE / MAE_naive
- **Range**: 0 to ∞ (< 1 is better than naive forecast)
- **Use**: Scale-independent, works across different time series
- **Advantage**: Can compare forecasts across different datasets

**Business Use Cases:**

**Retail demand forecasting**: Compare products with different scales
- MASE < 1: Better than naive (seasonal) forecast
- MASE > 1: Worse than naive, model not useful
- **Impact**: Inventory optimization across product categories

**Energy consumption**: Compare buildings of different sizes
- MASE = 0.7: 30% better than naive forecast
- MASE = 1.2: Worse than naive, don't use model
- **Impact**: Energy savings, cost reduction

**Real-world scenario**: Forecasting sales for 1000 products (range $10 to $10,000). MAPE doesn't work well across scales. MASE allows fair comparison. Products with MASE < 0.8 get automated ordering, MASE > 1.2 need manual review.

**Why better than MAPE:**
- Works when values are zero or near-zero
- Scale-independent (compare across products)
- Interpretable (< 1 = beats baseline)

### 2. SMAPE (Symmetric MAPE)
- **Formula**: 100/n × Σ(|y_true - y_pred| / (|y_true| + |y_pred|))
- **Range**: 0 to 100% (lower is better)
- **Use**: Symmetric version of MAPE
- **Advantage**: Treats over/under-prediction equally

**Business Use Cases:**

**Supply chain**: Balanced cost of over/under-forecasting
- SMAPE < 10%: Excellent forecast, minimal waste
- SMAPE > 30%: Poor forecast, high costs
- **Impact**: Reduce inventory costs and stockouts

**Financial forecasting**: Revenue/expense prediction
- SMAPE < 15%: Reliable for budgeting
- SMAPE > 25%: Too uncertain for planning
- **Impact**: Better financial planning

**Real-world scenario**: Restaurant food ordering. Over-forecast = waste ($), under-forecast = lost sales ($). SMAPE treats both equally. SMAPE = 12% means reliable ordering, minimal waste.

**When to use over MAPE:**
- When over/under-prediction have similar costs
- When values can be small (MAPE explodes)
- When need symmetric error metric

### 3. Forecast Bias
- **Formula**: Mean(y_pred - y_true)
- **Range**: -∞ to +∞ (0 is unbiased)
- **Use**: Detect systematic over/under-forecasting
- **Interpretation**: Positive = over-forecast, Negative = under-forecast

**Business Use Cases:**

**Demand planning**: Detect systematic errors
- Bias = +50 units: Consistently over-forecasting, excess inventory
- Bias = -50 units: Consistently under-forecasting, stockouts
- **Impact**: Adjust forecasts, reduce costs

**Sales forecasting**: Quota setting
- Bias = +10%: Sales team consistently beats forecast (quotas too low)
- Bias = -10%: Sales team consistently misses (quotas too high)
- **Impact**: Fair quota setting, better motivation

**Budget forecasting**: Expense prediction
- Bias = +$10K/month: Over-budgeting, inefficient capital allocation
- Bias = -$10K/month: Under-budgeting, cash flow issues
- **Impact**: Accurate budgeting, better cash management

**Real-world scenario**: Manufacturing demand forecast has bias = +200 units/day. Consistently over-producing, $50K/month in excess inventory. Adjust model to remove bias, save $600K/year.

### 4. Tracking Signal
- **Formula**: Cumulative Error / MAD (Mean Absolute Deviation)
- **Range**: Typically -4 to +4 (outside = model drift)
- **Use**: Monitor forecast quality over time
- **Threshold**: |Tracking Signal| > 4 indicates model needs retraining

**Business Use Cases:**

**Production planning**: Detect when forecast degrades
- |TS| < 4: Forecast still reliable
- |TS| > 4: Model drifting, retrain needed
- **Impact**: Proactive model maintenance, avoid bad decisions

**Inventory management**: Monitor forecast accuracy
- TS trending up: Systematic under-forecasting developing
- TS trending down: Systematic over-forecasting developing
- **Impact**: Early warning system, adjust before major issues

**Real-world scenario**: Retail demand forecast. Tracking signal = 2.5 (good) in Q1. Rises to 5.2 in Q2 (alert!). Investigation reveals new competitor changed market. Retrain model with recent data. Prevents $200K in inventory issues.

### 5. Coverage (Prediction Intervals)
- **Definition**: % of actual values within prediction interval
- **Target**: 95% coverage for 95% prediction interval
- **Use**: Measure uncertainty quantification quality

**Business Use Cases:**

**Risk management**: Quantify forecast uncertainty
- 95% interval coverage = 94-96%: Well-calibrated
- 95% interval coverage = 70%: Under-estimating uncertainty, risky
- **Impact**: Better risk assessment, avoid surprises

**Capacity planning**: Plan for worst-case scenarios
- Upper bound of 95% interval: Plan capacity for this
- Lower bound: Minimum resource allocation
- **Impact**: Efficient resource allocation

**Financial planning**: Budget ranges
- Point forecast: $1M revenue
- 95% interval: $800K - $1.2M
- Coverage = 95%: Reliable uncertainty estimates
- **Impact**: Better contingency planning

**Real-world scenario**: Cloud infrastructure planning. Forecast traffic with 95% prediction interval. Coverage = 93% (good). Plan capacity for upper bound. Avoid outages while minimizing over-provisioning. Saves $100K/year vs fixed over-provisioning.

### 6. Directional Accuracy
- **Definition**: % of times forecast correctly predicts direction (up/down)
- **Range**: 0 to 100% (50% = random)
- **Use**: When direction matters more than magnitude

**Business Use Cases:**

**Stock trading**: Predict price direction
- Directional accuracy > 55%: Profitable trading strategy
- Directional accuracy < 52%: Not better than random
- **Impact**: Trading profitability

**Inventory decisions**: Will demand increase or decrease?
- Directional accuracy > 70%: Reliable for ordering decisions
- Directional accuracy < 60%: Too risky for automation
- **Impact**: Inventory optimization

**Marketing campaigns**: Will sales go up or down?
- Directional accuracy > 65%: Can plan campaigns confidently
- Directional accuracy < 55%: Need more data/better model
- **Impact**: Campaign ROI

**Real-world scenario**: Cryptocurrency trading bot. Magnitude predictions unreliable (high volatility), but directional accuracy = 58%. Enough for profitable trading. Focus on direction, not exact price.

### 7. Quantile Loss (Pinball Loss)
- **Formula**: For quantile τ: max(τ(y - ŷ), (τ-1)(y - ŷ))
- **Range**: 0 to ∞ (lower is better)
- **Use**: Asymmetric loss for different quantiles
- **Advantage**: Optimize for specific risk levels

**Business Use Cases:**

**Inventory optimization**: Asymmetric costs
- **Problem**: Stockout costs $50/unit, overstock costs $5/unit (10:1 ratio)
- **Solution**: Use 90th percentile forecast (τ=0.9), not median
- **Impact**: Minimize total cost, not just forecast error
- **ROI**: Optimizing for cost, not accuracy

**Real-world scenario**: 
- Median forecast (τ=0.5): 100 units, balanced errors
- 90th percentile (τ=0.9): 130 units, avoid costly stockouts
- Result: 5% more overstock cost, but 40% fewer stockouts
- **Net savings: $200K/year**

**Energy capacity planning**: Avoid blackouts
- **Problem**: Blackout costs $1M/hour, excess capacity costs $10K/hour (100:1 ratio)
- **Solution**: Use 95th percentile forecast (τ=0.95)
- **Impact**: Plan for high demand scenarios, avoid catastrophic costs

**Real-world scenario**: Power grid planning. 95th percentile forecast ensures capacity for peak demand. Costs 10% more in infrastructure, but avoids $10M/year in blackout costs.

**Cloud infrastructure**: Balance cost vs availability
- **Problem**: Downtime costs $100K/hour, over-provisioning costs $5K/hour
- **Solution**: Use 90th percentile (τ=0.9) for capacity
- **Impact**: 99.9% uptime, minimal over-provisioning

**Healthcare staffing**: Patient wait times vs labor costs
- **Problem**: Long waits lose patients ($), excess staff costs $
- **Solution**: Use 80th percentile (τ=0.8) for patient volume
- **Impact**: Acceptable wait times, controlled costs

**Real-world scenario**: Emergency room staffing. 50th percentile = frequent understaffing, long waits. 80th percentile = adequate staff 80% of time, acceptable wait times, controlled labor costs.

**Quantile Selection Guide:**
- **τ = 0.5 (median)**: Symmetric costs, minimize absolute error
- **τ = 0.7-0.8**: Moderate asymmetry, slight over-forecast preference
- **τ = 0.9-0.95**: High asymmetry, strongly avoid under-forecasting
- **τ = 0.99**: Extreme risk aversion, plan for worst-case

**Cost-based quantile selection:**
```
Optimal τ = Cost_underforecast / (Cost_underforecast + Cost_overforecast)

Example: Stockout=$50, Overstock=$5
τ = 50 / (50 + 5) = 0.91 → Use 91st percentile
```

**Why better than point forecasts:**
- Point forecast optimizes for accuracy, not business cost
- Quantile forecast optimizes for your specific cost structure
- Provides actionable decision thresholds

**Real-world impact**: Retailer switched from median forecast to cost-optimized quantile (τ=0.85). Same forecast accuracy, but 25% reduction in total inventory costs ($2M/year savings).

## Time Series Specific Considerations

### Seasonality
**Problem**: Standard metrics don't account for seasonal patterns
**Solution**: Use MASE (compares to seasonal naive forecast)

**Example**: Ice cream sales
- Summer: 1000 units, Winter: 200 units
- Naive forecast: Use last year's same month
- MASE compares your model to this seasonal baseline

### Trend
**Problem**: Trending data makes absolute errors misleading
**Solution**: Use percentage-based metrics (SMAPE, MAPE)

**Example**: Growing startup revenue
- Year 1: $100K, Year 2: $500K, Year 3: $2M
- $100K error in Year 1 = 100% error
- $100K error in Year 3 = 5% error
- SMAPE accounts for scale

### Multiple Horizons
**Problem**: Accuracy degrades with forecast horizon
**Solution**: Report metrics by horizon

**Example**: Demand forecasting
- 1-day ahead: MASE = 0.6 (excellent)
- 7-day ahead: MASE = 0.9 (good)
- 30-day ahead: MASE = 1.3 (poor)
- **Decision**: Use model for 1-7 days only

## Decision Framework

**Choose MASE when:**
- Comparing across different scales
- Need scale-independent metric
- Want to beat seasonal baseline

**Choose SMAPE when:**
- Over/under-prediction equally costly
- Values can be near zero
- Need symmetric metric

**Choose Forecast Bias when:**
- Detecting systematic errors
- Adjusting forecasts
- Understanding error direction

**Choose Tracking Signal when:**
- Monitoring model over time
- Detecting model drift
- Deciding when to retrain

**Choose Coverage when:**
- Uncertainty quantification matters
- Risk management critical
- Planning for ranges, not points

**Choose Directional Accuracy when:**
- Direction matters more than magnitude
- Trading/investment decisions
- Binary decisions (increase/decrease inventory)

**Choose Quantile Loss when:**
- Asymmetric costs (stockout vs overstock)
- Risk management (plan for worst-case)
- Optimizing business costs, not forecast accuracy
- Need specific percentile forecasts

## Industry-Specific Recommendations

**Retail**: MASE < 0.8, Bias near 0, Tracking Signal monitoring

**Finance**: SMAPE < 15%, Coverage = 95%, Directional accuracy > 55%

**Energy**: MASE < 0.9, Forecast bias < 5%, Prediction intervals

**Manufacturing**: MASE < 0.85, Tracking Signal < 4, Bias monitoring

**Supply Chain**: SMAPE < 12%, MASE < 0.8, Directional accuracy > 70%

## Common Pitfalls

**Don't use MAPE when:**
- Values can be zero (division by zero)
- Asymmetric costs (use SMAPE)
- Comparing across scales (use MASE)

**Don't ignore bias:**
- Low MAE but high bias = systematic error
- Adjust forecasts to remove bias
- Monitor with tracking signal

**Don't forget uncertainty:**
- Point forecasts alone insufficient
- Provide prediction intervals
- Measure coverage

**Don't use single metric:**
- Combine multiple metrics
- MASE + Bias + Coverage = complete picture
- Different metrics for different decisions

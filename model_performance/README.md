# Model Performance Metrics

## Overview
Evaluating computational efficiency and resource usage of ML models.

## Inference Metrics

### 1. Latency
- **Definition**: Time to process single input
- **Unit**: milliseconds (ms)
- **Important for**: Real-time applications
- **Variants**: 
  - Average latency
  - P50, P95, P99 percentiles

**Business Use Cases:**

**Real-time bidding (Ad tech)**: Bid decisions in <100ms
- Latency < 50ms: Competitive, can bid on most auctions
- Latency > 100ms: Miss 60% of auctions, lost revenue
- **Impact**: $10M/year revenue difference for large ad platform

**Autonomous vehicles**: Object detection for braking
- Latency < 50ms: Safe reaction time
- Latency > 100ms: Dangerous, can't brake in time
- **Impact**: Safety-critical, liability

**High-frequency trading**: Market prediction
- Latency < 1ms: Competitive advantage
- Latency > 10ms: Opportunities missed
- **Impact**: Millions in trading profits

**Mobile apps**: Image recognition, AR filters
- Latency < 100ms: Feels instant, good UX
- Latency > 500ms: Laggy, users abandon
- **Impact**: User retention, app ratings

**Voice assistants**: Speech recognition
- Latency < 200ms: Natural conversation
- Latency > 500ms: Awkward pauses, poor UX
- **Impact**: User satisfaction, adoption

**Real-world scenario**: E-commerce product search. Latency = 50ms means instant results, users browse more. Latency = 300ms means slow, 20% of users abandon search. At 1M searches/day, that's 200K lost opportunities.

**P95/P99 importance**: Average latency = 50ms looks good, but P99 = 2000ms means 1% of users have terrible experience. For 1M users, that's 10K frustrated users daily.

### 2. Throughput
- **Definition**: Samples processed per second
- **Unit**: samples/sec or QPS (queries per second)
- **Important for**: Batch processing, high-traffic services

**Business Use Cases:**

**Video streaming**: Content moderation
- Throughput > 1000 videos/hour: Can moderate all uploads
- Throughput < 500 videos/hour: Backlog grows, harmful content stays up
- **Impact**: Platform safety, regulatory compliance

**E-commerce**: Product recommendation
- Throughput > 10K QPS: Handle Black Friday traffic
- Throughput < 5K QPS: Site slows down, lost sales
- **Impact**: $100K-1M in lost sales during peak

**Financial services**: Fraud detection
- Throughput > 50K transactions/sec: Real-time fraud prevention
- Throughput < 10K transactions/sec: Batch processing, delayed detection
- **Impact**: Fraud losses, customer trust

**Medical imaging**: Radiology AI
- Throughput > 100 scans/hour: Keeps up with hospital workflow
- Throughput < 50 scans/hour: Bottleneck, radiologists wait
- **Impact**: Hospital efficiency, patient wait times

**Real-world scenario**: Social media content moderation. 10M posts/day = 116 posts/sec. Throughput = 200 posts/sec means real-time moderation. Throughput = 50 posts/sec means 4-hour delay, harmful content spreads.

**Cost impact**: Cloud inference at $0.10/1000 requests. 1B requests/month:
- High throughput (fewer instances): $100K/month
- Low throughput (more instances): $300K/month
- **Savings: $200K/month with optimized throughput**

### 3. FLOPs (Floating Point Operations)
- **Definition**: Number of mathematical operations
- **Use**: Model complexity comparison
- **Related**: MACs (Multiply-Accumulate operations)

**Business Use Cases:**

**Mobile deployment**: Battery life considerations
- FLOPs < 1B: Runs efficiently on mobile
- FLOPs > 10B: Drains battery, poor UX
- **Impact**: App usability, user retention

**Edge devices**: IoT, smart cameras
- FLOPs < 500M: Runs on edge hardware
- FLOPs > 2B: Requires cloud, latency + cost issues
- **Impact**: Deployment feasibility, operational costs

**Model selection**: Choose architecture
- Model A: 5B FLOPs, 92% accuracy
- Model B: 20B FLOPs, 93% accuracy
- **Decision**: Is 1% accuracy worth 4x compute?

**Real-world scenario**: Smart doorbell with person detection. 500M FLOPs model runs on device ($50 hardware). 5B FLOPs model needs cloud ($2/month/device). For 1M devices, that's $24M/year in cloud costs.

## Memory Metrics

### 1. Model Size
- **Components**:
  - Parameters count
  - Storage size (MB/GB)
- **Important for**: Edge devices, mobile deployment

**Business Use Cases:**

**Mobile apps**: App download size
- Model < 50MB: Acceptable download size
- Model > 200MB: Users won't download, especially on cellular
- **Impact**: App installs, user acquisition

**Edge deployment**: IoT devices
- Model < 10MB: Fits on cheap hardware ($20)
- Model > 100MB: Needs expensive hardware ($200)
- **Impact**: Hardware costs, deployment scale

**Over-the-air updates**: Update models remotely
- Model < 20MB: Quick updates, minimal data usage
- Model > 100MB: Slow updates, user complaints
- **Impact**: Update adoption, model freshness

**Real-world scenario**: Keyboard app with text prediction. 30MB model fits in app, users download. 200MB model requires separate download, 70% of users skip it. Result: Feature unused, wasted development.

**Cost impact**: Deploying to 10M devices:
- 10MB model: $0.01/device storage = $100K
- 100MB model: $0.10/device storage = $1M
- **Savings: $900K with smaller model**

### 2. Memory Usage
- **Peak memory**: Maximum RAM during inference
- **Important for**: Resource-constrained environments

**Business Use Cases:**

**Serverless deployment**: AWS Lambda, Cloud Functions
- Memory < 512MB: Cheap tier ($0.0000166667/GB-sec)
- Memory > 2GB: Expensive tier ($0.0000333334/GB-sec)
- **Impact**: 2x cost difference

**Mobile devices**: Background processing
- Memory < 100MB: Runs alongside other apps
- Memory > 500MB: OS kills app, poor UX
- **Impact**: App reliability, user experience

**Batch processing**: Process many samples simultaneously
- Memory efficient: Batch size 128, faster processing
- Memory hungry: Batch size 8, 16x slower
- **Impact**: Processing time, costs

**Real-world scenario**: Serverless image classification. 1B requests/month:
- 256MB memory: $50K/month
- 2GB memory: $400K/month
- **Savings: $350K/month with memory optimization**

### 3. Activation Memory
- **Definition**: Memory for intermediate outputs
- **Important for**: Training large models

**Business Use Cases:**
- **Training budget**: Determines max model size you can train
- **Batch size**: Affects training speed and convergence
- **Hardware selection**: Choose GPU based on memory needs

**Real-world scenario**: Training large model. 16GB GPU can train batch size 32. 80GB GPU can train batch size 256, converges 3x faster. GPU cost difference: $10K vs $30K. Faster training saves weeks of researcher time ($20K+). Worth the investment.

## Efficiency Metrics

### 1. Parameters Count
- **Definition**: Total trainable parameters
- **Use**: Model complexity indicator
- **Example**: GPT-3 has 175B parameters

**Business Use Cases:**

**Deployment feasibility**: Can we deploy this?
- < 100M params: Easy deployment anywhere
- 1B-10B params: Needs good hardware, manageable
- > 100B params: Requires specialized infrastructure
- **Impact**: Deployment costs, feasibility

**Training costs**: More parameters = more expensive training
- 100M params: $1K to train
- 1B params: $10K to train
- 10B params: $100K to train
- 100B params: $1M+ to train
- **Impact**: R&D budget, experimentation speed

**Inference costs**: More parameters = slower, more expensive
- 100M params: $0.001 per 1K requests
- 10B params: $0.10 per 1K requests
- **Impact**: Operating costs at scale

**Real-world scenario**: Startup choosing model size. 100M param model costs $50K/year to run. 1B param model costs $500K/year. Need to justify 10x cost with 10x revenue increase.

### 2. Inference Speed
- **CPU vs GPU**: Performance comparison
- **Batch size impact**: Throughput vs latency tradeoff

**Business Use Cases:**

**Hardware selection**: CPU vs GPU deployment
- CPU: $0.05/hour, 10 QPS
- GPU: $0.50/hour, 200 QPS
- **Decision**: GPU is 4x cheaper per request at scale

**Batch size optimization**: 
- Batch=1: 50ms latency, 20 QPS
- Batch=32: 200ms latency, 160 QPS
- **Decision**: Use batch=1 for real-time, batch=32 for batch processing

**Real-world scenario**: Image classification service. 1M requests/day:
- CPU: 100 instances × $0.05/hour × 24 hours = $120/day
- GPU: 5 instances × $0.50/hour × 24 hours = $60/day
- **Savings: $22K/year with GPU**

### 3. Energy Consumption
- **Important for**: Green AI, mobile devices
- **Unit**: Joules or Watt-hours

**Business Use Cases:**

**Mobile apps**: Battery life
- Low energy: App runs all day
- High energy: Battery drains in 2 hours, users uninstall
- **Impact**: User retention, app ratings

**Data center costs**: Electricity bills
- Efficient model: $10K/month electricity
- Inefficient model: $50K/month electricity
- **Impact**: Operating costs, carbon footprint

**Edge devices**: Solar-powered IoT
- Low energy: Runs on solar panel
- High energy: Needs battery replacement, maintenance costs
- **Impact**: Deployment feasibility, maintenance costs

**Real-world scenario**: Smart home device. Efficient model uses 0.5W, runs on small battery for months. Inefficient model uses 5W, needs frequent charging. Result: Poor user experience, product returns.

## Optimization Techniques

### 1. Quantization
- Reduce precision (FP32 → INT8)
- Trade-off: Size/speed vs accuracy

**Business Impact:**
- Model size: 4x smaller (FP32 → INT8)
- Inference speed: 2-4x faster
- Accuracy loss: 0.5-2%
- **ROI**: Usually worth it for deployment

**Real-world scenario**: Mobile app. FP32 model = 200MB, too large. INT8 model = 50MB, acceptable. Accuracy: 92% → 91%. Trade-off accepted.

### 2. Pruning
- Remove unnecessary weights
- Reduce model size and FLOPs

**Business Impact:**
- Model size: 30-50% reduction
- Speed: 20-40% faster
- Accuracy loss: 0-1%
- **ROI**: Free performance boost

**Real-world scenario**: Edge device. Pruned model runs 40% faster, fits on cheaper hardware. Saves $50/device × 100K devices = $5M.

### 3. Knowledge Distillation
- Train smaller model from larger one
- Maintain accuracy with fewer parameters

**Business Impact:**
- Model size: 10x smaller
- Speed: 5-10x faster
- Accuracy: 95-98% of teacher model
- **ROI**: Enables deployment where large model impossible

**Real-world scenario**: Large model (1B params) too slow for production. Distill to small model (100M params), 8x faster, 2% accuracy loss. Enables real-time deployment.

## Benchmarking Best Practices

### 1. Warm-up runs
**Why**: First runs include initialization overhead
**Impact**: Accurate latency measurement
**Example**: First run 500ms, subsequent runs 50ms. Report 50ms, not 500ms.

### 2. Multiple runs
**Why**: Variance in measurements
**Impact**: Reliable estimates
**Example**: Report mean ± std: "50ms ± 5ms" not just "50ms"

### 3. Consistent environment
**Why**: Fair comparison
**Impact**: Valid benchmarks
**Example**: Same GPU, batch size, input size for all models

### 4. Profile bottlenecks
**Why**: Identify optimization opportunities
**Impact**: Targeted improvements
**Example**: 80% time in one layer → optimize that layer first

### 5. Consider real-world conditions
**Why**: Lab performance ≠ production performance
**Impact**: Realistic expectations
**Example**: Add network latency, concurrent requests, cold starts

## Decision Framework

**Choose latency optimization when:**
- Real-time applications (< 100ms required)
- User-facing features (UX critical)
- Safety-critical systems

**Choose throughput optimization when:**
- Batch processing
- High-traffic services
- Cost optimization at scale

**Choose memory optimization when:**
- Mobile/edge deployment
- Serverless functions
- Resource-constrained environments

**Choose model size optimization when:**
- Mobile apps (download size)
- Edge devices (storage limited)
- Frequent updates (OTA)

## Industry-Specific Recommendations

**Mobile Apps**: Latency < 100ms, Model < 50MB, Memory < 100MB

**Autonomous Vehicles**: Latency < 50ms, High throughput, Safety-critical

**Cloud Services**: Optimize throughput for cost, P99 latency < 200ms

**Edge/IoT**: Model < 10MB, Memory < 50MB, Low energy

**Real-time Systems**: Latency < 50ms, Consistent P99, High reliability

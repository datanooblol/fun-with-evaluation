import numpy as np
import time
import matplotlib.pyplot as plt

def mock_inference(batch_size, delay=0.001):
    """Simulate model inference"""
    time.sleep(delay * batch_size)
    return np.random.rand(batch_size, 10)

print("=== Model Performance Evaluation ===\n")

# Latency measurement
print("--- Latency Analysis ---")
latencies = []
n_runs = 100

for _ in range(n_runs):
    start = time.time()
    _ = mock_inference(1, delay=0.0001)
    latencies.append((time.time() - start) * 1000)

print(f"Average Latency: {np.mean(latencies):.2f} ms")
print(f"P50 Latency:     {np.percentile(latencies, 50):.2f} ms")
print(f"P95 Latency:     {np.percentile(latencies, 95):.2f} ms")
print(f"P99 Latency:     {np.percentile(latencies, 99):.2f} ms\n")

# Throughput measurement
print("--- Throughput Analysis ---")
batch_sizes = [1, 8, 16, 32, 64]
throughputs = []

for bs in batch_sizes:
    start = time.time()
    for _ in range(10):
        _ = mock_inference(bs, delay=0.0001)
    elapsed = time.time() - start
    throughput = (10 * bs) / elapsed
    throughputs.append(throughput)
    print(f"Batch Size {bs:2d}: {throughput:.0f} samples/sec")

print()

# Model complexity
print("--- Model Complexity ---")
params = 1_234_567
model_size_mb = params * 4 / (1024 ** 2)  # FP32
flops = params * 2  # Simplified

print(f"Parameters:  {params:,}")
print(f"Model Size:  {model_size_mb:.2f} MB (FP32)")
print(f"FLOPs:       {flops:,}\n")

# Memory usage simulation
print("--- Memory Usage ---")
input_size = (1, 3, 224, 224)
input_memory = np.prod(input_size) * 4 / (1024 ** 2)
activation_memory = input_memory * 10  # Simplified

print(f"Input Memory:      {input_memory:.2f} MB")
print(f"Activation Memory: {activation_memory:.2f} MB")
print(f"Total Memory:      {input_memory + activation_memory + model_size_mb:.2f} MB\n")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(latencies, bins=30, edgecolor='black')
axes[0].axvline(np.mean(latencies), color='r', linestyle='--', label=f'Mean: {np.mean(latencies):.2f}ms')
axes[0].set_xlabel('Latency (ms)')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Latency Distribution')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(batch_sizes, throughputs, marker='o', linewidth=2)
axes[1].set_xlabel('Batch Size')
axes[1].set_ylabel('Throughput (samples/sec)')
axes[1].set_title('Throughput vs Batch Size')
axes[1].grid(True)

plt.tight_layout()
plt.savefig('model_performance/performance_metrics.png')
print("✓ Saved visualization to 'model_performance/performance_metrics.png'")

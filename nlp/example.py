import numpy as np
from collections import Counter

def bleu_score(reference, candidate, n=1):
    """Simplified BLEU score for n-grams"""
    ref_ngrams = [tuple(reference[i:i+n]) for i in range(len(reference)-n+1)]
    cand_ngrams = [tuple(candidate[i:i+n]) for i in range(len(candidate)-n+1)]
    
    ref_counts = Counter(ref_ngrams)
    cand_counts = Counter(cand_ngrams)
    
    matches = sum((cand_counts & ref_counts).values())
    total = len(cand_ngrams)
    
    return matches / total if total > 0 else 0

def rouge_n(reference, candidate, n=1):
    """ROUGE-N score"""
    ref_ngrams = [tuple(reference[i:i+n]) for i in range(len(reference)-n+1)]
    cand_ngrams = [tuple(candidate[i:i+n]) for i in range(len(candidate)-n+1)]
    
    ref_counts = Counter(ref_ngrams)
    cand_counts = Counter(cand_ngrams)
    
    matches = sum((cand_counts & ref_counts).values())
    total = len(ref_ngrams)
    
    return matches / total if total > 0 else 0

def perplexity(probabilities):
    """Calculate perplexity from token probabilities"""
    log_probs = np.log(probabilities)
    return np.exp(-np.mean(log_probs))

print("=== NLP Metrics ===\n")

# Machine Translation / Text Generation
print("--- BLEU Score (Machine Translation) ---")
reference = "the cat sat on the mat".split()
candidate = "the cat is on the mat".split()

bleu1 = bleu_score(reference, candidate, n=1)
bleu2 = bleu_score(reference, candidate, n=2)

print(f"Reference:  {' '.join(reference)}")
print(f"Candidate:  {' '.join(candidate)}")
print(f"BLEU-1: {bleu1:.3f}")
print(f"BLEU-2: {bleu2:.3f}\n")

# Summarization
print("--- ROUGE Score (Summarization) ---")
ref_summary = "machine learning is a subset of artificial intelligence".split()
gen_summary = "machine learning is part of artificial intelligence".split()

rouge1 = rouge_n(ref_summary, gen_summary, n=1)
rouge2 = rouge_n(ref_summary, gen_summary, n=2)

print(f"Reference:  {' '.join(ref_summary)}")
print(f"Generated:  {' '.join(gen_summary)}")
print(f"ROUGE-1: {rouge1:.3f}")
print(f"ROUGE-2: {rouge2:.3f}\n")

# Language Model
print("--- Perplexity (Language Model) ---")
np.random.seed(42)
token_probs = np.random.rand(100) * 0.5 + 0.3
ppl = perplexity(token_probs)

print(f"Perplexity: {ppl:.2f}")
print("Lower perplexity = better language model\n")

# Word Embeddings
print("--- Embedding Quality ---")
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

king = np.random.rand(50)
queen = king + np.random.randn(50) * 0.1
man = np.random.rand(50)

sim_king_queen = cosine_similarity(king, queen)
sim_king_man = cosine_similarity(king, man)

print(f"Similarity(king, queen): {sim_king_queen:.3f}")
print(f"Similarity(king, man):   {sim_king_man:.3f}")
print("Higher similarity = more related words")

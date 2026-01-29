# NLP Metrics

## Overview
Metrics for evaluating natural language processing tasks.

## Machine Translation

### 1. BLEU (Bilingual Evaluation Understudy)
- **Range**: 0 to 1 (higher is better)
- **Use**: Machine translation quality
- **Method**: N-gram precision with brevity penalty
- **Variants**: BLEU-1, BLEU-2, BLEU-4
- **Limitation**: Doesn't consider semantics

**Business Use Cases:**

**E-commerce internationalization**: Translate product descriptions
- BLEU > 0.5: Acceptable for product listings
- BLEU < 0.3: Requires human post-editing
- **Impact**: Time-to-market for new regions, translation costs
- **Cost**: Human translation $0.10-0.30/word, MT + editing $0.03-0.08/word

**Customer support**: Translate support tickets/responses
- BLEU > 0.4: Can use with human review
- BLEU < 0.3: Too many errors, customer frustration
- **Impact**: Support costs, customer satisfaction

**Content localization**: Translate marketing materials
- BLEU > 0.6: Good starting point for human refinement
- BLEU < 0.4: Faster to translate from scratch
- **Impact**: Localization costs, brand consistency

**Real-world scenario**: Translating 10,000 product descriptions to 5 languages. BLEU = 0.55 means 80% cost reduction vs full human translation. BLEU = 0.25 means only 30% savings due to extensive editing needed.

**When NOT to use:**
- Legal/medical documents (semantics critical)
- Creative content (multiple valid translations)
- When one reference translation (BLEU needs multiple references for accuracy)

### 2. METEOR
- **Advantage**: Considers synonyms and stemming
- **Use**: Better correlation with human judgment than BLEU

**Business Use Cases:**

**High-stakes translation**: Legal, medical, financial documents
- METEOR > 0.6: Acceptable with expert review
- METEOR < 0.5: Too risky, use human translation
- **Impact**: Legal compliance, patient safety

**Marketing content**: Brand voice matters
- METEOR > 0.65: Captures meaning and style
- METEOR < 0.5: Loses brand voice
- **Impact**: Brand perception, marketing effectiveness

**Real-world scenario**: Pharmaceutical company translating drug information. METEOR = 0.7 means synonyms handled well ("medicine" vs "medication"). Safe for expert review. METEOR = 0.4 means too literal, missing context.

## Summarization

### 1. ROUGE (Recall-Oriented Understudy for Gisting Evaluation)
- **ROUGE-N**: N-gram overlap
- **ROUGE-L**: Longest common subsequence
- **ROUGE-S**: Skip-bigram overlap
- **Use**: Automatic summarization evaluation

**Business Use Cases:**

**News aggregation**: Auto-summarize articles
- ROUGE-L > 0.5: Readable, informative summaries
- ROUGE-L < 0.3: Missing key information
- **Impact**: User engagement, time-on-site

**Legal document review**: Summarize contracts, cases
- ROUGE-2 > 0.4: Captures key terms and clauses
- ROUGE-2 < 0.3: Misses critical details
- **Impact**: Review efficiency, legal risk
- **Cost**: Lawyer time $300-800/hour, good summaries save hours

**Customer feedback analysis**: Summarize reviews
- ROUGE-1 > 0.45: Captures main sentiments
- ROUGE-1 < 0.35: Misses important feedback
- **Impact**: Product decisions, customer insights

**Meeting notes**: Auto-generate meeting summaries
- ROUGE-L > 0.4: Captures action items and decisions
- ROUGE-L < 0.3: Attendees must re-listen to recording
- **Impact**: Productivity, follow-through on decisions

**Real-world scenario**: Legal firm summarizing 100-page contracts. ROUGE-2 = 0.45 means lawyers can review summary (30 min) instead of full document (3 hours). At $500/hour, saves $1,250 per contract.

## Language Models

### 1. Perplexity
- **Formula**: exp(-1/N × Σ log P(w_i))
- **Range**: 1 to ∞ (lower is better)
- **Use**: How well model predicts text
- **Interpretation**: Average branching factor

**Business Use Cases:**

**Chatbots**: Measure response quality
- Perplexity < 50: Natural, coherent responses
- Perplexity > 100: Awkward, unnatural language
- **Impact**: User satisfaction, task completion rate

**Auto-complete**: Predictive text quality
- Perplexity < 30: Accurate predictions, fast typing
- Perplexity > 80: Poor predictions, user frustration
- **Impact**: User experience, typing efficiency

**Content generation**: Blog posts, product descriptions
- Perplexity < 40: Fluent, readable content
- Perplexity > 70: Requires heavy editing
- **Impact**: Content production costs, quality

**Code completion**: IDE auto-complete
- Perplexity < 20: Accurate code suggestions
- Perplexity > 50: Irrelevant suggestions
- **Impact**: Developer productivity

**Real-world scenario**: Customer service chatbot. Perplexity = 35 means natural conversations, 80% issue resolution without human. Perplexity = 90 means awkward responses, 40% escalation to human agents.

**Interpretation guide:**
- Perplexity < 30: Excellent (GPT-level)
- Perplexity 30-60: Good (usable for production)
- Perplexity 60-100: Moderate (needs improvement)
- Perplexity > 100: Poor (not production-ready)

### 2. Cross-Entropy Loss
- **Related**: log(perplexity)
- **Use**: Training objective for language models

**Business Use Cases:**
- **Model comparison**: Lower loss = better model
- **Training monitoring**: Ensure convergence
- **Resource allocation**: Decide when to stop training

## Word Embeddings

### 1. Cosine Similarity
- **Range**: -1 to 1 (1 = identical direction)
- **Use**: Semantic similarity between words
- **Application**: Word analogies, similarity tasks

**Business Use Cases:**

**Search engines**: Find semantically similar queries
- Similarity > 0.8: Highly related, can show same results
- Similarity < 0.5: Different intent, different results
- **Impact**: Search relevance, user satisfaction

**Recommendation systems**: Find similar products/content
- Similarity > 0.7: Good recommendations
- Similarity < 0.5: Irrelevant recommendations
- **Impact**: Click-through rate, conversion

**Duplicate detection**: Find duplicate support tickets
- Similarity > 0.85: Likely duplicate
- Similarity < 0.7: Different issues
- **Impact**: Support efficiency, response time

**Resume screening**: Match job descriptions to resumes
- Similarity > 0.75: Good candidate match
- Similarity < 0.6: Poor fit
- **Impact**: Hiring efficiency, candidate quality

**Real-world scenario**: E-commerce search. User searches "laptop", system finds "notebook computer" (similarity = 0.85) and shows relevant results. Without good embeddings, misses 40% of relevant products.

### 2. Intrinsic Evaluation
- **Word Similarity**: Correlation with human judgments
- **Word Analogies**: king - man + woman ≈ queen

**Business Use Cases:**
- **Embedding quality check**: Before deploying in production
- **Model selection**: Choose best embedding model
- **Domain adaptation**: Verify embeddings work for your domain

### 3. Extrinsic Evaluation
- Performance on downstream tasks
- More reliable than intrinsic metrics

**Business Use Cases:**
- **ROI measurement**: Does better embedding improve business metrics?
- **A/B testing**: Compare embedding models in production
- **Budget justification**: Prove value of better embeddings

**Real-world scenario**: Upgrading embeddings improves search click-through rate from 35% to 42%. That's 20% more engagement, directly measurable business impact.

## Classification Tasks

### 1. Accuracy, F1, Precision, Recall
- Standard classification metrics
- Use for sentiment analysis, NER, etc.

**Business Use Cases:**

**Sentiment analysis**: Analyze customer reviews
- F1 > 0.8: Reliable for business decisions
- F1 < 0.7: Too many errors, manual review needed
- **Impact**: Product decisions, customer insights

**Named Entity Recognition**: Extract entities from documents
- Precision > 0.9: Few false extractions, clean data
- Recall > 0.85: Captures most entities
- **Impact**: Data quality, downstream task performance

**Spam detection**: Filter spam messages
- Precision > 0.95: Few false positives (important messages not lost)
- Recall > 0.90: Most spam caught
- **Impact**: User experience, inbox quality

### 2. Exact Match (EM)
- **Use**: Question answering
- **Definition**: Percentage of exact matches

**Business Use Cases:**

**Customer support bots**: Answer factual questions
- EM > 0.7: Can handle most queries
- EM < 0.5: Too many wrong answers, user frustration
- **Impact**: Support costs, customer satisfaction

**Document search**: Find exact information
- EM > 0.8: Reliable for critical information retrieval
- EM < 0.6: Users must verify answers
- **Impact**: User trust, task efficiency

**Real-world scenario**: HR chatbot answering policy questions. EM = 0.75 means 75% of answers exactly correct. Reduces HR inquiries by 60%. EM = 0.45 means too many wrong answers, employees lose trust.

### 3. F1 (Token-level)
- **Use**: Question answering, NER
- **Method**: Token overlap between prediction and ground truth

**Business Use Cases:**

**Information extraction**: Extract key facts from documents
- F1 > 0.85: Reliable extraction, minimal manual correction
- F1 < 0.7: Extensive manual review needed
- **Impact**: Processing costs, data quality

**Real-world scenario**: Insurance claims processing. Extract policy numbers, dates, amounts. F1 = 0.88 means 90% automation. F1 = 0.65 means only 50% automation, still need heavy manual review.

## Decision Framework

**Machine Translation:**
- Use BLEU for quick evaluation, multiple references
- Use METEOR for better semantic evaluation
- Always include human evaluation for production

**Summarization:**
- Use ROUGE-L for overall quality
- Use ROUGE-2 for key phrase capture
- Combine with human evaluation

**Language Models:**
- Use perplexity for model comparison
- Lower perplexity generally means better quality
- Validate with downstream task performance

**Embeddings:**
- Use intrinsic metrics for quick checks
- Use extrinsic metrics for business decisions
- Measure impact on actual business metrics

## Industry-Specific Recommendations

**E-commerce**: BLEU > 0.5 for product descriptions, Cosine similarity > 0.7 for recommendations

**Customer Support**: Perplexity < 50 for chatbots, EM > 0.7 for FAQ bots

**Legal/Medical**: METEOR > 0.6 for translation, F1 > 0.9 for entity extraction

**Content Creation**: Perplexity < 40 for generation, ROUGE-L > 0.5 for summarization

**Search/Recommendations**: Cosine similarity > 0.7 for relevance, F1 > 0.8 for classification

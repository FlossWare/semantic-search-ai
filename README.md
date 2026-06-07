# Semantic Search AI

**Advanced semantic search toolkit for AI applications**

Production-grade search enhancements that work with ANY search backend.

## Features

✅ **Hybrid Search**
- Combine semantic + keyword search
- Reciprocal Rank Fusion (RRF) algorithm
- Configurable weights (semantic vs keyword)

✅ **Reranking**
- Two-stage retrieval (bi-encoder → cross-encoder)
- Cross-encoder for precision
- Fast candidates → accurate top results

✅ **Advanced Filtering**
- MongoDB-style query operators
- Comparison: `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`
- Logical: `$and`, `$or`, `$not`
- Array: `$in`, `$nin`
- String: `$regex`, `$glob`

✅ **Backend Agnostic**
- Works with ANY search system
- Elasticsearch, Solr, vector databases
- Pure algorithmic enhancements

## Quick Start

### Hybrid Search

```python
from semantic_search_ai import HybridSearch

# Create hybrid searcher
hybrid = HybridSearch(semantic_weight=0.7, keyword_weight=0.3)

# Merge semantic + keyword results
results = hybrid.merge_results(
    semantic_results=vector_search_results,
    keyword_results=text_search_results,
    top_k=10
)
```

### Reranking

```python
from semantic_search_ai import Reranker

# Create reranker
reranker = Reranker()

# Two-stage retrieval
candidates = vector_db.search(query, top_k=100)  # Fast: get many candidates
top_results = reranker.rerank(query, candidates, top_k=5)  # Accurate: rerank to top 5
```

### Advanced Filtering

```python
from semantic_search_ai import AdvancedFilter

# Complex filters with MongoDB operators
filtered = AdvancedFilter.filter_results(results, {
    '$and': [
        {'confidence': {'$gte': 0.8}},
        {'source': {'$glob': '*.pdf'}},
        {'date': {'$gte': '2024-01-01'}}
    ]
})
```

## Real-World Pipeline

```python
from semantic_search_ai import HybridSearch, Reranker, AdvancedFilter

# 1. Hybrid search (semantic + keyword)
semantic = vector_db.search(embed(query), top_k=100)
keyword = text_search(query, top_k=100)
hybrid = HybridSearch().merge_results(semantic, keyword, top_k=50)

# 2. Advanced filtering
filtered = AdvancedFilter.filter_results(hybrid, {
    '$and': [
        {'confidence': {'$gte': 0.8}},
        {'content_type': {'$in': ['documentation', 'code']}}
    ]
})

# 3. Reranking for precision
reranker = Reranker()
final_results = reranker.rerank(query, filtered, top_k=5)
```

## Algorithms

### Reciprocal Rank Fusion (RRF)

Merges ranked lists from different sources:

```
score = 1 / (k + rank)
```

Where `k=60` (standard constant), `rank` is position in result list.

### Cross-Encoder Reranking

Two-stage retrieval:
1. **Bi-encoder** (fast): Encode query and docs separately, cosine similarity
2. **Cross-encoder** (accurate): Encode query+doc together, predict relevance

### MongoDB-Style Filtering

Industry-standard query operators for flexible filtering.

## Installation

```bash
pip install semantic-search-ai
```

## Use Cases

✅ RAG applications - Better retrieval quality  
✅ Search engines - Hybrid semantic + keyword  
✅ Document search - Advanced filtering  
✅ Code search - Reranking for precision  
✅ Knowledge bases - Production-grade search  

## Part of FlossWare AI

- **vectordb-ai** - Vector database adapter
- **semantic-search-ai** - Search enhancements (this project)
- **consensus-ai** - Multi-AI orchestration
- **knowledge-ai** - Knowledge ingestion
- **universal-ai** - AI platform

## License

GPL-3.0 - FlossWare (sfloess)


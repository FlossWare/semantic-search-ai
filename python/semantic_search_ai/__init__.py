"""
Semantic Search AI - Advanced semantic search toolkit

Production-grade search enhancements for AI applications.
"""

__version__ = "0.3"
__author__ = "FlossWare (sfloess)"
__license__ = "GPL-3.0"

from semantic_search_ai.hybrid import HybridSearch, SearchResult
from semantic_search_ai.reranker import Reranker, rerank
from semantic_search_ai.filters import AdvancedFilter, apply_filter

__all__ = [
    "HybridSearch",
    "SearchResult",
    "Reranker",
    "rerank",
    "AdvancedFilter",
    "apply_filter",
]

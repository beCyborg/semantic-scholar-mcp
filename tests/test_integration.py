"""Integration tests using real Semantic Scholar API.

These tests hit the actual API and verify end-to-end functionality.
Run with: uv run pytest tests/test_integration.py -v -m integration
"""

import pytest
import pytest_asyncio

from semantic_scholar_mcp.client import SemanticScholarClient
from semantic_scholar_mcp.paper_tracker import PaperTracker, get_tracker
from semantic_scholar_mcp.tools._common import set_client_getter
from semantic_scholar_mcp.tools.papers import get_paper_details, search_papers

# Mark all tests in this module as integration tests
pytestmark = pytest.mark.integration


@pytest_asyncio.fixture
async def real_client():
    """Create a real client for integration tests."""
    client = SemanticScholarClient()
    set_client_getter(lambda: client)
    yield client
    await client.close()


@pytest.fixture(autouse=True)
def reset_tracker_integration():
    """Reset tracker between integration tests."""
    PaperTracker.reset_instance()
    yield
    PaperTracker.reset_instance()


class TestSearchIntegration:
    """Integration tests for paper search."""

    @pytest.mark.asyncio
    async def test_search_real_papers(self, real_client: SemanticScholarClient) -> None:
        """Test searching for a known paper returns results."""
        result = await search_papers("attention is all you need", limit=5)

        assert isinstance(result, list)
        assert len(result) > 0
        assert any("attention" in p.title.lower() for p in result)

    @pytest.mark.asyncio
    async def test_search_with_year_filter(self, real_client: SemanticScholarClient) -> None:
        """Test search with year filter."""
        result = await search_papers(
            "transformer neural network",
            year="2020-2024",
            limit=5,
        )

        assert isinstance(result, list)
        if result:  # May be empty for very specific queries
            assert all(2020 <= (p.year or 0) <= 2024 for p in result)


class TestPaperDetailsIntegration:
    """Integration tests for paper details."""

    @pytest.mark.asyncio
    async def test_get_known_paper(self, real_client: SemanticScholarClient) -> None:
        """Test fetching a known paper by ID."""
        # "Attention Is All You Need" paper ID
        paper_id = "204e3073870fae3d05bcbc2f6a8e263d9b72e776"
        result = await get_paper_details(paper_id)

        assert not isinstance(result, str)  # Not an error message
        assert "attention" in result.title.lower()

    @pytest.mark.asyncio
    async def test_get_paper_by_doi(self, real_client: SemanticScholarClient) -> None:
        """Test fetching paper by DOI."""
        result = await get_paper_details("DOI:10.48550/arXiv.1706.03762")

        # May return paper or "not found" message
        if not isinstance(result, str):
            assert result.title is not None


class TestWorkflowIntegration:
    """Integration tests for complete workflows."""

    @pytest.mark.asyncio
    async def test_search_track_workflow(self, real_client: SemanticScholarClient) -> None:
        """Test searching papers and tracking them."""
        # Search for papers
        result = await search_papers("BERT language model", limit=3)

        assert isinstance(result, list)
        assert len(result) > 0

        # Check papers are tracked
        tracker = get_tracker()
        tracked = tracker.get_all_papers()

        assert len(tracked) == len(result)
        assert all(p.paperId in [t.paperId for t in tracked] for p in result)

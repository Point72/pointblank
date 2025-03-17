from __future__ import annotations
import pytest

from pointblank.compare import Compare
import polars.testing.parametric as pt
from hypothesis import given


@pytest.mark.skip
@given(
    dfa=pt.dataframes(min_size=100, max_size=1_000, allow_null=False),
    dfb=pt.dataframes(min_size=100, max_size=1_000, allow_null=False),
)
def test_compare_basic(dfa, dfb) -> None:
    comp = Compare(dfa, dfb)

    comp.compare()

    raise NotImplementedError


if __name__ == "__main__":
    pytest.main([__file__])

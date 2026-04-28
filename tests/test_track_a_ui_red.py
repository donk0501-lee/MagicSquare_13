"""
Track A — Boundary(UI) RED.

계약: docs/MagicSquare_4x4_TDD.md §8.1 (U-01~U-07, 성공 시 int[6]·좌표 1-index).
GREEN 전: magic_square.boundary 미구현 → import 실패 또는 미충족 assert.
"""

from __future__ import annotations

import importlib
import re

import pytest

from tests.prd_constants import (
    EXPECTED_M1_INT6,
    M1,
    MSG_BLANK_COUNT_INVALID,
    MSG_DUPLICATE_NONZERO,
    MSG_SIZE_INVALID,
    MSG_VALUE_OUT_OF_RANGE,
)


def _boundary():
    """GREEN에서 `magic_square.boundary` 모듈을 채우면 로드된다."""
    return importlib.import_module("magic_square.boundary")


def test_U01_given_non_4x4_rows_when_solve_then_size_invalid_message() -> None:
    """Given: 행 수가 4가 아님. When: 경계 진입. Then: SIZE_INVALID 고정 문구."""
    mod = _boundary()
    bad = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    with pytest.raises(Exception, match=re.escape(MSG_SIZE_INVALID)):
        mod.solve_two_blank_4x4(bad)


def test_U02_given_row_length_not_4_when_solve_then_size_invalid_message() -> None:
    """Given: 4행이나 한 행 길이≠4. When: 경계 진입. Then: SIZE_INVALID 동일 문구."""
    mod = _boundary()
    bad = [
        [1, 2, 3, 4],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
    ]
    with pytest.raises(Exception, match=re.escape(MSG_SIZE_INVALID)):
        mod.solve_two_blank_4x4(bad)


def test_U03_given_single_blank_when_solve_then_blank_count_invalid_message() -> None:
    """Given: 0이 1개. When: 경계 진입. Then: BLANK_COUNT_INVALID 고정 문구."""
    mod = _boundary()
    g = [row[:] for row in M1]
    z = sum(row.count(0) for row in g)
    assert z == 2
    # 한 칸만 0으로 줄이기: (0,1)을 3으로 채움 → 0 한 개
    g[0][1] = 3
    assert sum(row.count(0) for row in g) == 1
    with pytest.raises(Exception, match=re.escape(MSG_BLANK_COUNT_INVALID)):
        mod.solve_two_blank_4x4(g)


def test_U04_given_three_blanks_when_solve_then_blank_count_invalid_message() -> None:
    """Given: 0이 3개. When: 경계 진입. Then: BLANK_COUNT_INVALID 동일."""
    mod = _boundary()
    g = [row[:] for row in M1]
    g[0][0] = 0
    assert sum(row.count(0) for row in g) == 3
    with pytest.raises(Exception, match=re.escape(MSG_BLANK_COUNT_INVALID)):
        mod.solve_two_blank_4x4(g)


def test_U05_given_value_17_when_solve_then_value_out_of_range_message() -> None:
    """Given: 17 포함(빈칸 2·중복 없음). When: 경계 진입. Then: VALUE_OUT_OF_RANGE 고정 문구."""
    mod = _boundary()
    g = [row[:] for row in M1]
    g[3][3] = 17
    assert sum(row.count(0) for row in g) == 2
    with pytest.raises(Exception, match=re.escape(MSG_VALUE_OUT_OF_RANGE)):
        mod.solve_two_blank_4x4(g)


def test_U06_given_value_negative_when_solve_then_value_out_of_range_message() -> None:
    """Given: -1 포함, 빈칸 2 유지. When: 경계 진입. Then: VALUE_OUT_OF_RANGE 동일."""
    mod = _boundary()
    g = [row[:] for row in M1]
    g[2][0] = -1
    assert sum(row.count(0) for row in g) == 2
    with pytest.raises(Exception, match=re.escape(MSG_VALUE_OUT_OF_RANGE)):
        mod.solve_two_blank_4x4(g)


def test_U07_given_duplicate_nonzero_when_solve_then_duplicate_message() -> None:
    """Given: 비0 중복, 빈칸 2 유지. When: 경계 진입. Then: DUPLICATE_NONZERO 고정 문구."""
    mod = _boundary()
    g = [row[:] for row in M1]
    g[2][1] = 10
    assert sum(row.count(0) for row in g) == 2
    with pytest.raises(Exception, match=re.escape(MSG_DUPLICATE_NONZERO)):
        mod.solve_two_blank_4x4(g)


def test_U08_given_valid_M1_when_solve_then_length_six() -> None:
    """Given: FR-01 만족(M1). When: 경계 성공 경로. Then: 반환 길이 6 (I6/출력 계약)."""
    mod = _boundary()
    out = mod.solve_two_blank_4x4([row[:] for row in M1])
    assert len(out) == 6
    assert out == EXPECTED_M1_INT6


def test_U09_given_valid_M1_when_solve_then_coords_are_one_indexed() -> None:
    """Given: M1. When: 성공 반환. Then: r1,c1,r2,c2 ∈ [1,4] (BR-06)."""
    mod = _boundary()
    out = mod.solve_two_blank_4x4([row[:] for row in M1])
    r1, c1, _n1, r2, c2, _n2 = out
    for v in (r1, c1, r2, c2):
        assert 1 <= v <= 4

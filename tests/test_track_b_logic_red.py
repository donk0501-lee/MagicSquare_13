"""
Track B — Logic(domain) RED.

계약: 사용자 지정 API — find_blank_coords, find_not_exist_nums, is_magic_square, solution.
전제: FR-01 통과 격자는 별도 검증 레이어에서 보장; 본 테스트는 도메인 단위 계약 고정.

GREEN 전: magic_square.logic 미구현 → import 실패 또는 assert 실패.
"""

from __future__ import annotations

import importlib

import pytest

from tests.prd_constants import (
    EXPECTED_M1_INT6,
    EXPECTED_M2_INT6,
    M1,
    M1_FILLED_MAGIC,
    M1_NONMAGIC_ANTI_DIAG_SWAP,
    M1_NONMAGIC_COL_SWAP,
    M1_NONMAGIC_MAIN_DIAG_SWAP,
    M1_NONMAGIC_ROW_SWAP,
    M2,
    M_UNSOLVABLE,
)


def _logic():
    return importlib.import_module("magic_square.logic")


# --- find_blank_coords: row-major 두 빈칸, 1-index ---


def test_L_blank_coords_M1_row_major_two_pairs_one_indexed() -> None:
    """Invariant: BR-05, BR-06 — 첫/둘째 0의 (r,c)가 행 우선 스캔 순서·1-index."""
    logic = _logic()
    pairs = logic.find_blank_coords([row[:] for row in M1])
    assert pairs == [(1, 2), (2, 1)]


def test_L_blank_coords_M2_row_major_two_pairs_one_indexed() -> None:
    logic = _logic()
    pairs = logic.find_blank_coords([row[:] for row in M2])
    assert pairs == [(3, 4), (4, 4)]


# --- find_not_exist_nums: 누락 2개, 오름차순 ---


def test_L_missing_nums_M1_sorted_pair() -> None:
    """Invariant: BR-09 / FR-03 — {3,5} 오름차순."""
    logic = _logic()
    assert logic.find_not_exist_nums([row[:] for row in M1]) == [3, 5]


def test_L_missing_nums_M2_sorted_pair() -> None:
    """Invariant: M2 누락 {1,6}."""
    logic = _logic()
    assert logic.find_not_exist_nums([row[:] for row in M2]) == [1, 6]


# --- is_magic_square: 행·열·대각 모두 34 ---


def test_L_is_magic_true_on_M1_filled() -> None:
    """Invariant: I6, I7, BR-08 — 완성·비0 격자에서 True."""
    logic = _logic()
    assert logic.is_magic_square([row[:] for row in M1_FILLED_MAGIC]) is True


def test_L_is_magic_false_when_one_row_sum_broken() -> None:
    """Invariant: 한 행 합≠34이면 False (순열 유지 스왑)."""
    logic = _logic()
    assert logic.is_magic_square([row[:] for row in M1_NONMAGIC_ROW_SWAP]) is False


def test_L_is_magic_false_when_one_col_sum_broken() -> None:
    """Invariant: 한 열 합≠34이면 False."""
    logic = _logic()
    assert logic.is_magic_square([row[:] for row in M1_NONMAGIC_COL_SWAP]) is False


def test_L_is_magic_false_when_main_diagonal_broken() -> None:
    """Invariant: 주대각 합≠34이면 False."""
    logic = _logic()
    assert logic.is_magic_square([row[:] for row in M1_NONMAGIC_MAIN_DIAG_SWAP]) is False


def test_L_is_magic_false_when_anti_diagonal_broken() -> None:
    """Invariant: 부대각 합≠34이면 False."""
    logic = _logic()
    assert logic.is_magic_square([row[:] for row in M1_NONMAGIC_ANTI_DIAG_SWAP]) is False


# --- solution: 시도1→시도2, int[6], 1-index ---


def test_L_solution_M1_small_first_blank_then_int6_golden() -> None:
    """Invariant: BR-10, BR-14 — 시도1 성공 시 (n1,n2)=(n_small,n_large), 골든 일치."""
    logic = _logic()
    assert logic.solution([row[:] for row in M1]) == EXPECTED_M1_INT6


def test_L_solution_M2_reverse_order_golden() -> None:
    """Invariant: BR-11 — 시도1 실패·시도2 성공 시 (n1,n2)=(n_large,n_small)."""
    logic = _logic()
    assert logic.solution([row[:] for row in M2]) == EXPECTED_M2_INT6


def test_L_solution_returns_length_six_and_one_indexed_coords() -> None:
    """Invariant: 출력 길이 6, 좌표 1~4."""
    logic = _logic()
    out = logic.solution([row[:] for row in M1])
    assert len(out) == 6
    r1, c1, n1, r2, c2, n2 = out
    for x in (r1, c1, r2, c2):
        assert 1 <= x <= 4
    assert 1 <= n1 <= 16 and 1 <= n2 <= 16 and n1 != n2


def test_L_solution_T05_both_placements_fail_raises_not_magic() -> None:
    """Invariant: BR-13 — 두 시도 모두 비마방진이면 해 없음(도메인 예외)."""
    logic = _logic()
    NotMagic = getattr(logic, "NotMagicError", None)
    if NotMagic is None:
        pytest.fail("RED: logic.NotMagicError 타입을 GREEN에서 정의할 것 (도메인 NOT_MAGIC).")
    with pytest.raises(NotMagic):
        logic.solution([row[:] for row in M_UNSOLVABLE])

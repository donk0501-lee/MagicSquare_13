"""pytest — Track B 도메인 RED 스켈레톤(본문 미구현, GREEN 전 항상 실패).

상세 계약 테스트: test_track_b_logic_red.py
"""

from __future__ import annotations

import pytest


class TestLogicRedContractSkeleton:
    """magic_square.logic — find_blank_coords, find_not_exist_nums, is_magic_square, solution."""

    def test_l_find_blank_coords_m1_row_major(self) -> None:
        pytest.fail("RED")

    def test_l_find_blank_coords_m2_row_major(self) -> None:
        pytest.fail("RED")

    def test_l_find_not_exist_nums_m1_sorted(self) -> None:
        pytest.fail("RED")

    def test_l_find_not_exist_nums_m2_sorted(self) -> None:
        pytest.fail("RED")

    def test_l_is_magic_square_true_complete_grid(self) -> None:
        pytest.fail("RED")

    def test_l_is_magic_square_false_row_broken(self) -> None:
        pytest.fail("RED")

    def test_l_is_magic_square_false_col_broken(self) -> None:
        pytest.fail("RED")

    def test_l_is_magic_square_false_main_diagonal_broken(self) -> None:
        pytest.fail("RED")

    def test_l_is_magic_square_false_anti_diagonal_broken(self) -> None:
        pytest.fail("RED")

    def test_l_solution_m1_small_first_then_golden_int6(self) -> None:
        pytest.fail("RED")

    def test_l_solution_m2_reverse_then_golden_int6(self) -> None:
        pytest.fail("RED")

    def test_l_solution_result_length_six_one_indexed_coords(self) -> None:
        pytest.fail("RED")

    def test_l_solution_t05_both_placements_not_magic_raises(self) -> None:
        pytest.fail("RED")

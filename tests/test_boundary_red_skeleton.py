"""pytest — Track A 경계 계약 RED 스켈레톤(본문 미구현, GREEN 전 항상 실패).

상세 계약 테스트: test_track_a_ui_red.py
"""

from __future__ import annotations

import pytest


class TestBoundaryRedContractSkeleton:
    """PRD §8.1 U-01~U-09 — magic_square.boundary (예: solve_two_blank_4x4)."""

    def test_u01_non_4x4_rows_size_invalid(self) -> None:
        pytest.fail("RED")

    def test_u02_row_length_not_4_size_invalid(self) -> None:
        pytest.fail("RED")

    def test_u03_single_blank_blank_count_invalid(self) -> None:
        pytest.fail("RED")

    def test_u04_three_blanks_blank_count_invalid(self) -> None:
        pytest.fail("RED")

    def test_u05_value_17_out_of_range(self) -> None:
        pytest.fail("RED")

    def test_u06_value_negative_out_of_range(self) -> None:
        pytest.fail("RED")

    def test_u07_duplicate_nonzero(self) -> None:
        pytest.fail("RED")

    def test_u08_valid_input_result_length_six(self) -> None:
        pytest.fail("RED")

    def test_u09_valid_input_coords_one_indexed(self) -> None:
        pytest.fail("RED")

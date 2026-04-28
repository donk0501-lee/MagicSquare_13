"""경계(원시 입력·출력·오류 매핑) — GREEN 단계적 구현 (PRD §11 I1 우선)."""

from __future__ import annotations

from magic_square.errors import MagicSquareContractError

_SIZE_CODE = "SIZE_INVALID"
_SIZE_MSG = "Matrix must be 4x4."


def _raise_size_invalid() -> None:
    raise MagicSquareContractError(_SIZE_CODE, _SIZE_MSG)


def _validate_matrix_is_4x4(matrix: list[list[int]]) -> None:
    """I1: 바깥 길이 4, 각 행 길이 4 (U-01, U-02, FTC-MS-D-003·D-006)."""
    if len(matrix) != 4:
        _raise_size_invalid()
    for row in matrix:
        if len(row) != 4:
            _raise_size_invalid()


def solve_two_blank_magic_square(matrix: list[list[int]]) -> list[int]:
    """I1~I4 검증 후 도메인 해결; 성공 시 int[6], 실패 시 MagicSquareContractError."""
    _validate_matrix_is_4x4(matrix)
    raise NotImplementedError("GREEN: Track A - solve_two_blank_magic_square")

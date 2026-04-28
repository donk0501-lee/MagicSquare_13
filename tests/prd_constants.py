"""PRD §8.1 / §9.1 고정 문자열·골든 격자 (RED 테스트 전용, 도메인 구현 없음)."""

# §8.1 Track A — 기대 message (바이트 단위 고정)
MSG_SIZE_INVALID = "Matrix must be 4x4."
MSG_BLANK_COUNT_INVALID = "Exactly two cells must be 0."
MSG_VALUE_OUT_OF_RANGE = "Each cell must be 0 or between 1 and 16 inclusive."
MSG_DUPLICATE_NONZERO = "Non-zero values must be unique."
MSG_NOT_MAGIC_SQUARE = "No valid placement completes a 4x4 magic square."

# §9.1 M1 — 시도 1(작은 수→첫 빈칸) 성공
M1: list[list[int]] = [
    [16, 0, 2, 13],
    [0, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]
EXPECTED_M1_INT6: list[int] = [1, 2, 3, 2, 1, 5]

# §9.1 M2 — 역배치만 성공
M2: list[list[int]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 0, 12],
    [4, 14, 15, 0],
]
EXPECTED_M2_INT6: list[int] = [3, 3, 6, 4, 4, 1]

# T-05: FR-01 만족·두 빈칸 배치 모두 비마방진 (행 합으로 즉시 불가)
M_UNSOLVABLE: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 0, 12],
    [13, 14, 15, 0],
]

# FR-04 AC: M1 완성(0 없음) — 마방진 True
M1_FILLED_MAGIC: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]


def _swap_cells(g: list[list[int]], a: tuple[int, int], b: tuple[int, int]) -> list[list[int]]:
    out = [row[:] for row in g]
    r1, c1 = a
    r2, c2 = b
    out[r1][c1], out[r2][c2] = out[r2][c2], out[r1][c1]
    return out


# 완성·1~16 순열 유지, 합 34는 깨짐 (FR-04 False 분기용)
M1_NONMAGIC_ROW_SWAP = _swap_cells(M1_FILLED_MAGIC, (0, 1), (1, 0))
M1_NONMAGIC_COL_SWAP = _swap_cells(M1_FILLED_MAGIC, (0, 2), (2, 0))
M1_NONMAGIC_MAIN_DIAG_SWAP = _swap_cells(M1_FILLED_MAGIC, (0, 0), (1, 1))
M1_NONMAGIC_ANTI_DIAG_SWAP = _swap_cells(M1_FILLED_MAGIC, (0, 3), (3, 0))

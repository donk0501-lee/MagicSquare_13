# To-do list creation references
_Exported on 4/28/2026 at 11:45:21 GMT+9 from Cursor (3.2.11)_

---

**User**

Ｔｏ－Ｄｏ　리스트를 작성하고 싶습니다. 작성한 문서 중 무엇을 참조해서 만들어야 할까요?


---

**Cursor**

문서들의 목적과 내용을 확인해 To-Do 리스트 작성에 어떤 것을 참조하면 좋은지 정리합니다.



To-Do를 **무엇을 위한 리스트인지**에 따라 참조 문서를 나누는 것이 좋습니다.

## 1. 우선 참고: **`Report/4. UserJourney_Backlog_Report.md`**

문서 목적이 *Epic → User Journey → User Stories → Gherkin → 검증 체크리스트*로 명시되어 있어, **백로그·스프린트 단위 작업 목록**을 만들 때 가장 직접적인 근거입니다. 이미 스토리·시나리오·체크리스트 구조가 있으면 그걸 그대로 To-Do로 쪼개면 됩니다.

## 2. 요구·범위를 맞출 때: **`docs/PRD_MagicSquare_4x4_TDD.md`**

PRD 본문에서도 `Report/4`를 **축**으로 두고 `1, 2, 3`번 리포트와 `.cursorrules`를 근거로 한다고 적혀 있습니다. **FR 번호, AC, In/Out of scope**로 To-Do를 검증·누락 방지할 때 쓰면 좋습니다.

## 3. 기술 작업 쪼개기: **`Report/2. LayeredDesign_TDD_Report.md`**

도메인 컴포넌트·입출력 계약·테스트 설계가 정리되어 있어, **어떤 클래스/경계부터 테스트할지** 같은 구현 단위 To-Do를 만들 때 참조합니다. `Report/4`에서도 세부 설계는 이 리포트를 보라고 안내합니다.

## 4. “왜 이 순서인지”·불변조건 정렬: **`Report/1. ProblemDefinition_Report.md`**

문제 정의·Invariant·훈련 목표용이라, **우선순위·스코프 논의**나 Epic 수준 정렬에는 유용하고, 일일 코딩 To-Do의 세부 항목보다는 상위 맥락에 가깝습니다.

## 5. 도구·프로세스 To-Do: **`Report/3. CursorRules_WorkReport.md`**

Cursor 규칙·워크플로와 관련된 **작업 방식·규칙 준수** 항목을 넣을 때만 참조하면 됩니다.

---

**정리:**  
- **기능·스토리·검증 중심 To-Do** → `4. UserJourney_Backlog_Report.md` + 필요 시 `PRD`  
- **구현·테스트·레이어별 To-Do** → `2. LayeredDesign_TDD_Report.md` + PRD의 FR/AC  
- **목표·불변조건과의 정합** → `1. ProblemDefinition_Report.md`  
- **에디터/에이전트 규칙 관련** → `3. CursorRules_WorkReport.md`

---

**User**


당신은 시니어 소프트웨어 아키텍트이자 TDD 코치입니다. 할 일 목록의 항목과 완료 조건은 docs/5.PRD_MagicSquare_4x4_TDD.md를 주 소스로 두고, 스토리 단위 분해는 Report/4, 계약·오류 세부는 Report/2, 품질·TDD·ECB 준수는 Report/3와 Cursor 규칙을 참조해, 

다음 방법론을 적용하여
"Magic Square 4x4 완성 시스템"의 구현용 To-Do 구조를 작성하세요.

적용 방법론:
- Concept-to-Code Traceability
- Dual-Track UI + Logic TDD
- To-Do → Scenario → Test → Code 구조
- ECB(Entity / Control / Boundary) 모델
- RED → GREEN → REFACTOR

반드시 한국어로 작성하세요.

[시스템 목표]
부분적으로 비어 있는 4x4 Magic Square를 완성하는 시스템의 개발 To-Do를 작성합니다.

[도메인 규칙]
- 보드는 4x4이다.
- 숫자는 1~16만 사용한다.
- 0은 빈칸이다.
- 정확히 2칸이 비어 있다.
- 0을 제외한 중복 숫자는 허용되지 않는다.
- 모든 행, 열, 대각선의 합은 34여야 한다.
- 해결 가능한 경우 빈칸 값을 찾아 채운다.
- 유효하지 않은 보드는 거부한다.

[출력 형식]
다음 구조를 반드시 지켜서 작성하세요.

1. Epic
2. User Story
3. Phase별 Task 목록
4. 각 Task에는 반드시 아래 정보를 포함하세요.
   - Task ID
   - RED / GREEN / REFACTOR 여부
   - 작업 제목
   - Scenario Level (L0/L1/L2/L3)
   - 연결되는 Test 이름
   - 연결되는 Code 대상
   - ECB 스테레오타입 (Entity / Control / Boundary)
   - 필요 시 체크포인트

[표현 스타일]
- Markdown 사용
- 체크박스 형식 사용
- 실제 Cursor.AI 실습용 개발 보드처럼 작성
- 식별자는 Epic-001, US-001, TASK-001 형식 사용
- 유효한 케이스와 실패 케이스를 모두 포함
- 최소한 다음 작업을 포함
  - 보드 생성
  - 보드 유효성 검사
  - 빈칸 탐지
  - 후보값 필터링
  - 완성 로직
  - 잘못된 입력 처리
  - 테스트 커버리지 체크포인트

[Scenario Level 정의]
- L0: 기능 개요
- L1: 정상 흐름
- L2: 경계 상황
- L3: 실패 상황

[추가 제약]
- Logic 책임은 명확히 분리할 것
- UI/Boundary에는 비즈니스 규칙을 넣지 말 것
- Control은 검증과 해결 흐름을 조율할 것
- Entity는 보드 상태를 표현할 것
- 모든 To-Do는 Scenario, Test, Code로 추적 가능해야 함

이제
"Magic Square 4x4 완성 시스템"의 To-Do 구조를 생성하세요.

---

**Cursor**

PRD와 Report 2·3·4를 읽어 식별자·계약·컴포넌트 이름을 정확히 맞춥니다.



참고: 저장소에는 `docs/5.PRD_MagicSquare_4x4_TDD.md`가 없고, 동일 본문은 `docs/PRD_MagicSquare_4x4_TDD.md`에 있습니다. 아래 To-Do는 해당 PRD와 `Report/2`·`Report/3`·`.cursorrules`에 맞춰 작성했습니다.

---

# Magic Square 4×4 완성 시스템 — 구현용 To-Do 보드

**주 소스:** `docs/PRD_MagicSquare_4x4_TDD.md`  
**스토리 분해:** `Report/4. UserJourney_Backlog_Report.md`  
**계약·오류:** `Report/2. LayeredDesign_TDD_Report.md`  
**품질·TDD·ECB:** `Report/3. CursorRules_WorkReport.md`, 저장소 루트 `.cursorrules`

**방법론:** Concept→Code 추적, Dual-Track(Boundary + Domain), To-Do→Scenario→Test→Code, ECB, RED→GREEN→REFACTOR

---

## 1. Epic

- [ ] **Epic-001 — 불변조건·계약 기반 4×4 두 빈칸 마방진 완성**  
  - **완료 조건(PRDD 기준):** FR-01~FR-05 및 BR-01~BR-14 충족; §8 Dual-Track 최소 계약(U-01~U-09)·도메인 단위 테스트·§9.1 골든 M1/M2·T-05 실패 케이스 통과; §12 추적표와 컴포넌트·테스트 ID 대응 유지; NFR-01(도메인 ≥95%)·NFR-02(경계 ≥85%)·NFR-04(입력 배열 비변조) 달성.

---

## 2. User Story

- [ ] **US-001 (경계)** — 학습자로서, **원시 `int[][]`가 I1~I4를 위반하면** 고정 `code`·`message`로 거절되길 원한다. *(FR-01, PRD §8.1 U-01~U-07, Report/2 Error schema)*  
- [ ] **US-002 (도메인)** — 학습자로서, **FR-01을 통과한 퍼즐에 대해** row-major 두 빈칸·누락 두 수·두 조합 시도 후 **`int[6]` 또는 `NOT_MAGIC`**으로 결정되길 원한다. *(FR-02~FR-05, BR-05~BR-14)*  
- [ ] **US-003 (통합·품질)** — 학습자로서, **Boundary가 도메인 결과를 스키마에 맞게 노출**하고, 커버리지·결정론·매직 넘버 금지·ECB 의존 방향이 유지되길 원한다. *(NFR-01~NFR-05, Report/3, `.cursorrules`)*

---

## 3. Phase별 Task 목록

### Phase 0 — 추적·스캐폴딩 (Concept → Test 자리 확보)

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-001 | **RED** | 저장소에 `pytest` 실패용 최소 테스트 파일 추가(모듈 미존재) | L0 | `test_project_scaffold_imports` | `tests/conftest.py`, 패키지 진입점 초안 | Boundary·Control·Entity 경로만 명시 | RED 로그에 의도적 실패 1건 이상 |
| [ ] | TASK-002 | **GREEN** | ECB 권장 트리에 맞춘 패키지·빈 구현 스텁(테스트 통과용 pass 제외 금지 — 최소 시그니처) | L0 | `test_package_layout_matches_cursorrules` | `src/.../boundary`, `control`, `entity`, `domain` 등 | — | `.cursorrules` `file_structure`와 불일치 0 |
| [ ] | TASK-003 | **REFACTOR** | PRD §12 한 페이지짜리 **Traceability 스프레드시트/표**에 Task→FR→Test ID 링크 | L0 | (문서 검수용 체크리스트) | `docs/` 또는 `Report/` 내 추적 문서 1곳 | — | Epic-001의 각 FR에 Test·Component 열이 채워짐 |

---

### Phase 1 — Entity: 보드·스펙 (규칙 상수 단일화)

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-004 | **RED** | 4×4·매직 상수 34·검사 선 정의가 단일 출처에서 읽히는지 실패하는 테스트 | L1 | `test_magic_square_spec_magic_constant_34` | `MagicSquareSpec`(또는 동등) | **Entity** | NFR-05 위반 패턴(산재 리터럴) 없이 RED |
| [ ] | TASK-005 | **GREEN** | `magicConstantFor4x4()` / 스펙 객체로 상수·크기 노출 | L1 | 위 동일 | `entity/magic_square_spec.py` 등 | **Entity** | GREEN |
| [ ] | TASK-006 | **REFACTOR** | `PuzzleGrid` 등 값 객체로 4×4 스냅샷 복사 생성(불변 전제는 점진 도입) | L2 | `test_puzzle_grid_copy_is_detached_from_raw_array` | `PuzzleGrid` | **Entity** | NFR-04: 원본 `int[][]` 변조 테스트와 연계 준비 |

---

### Phase 2 — Dual-Track kickoff: Domain FR-01 RED + Boundary 계약 RED

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-007 | **RED** | `validatePuzzleInput` — 비4×4·빈칸 개수·범위·중복 실패 케이스 | L3 | `test_validate_puzzle_input_D06_through_D11` | `PuzzleInputInvariantChecker.validate_puzzle_input` | **Entity**/Domain Service | Report/2 D-06~D-11 대응 |
| [ ] | TASK-008 | **RED** | Boundary — `SIZE_INVALID` 고정 문구(U-01, U-02) | L3 | `test_boundary_U01_U02_size_invalid_message_exact` | `PuzzleBoundary.solve` 또는 동등 API | **Boundary** | PRD §8.1 바이트 동일 |
| [ ] | TASK-009 | **RED** | Boundary — `BLANK_COUNT_INVALID`, `VALUE_OUT_OF_RANGE`, `DUPLICATE_NONZERO` (U-03~U-07) | L3 | `test_boundary_U03_through_U07` | **Boundary** | **Boundary** | 도메인은 Mock/Stub |

---

### Phase 3 — Track B GREEN: 보드 유효성 검사 (FR-01 / I1~I4)

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-010 | **GREEN** | `validatePuzzleInput` I1~I4 및 **탐지 순서** SIZE→BLANK→RANGE→DUPLICATE (PRD §11) | L2~L3 | `test_validate_detection_order_single_violation` | `PuzzleInputInvariantChecker` | Domain(**Entity** 전제 데이터만 다룸) | FR-01 AC 전항목 |
| [ ] | TASK-011 | **REFACTOR** | 검증 결과 타입(`ValidationFailure` 등) 정리, 비즈니스 문구는 Boundary에만 | L2 | `test_domain_error_types_have_no_user_strings` | Domain 모듈 | Domain | Boundary에 도메인 규칙 문자열 없음 |

---

### Phase 4 — Track A GREEN: 잘못된 입력 처리 (Boundary 전용)

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-012 | **GREEN** | Boundary에서 I1~I4 위반을 §8.1 `code`/`message`로 매핑 | L3 | `test_boundary_maps_domain_invalid_to_schema` | `boundary/puzzle_gateway.py` 등 | **Boundary** | FR-01, U-01~U-07 GREEN |
| [ ] | TASK-013 | **REFACTOR** | 예상 밖 예외 → `INTERNAL_ERROR` / `Unexpected error.` 래핑(단, 계약 테스트 경로 유발 금지) | L3 | `test_boundary_internal_error_wrapper_optional` | **Boundary** | **Boundary** | PRD §8.1 실패 정책 |

---

### Phase 5 — 빈칸 탐지 (FR-02)

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-014 | **RED** | row-major 첫/둘째 0의 1-index 좌표 — M1, M2 기대 | L1 | `test_locate_two_blanks_M1_M2_D17` | `EmptyCellLocator.locate_two_blanks` | Domain | FR-02 AC |
| [ ] | TASK-015 | **GREEN** | `locateTwoBlanks` 구현 | L1 | 위 + `test_locate_two_blanks_returns_cell_index_vo` | `EmptyCellLocator`, `CellIndex` | **Entity** | BR-05, BR-06 |

---

### Phase 6 — 후보값(누락 두 수) 산출 (FR-03)

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-016 | **RED** | M1 {3,5}, M2 {1,6}, `n_small`/`n_large` 고정 | L1 | `test_find_missing_two_numbers_M1_M2` | `MissingNumberFinder.find_missing_two_numbers` | Domain + **`MissingNumberPair`(Entity)** | FR-03 AC |
| [ ] | TASK-017 | **GREEN** | 0 제외 1~16 multiset 기반 누락 계산 | L2 | `test_find_missing_two_numbers_sorted_pair` | `MissingNumberFinder` | **Entity** | BR-09 |

---

### Phase 7 — 완성 격자 마방진 판정 (FR-04) — “후보 배치” 검증의 핵심

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-018 | **RED** | `isMagicSquareComplete` — 완성 마방진 true, 행/열/주·부대각 각각 깨진 케이스 false | L1~L3 | `test_is_magic_square_complete_D13_through_D16` | `MagicCompletenessChecker.is_magic_square_complete` | Domain | FR-04 AC, I6/I7 |
| [ ] | TASK-019 | **GREEN** | 10선 합 `M=34` 판정 구현 | L1 | `test_is_magic_square_complete_true_on_valid_completion` | `MagicCompletenessChecker`, `MagicSquareSpec` | **Entity** | 0 포함 입력 호출 금지(전제는 테스트에서) |

---

### Phase 8 — 완성 로직: 두 조합 시도 + `int[6]` (FR-05, BR-10~14)

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-020 | **RED** | M1→`[1,2,3,2,1,5]`, M2→`[3,3,6,4,4,1]` 원소 단위 동일 | L1 | `test_T01_T02_golden_outputs` | `TwoBlankSolutionResolver.resolve` | Domain | T-01, T-02 |
| [ ] | TASK-021 | **GREEN** | 시도1 성공 시 시도2 미실행(BR-12), 복사 격자에서만 배치 | L2 | `test_resolve_skips_second_attempt_when_first_succeeds` | `TwoBlankSolutionResolver` | Domain | NFR-03, NFR-04 |
| [ ] | TASK-022 | **RED** | 두 시도 모두 실패 시 도메인 `NOT_MAGIC` | L3 | `test_T05_not_magic_domain_error` | `TwoBlankSolutionResolver` | Domain | T-05, D-12 |
| [ ] | TASK-023 | **GREEN** | `NOT_MAGIC` 반환 및 경계 매핑 준비 | L3 | `test_boundary_U09_maps_not_magic_to_NOT_MAGIC_SQUARE` | Boundary 매퍼 | **Boundary** | PRD §8.1 U-09 문구 |

---

### Phase 9 — Control: 검증·해결 흐름 조율 (비즈니스 규칙 없음)

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-024 | **RED** | Control이 “검증→빈칸→누락→해결” 순서만 호출하는지 실패 테스트(순서/미호출) | L0 | `test_solve_use_case_invocation_order` | `SolveTwoBlankPuzzleUseCase`(가칭) | **Control** | 도메인 서비스에 규칙 중복 없음 |
| [ ] | TASK-025 | **GREEN** | Control 구현 + Boundary에서 Control 주입 | L1 | `test_end_to_end_domain_path_through_control` | `control/solve_puzzle.py` | **Control** | PRD §10.3 의존 방향 |
| [ ] | TASK-026 | **REFACTOR** | 포트 인터페이스로 Boundary 테스트 더블(U-08) 용이화 | L1 | `test_boundary_U08_with_domain_port_double` | Port + Fake | **Control**/Boundary | U-08 |

---

### Phase 10 — Track A 완성: 성공 경로·골든 회귀

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-027 | **GREEN** | 실제 도메인 연결 후 M1/M2 E2E(경계 진입) | L1 | `test_boundary_real_domain_M1_M2` | Boundary→Control→Domain | **Boundary** | §9.1 변경 금지 정책 준수 |
| [ ] | TASK-028 | **GREEN** | `int[6]` 스키마 검증(길이 6, 좌표 1~4) — 성공 시에만 | L2 | `test_boundary_success_output_schema` | **Boundary** | **Boundary** | Report/2 Output schema |

---

### Phase 11 — 속성·비변조·커버리지 체크포인트

| 완료 | Task ID | 단계 | 작업 제목 | Scenario | 연결 Test | 연결 Code | ECB | 체크포인트 |
|------|---------|------|-----------|----------|-----------|-----------|-----|------------|
| [ ] | TASK-029 | **RED** | P-01~P-04 성격의 **property/invariant** 테스트(최소 1~2개) | L2 | `test_property_P02_output_pair_matches_missing_set` | Domain + Boundary | Domain | PRD §9.4 |
| [ ] | TASK-030 | **GREEN** | NFR-04: 호출자 배열이 호출 후에도 비트동일 | L2 | `test_NFR04_input_matrix_unchanged_after_solve` | Boundary 전체 | **Boundary** | 스냅샷 비교 |
| [ ] | TASK-031 | **REFACTOR** | 중복 제거·이름 정리(계약 불변) | L0 | 전 스위트 회귀 | 전 레이어 | — | REFACTOR 후 전부 GREEN |
| [ ] | TASK-032 | — | **테스트 커버리지 체크포인트** | L0 | `pytest --cov` 리포트 아카이브 | CI 또는 `Makefile` | — | **NFR-01 ≥95% (Domain)**, **NFR-02 ≥85% (Boundary)**; 미달 시 Phase 역추적 |
| [ ] | TASK-033 | — | **품질 게이트** | L0 | `black`, `ruff`/`mypy`(팀 합의) | — | — | Report/3·`.cursorrules` `code_style` |

---

## 4. 최소 포함 매핑 (요청하신 작업 ↔ Task)

| 요청 항목 | Task ID |
|-----------|---------|
| 보드 생성 | TASK-002, TASK-006 (`PuzzleGrid`/복사) |
| 보드 유효성 검사 | TASK-007, TASK-010, TASK-012 |
| 빈칸 탐지 | TASK-014, TASK-015 |
| 후보값 필터링 | TASK-016, TASK-017 (누락 두 수); 배치 후보는 TASK-018~TASK-022 |
| 완성 로직 | TASK-018~TASK-023 |
| 잘못된 입력 처리 | TASK-008, TASK-009, TASK-012, TASK-013 |
| 테스트 커버리지 체크포인트 | TASK-032, TASK-033 |

---

## 5. Dual-Track 작업 순서 메모 (PRD §8.3)

- 동일 Phase에서 **Boundary RED(TASK-008~009)**와 **Domain RED(TASK-007 등)**를 먼저 병렬로 두고, GREEN은 트랙별 최소 구현(TASK-010, TASK-012) 후 REFACTOR(TASK-011, TASK-013) 순을 권장합니다.  
- **금지:** 도메인 전부 구현 후 경계만 추가(PRDD §8.3).

---

## 6. Scenario Level 사용 요약

- **L0:** Epic/파이프라인/커버리지 게이트  
- **L1:** M1/M2 정상, 마방진 true, 성공 `int[6]`  
- **L2:** 탐지 순서, 스키마, 복사·결정론, property  
- **L3:** U-xx/T-xx 오류·`NOT_MAGIC`·내부 래핑  

---

원하시면 이 보드를 `docs/Implementation_Todo_MagicSquare_4x4.md` 같은 파일로 저장하는 패치까지 적용할 수 있습니다.

---

**User**

잘했습니다. 이제 만들어주신Ｔｏ－Ｄｏ　리스트를  포함해 READMD.md 파일을 만들고 싶습니다. 무슨 문서를 참조하면 좋을까요?

---

**Cursor**

README 구성에 맞는 참조 문서를 정리합니다. 현재 `README.md` 상태를 확인합니다.



프로젝트 루트 구조를 확인한 뒤 README에 넣을 ‘참조 문서’ 안내와 실용적인 README 초안을 작성합니다.



참조 가이드를 README에 반영하고, 긴 To-Do는 `docs/`에 두어 README가 읽기 쉽게 유지되게 합니다.



README의 Report 링크에 공백이 있어 인코딩을 통일합니다.



다음처럼 정리하면 됩니다.

## README에 무엇을 참조하면 좋은지

1. **`docs/PRD_MagicSquare_4x4_TDD.md`** — 한 줄로 말하면 **진실의 원천**. 기능·완료 조건·FR/BR/NFR·테스트 ID·Dual-Track·§12 추적표까지 README의 “무엇을 만들지”는 여기에 맞추면 됩니다.  
2. **`Report/4. UserJourney_Backlog_Report.md`** — Epic·여정·스토리 관점으로 README나 To-Do를 **사용자/학습 목표**에 묶을 때.  
3. **`Report/2. LayeredDesign_TDD_Report.md`** — **계약·오류 코드·도메인 컴포넌트 이름**을 README나 구현 계획에 적을 때.  
4. **`Report/1. ProblemDefinition_Report.md`** — README 상단 **배경·Invariant·왜 4×4인지** 짧게 쓸 때.  
5. **`Report/3. CursorRules_WorkReport.md`** + **`.cursorrules`** — **개발 방식·금지 사항·커버리지·ECB**를 “기여 방법”에 쓸 때.

동일 PRD 본문은 **`Report/5. PRD_Report.md`**에도 있으므로, 링크는 하나만 골라 **단일 진입 경로**로 안내하는 편이 좋습니다.

---

## 적용해 둔 것

- **`README.md`** — 위 문서들을 표로 정리하고, To-Do는 길이를 줄이기 위해 **`docs/Implementation_Todo_MagicSquare_4x4.md`**로 링크했습니다. README에는 Epic/US 체크만 두었습니다.  
- **`docs/Implementation_Todo_MagicSquare_4x4.md`** — 이전에 드린 To-Do의 Epic·US·Phase 요약·매핑·Dual-Track 메모를 넣었습니다. **TASK별 전체 표(각 열 RED/테스트/ECB 등)**는 한 번에 넣으면 파일이 매우 길어져서, 채팅에 있던 전체 표를 그대로 붙여 넣거나 PRD FR 단위로 행을 추가하는 방식을 본문에 안내해 두었습니다.

전체 Task 표까지 `Implementation_Todo` 파일 안에 모두 옮기길 원하시면, 그때는 채팅에 있던 긴 표를 그 파일로 옮기면 됩니다.

---

**User**

좀더 자세하게 갑시다. README 본문·To-Do·검증 기준은 docs/5.PRD_MagicSquare_4x4_TDD.md를 중심에 두고, 스토리 표현은 Report/4, 오류·계약 요약은 Report/2, 실행·ECB·TDD는 Report/3 + pyproject.toml + Cursor 규칙, 문서 관계 한 줄은 Report/5를 참조해서 To-Do 리스트를 포함한 MagicSquare를 만들기 위한 README.md 파일을 만들어줘.


---

**Cursor**

PRD·Report/5·프로젝트 설정을 읽고 `docs/5.PRD_MagicSquare_4x4_TDD.md`를 정식 경로로 정리한 뒤 상세 README를 작성합니다.



`docs/5.PRD_MagicSquare_4x4_TDD.md` 생성, `Report/5`·`docs/PRD_*` 동기 문구 정리, `pyproject.toml` 추가, README 본문 확장.



`pyproject.toml` 추가 및 `Implementation_Todo`·`README.md` 갱신 중입니다.



`pyproject.toml`의 패키지 발견 설정이 실제 패키지 없이는 실패할 수 있어, `.cursorrules` 권장에 맞춰 최소 패키지 스텁을 추가합니다.



개발 환이 Python 3.10이라 `requires-python`을 완화하고, `pytest` 없이도 동작하도록 README에 두 가지 실행 방법을 적습니다.



상세 `README.md` 작성 및 `Implementation_Todo`를 `docs/5` 기준으로 갱신합니다.



작업을 반영했습니다. 요약만 정리합니다.

## 한 일

1. **`docs/5.PRD_MagicSquare_4x4_TDD.md`**  
   - 기존 PRD 전문을 복사해 두고, 상단에 **정식 경로(LSSOT)**·**문서 관계 한 줄**(`Report/5`와의 역할)을 명시했습니다.  
   - 문서 이력도 한 줄로 정리했습니다.

2. **`docs/PRD_MagicSquare_4x4_TDD.md`**  
   - **`5.PRD...`로만 편집**하라는 리다이렉트만 두었습니다.

3. **`Report/5. PRD_Report.md`**  
   - 서두의 **동기 사본** 문구를, 요청하신 **「문서 관계 한 줄」** 형태로 바꿨습니다(정식 PRD = `docs/5`, Report·구 PRD 경로 = 동기·호환).

4. **`pyproject.toml`**  
   - `project`, `optional-dependencies.dev`(pytest, pytest-cov), `[tool.pytest.ini_options]`, `[tool.coverage.*]`를 추가했습니다.  
   - CI/로컬에서 `pip install`이 되도록 `requires-python`은 **`>=3.10`**으로 두었고, README에는 PRD·`.cursorrules`가 말하는 **3.11+ 권장**을 적어 두었습니다.

5. **최소 패키지·테스트**  
   - `src/magic_square/__init__.py`, `tests/test_smoke.py`로 `pytest`/`coverage`가 돌아가게 했습니다.

6. **`docs/Implementation_Todo_MagicSquare_4x4.md`**  
   - 주 소스를 **`docs/5` PRD**로 바꾸고, **TASK-001~TASK-033 전체 표**를 넣었습니다.

7. **`README.md`**  
   - 본문·검증 기준·To-Do 요약을 **`docs/5` PRD 중심**으로 재작성했고, 스토리는 **`Report/4`**, 계약·오류 표는 **`Report/2` + PRD §8.1**, 실행·ECB·TDD는 **`Report/3` + `pyproject.toml` + `.cursorrules`**, 문서 관계 한 줄은 **`Report/5` 인용** 형태로 맞춰 두었습니다.

이제 README에서 PRD를 가리킬 때는 **`docs/5.PRD_MagicSquare_4x4_TDD.md`**만 기준으로 잡으면 됩니다.

---

**User**

작업중에 docs의 문서가 세개로 늘어났는데, 중복된게 대부분인거같아. 세 문서 내용과 역할을 하나로 통합해줘.

---

**Cursor**

docs 폴더의 세 문서와 저장소 전체의 참조를 확인한 뒤 하나로 통합합니다.



Python으로 본문을 추출해 통합 파일을 생성하고, 기존 세 파일을 제거한 뒤 참조를 갱신합니다.



Python 삼중따옴표에서 `\t`가 탭으로 해석되어 표가 손상되었습니다. §13.3 표 전체를 올바른 내용으로 교체합니다.



작업을 반영했습니다.

## 결과: `docs/`는 파일 하나

**[`docs/MagicSquare_4x4_TDD.md`](docs/MagicSquare_4x4_TDD.md)** 하나로 합쳤습니다.

| 이전 파일 | 통합 후 |
|-----------|---------|
| `docs/5.PRD_MagicSquare_4x4_TDD.md` | 삭제 → 본문은 §1~§12로 편입 |
| `docs/PRD_MagicSquare_4x4_TDD.md` | 삭제 |
| `docs/Implementation_Todo_MagicSquare_4x4.md` | 삭제 → **§13 구현 To-Do 보드**로 편입 |

### 통합 문서 구조

1. **머리말** — 역할(요구·검증·To-Do 단일 원천), `Report/5`와의 관계, 버전 **1.1**, 근거 Report·`.cursorrules`  
2. **§1~§12** — 기존 PRD와 동일(Executive Summary ~ Traceability Matrix)  
3. **§13** — Epic, User Story, TASK-001~033 표, Dual-Track, Task·Test 추적  
4. **문서 이력** — 통합(1.1) 행 추가  

### 같이 수정한 곳

- **`README.md`** — 링크·문구를 모두 `docs/MagicSquare_4x4_TDD.md` 기준으로 수정, To-Do는 **§13** 안내  
- **`Report/5. PRD_Report.md`** — “정식 본문”을 통합 경로로 수정, 목적/범위에 §13·통합본 설명 추가, 문서 이력 한 줄 갱신  
- **`src/magic_square/__init__.py`**, **`pyproject.toml`**, **`Prompts/PRD_prompt.md`** — 경로 문구 정리  
- **`pip install -e ".[dev]"`** 로 `egg-info` 재생성  

이제 `docs/`에는 **`MagicSquare_4x4_TDD.md`만** 두면 됩니다. 예전 경로로 북마크한 경우 README·Report/5의 “문서 관계 한 줄”을 따라 새 파일로 옮기면 됩니다.

---

**User**

좋습니다. 이제 작업내역 Report 디렉토리에 내보내고 마무리합시다

---

**Cursor**

Report 폴더의 명명 규칙을 확인한 뒤 작업 내역 보고서를 추가합니다.



`Report/6. Documentation_Consolidation_WorkReport.md`를 추가하고 README의 문서 표에 링크를 넣습니다.



작업을 마쳤습니다.

## 추가한 보고서

**[`Report/6. Documentation_Consolidation_WorkReport.md`](Report/6.%20Documentation_Consolidation_WorkReport.md)**

- **목적·범위·비범위** — `Report/3` 스타일과 맞춤  
- **배경** — `docs/` 3파일 중복 문제  
- **수행 요약 표** — 통합본 경로, 삭제 파일(정확한 이름), README·Report/5·기타 수정, §13 표 보정, pytest 검증  
- **통합 후 `docs/` 트리**  
- **문서 관계** — 정식본 vs `Report/5` 동기  
- **후속 제안** — CI 검사, Report/5와 §13 동기 절차  
- **참고 경로** 표  

## 같이 반영한 링크

- **`README.md`** — 문서 표에 `Report/6` 한 줄 추가  
- **`docs/MagicSquare_4x4_TDD.md`** — 문서 이력 1.1 행에 Report/6 수록 문구 추가  
- **`Report/5. PRD_Report.md`** — 관련 Report 목록에 `Report/6` 추가  

이제 통합 작업 요약은 **`Report/6`**에서만 따라가면 됩니다.


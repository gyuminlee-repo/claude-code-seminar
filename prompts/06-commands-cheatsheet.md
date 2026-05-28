# Section 06 명령어 cheatsheet (슬 60-67)

세미나 중 실제로 한 번씩 눌러보는 명령. 복붙 가능하지만 개념 위주이므로 cheatsheet으로 활용.

## /model (슬 62-63)

```
/model
```

가벼운 작업은 Haiku, 일상 작업은 Sonnet, 복잡한 추론은 Opus.
느리거나 비싸다고 느낄 때 가장 먼저 확인할 곳.

### 모델별 적합 작업

| 모델 | 적합 작업 |
|------|----------|
| Haiku | CSV 컬럼명 변경, 파일 이름 정리, 단순 포맷 변환 |
| Sonnet | GC content 계산, 그래프 그리기, 코드 수정·리팩토링 |
| Opus | 논문 분석·요약, 파이프라인 설계, 멀티스텝 디버깅 |

### 에이전트별 모델 배정 예

`.claude/agents/lit.md` 상단에 지정:

```yaml
---
model: opus
---
문헌 검색 전문 에이전트.
```

또는 Agent 호출 시 지정:

```python
Agent(subagent_type="lit", model="opus")
Agent(subagent_type="viz", model="sonnet")
```

## /btw (슬 64)

```
/btw 그 config 파일 이름이 뭐였지?
```

작업 중에도 사이드 질문이 가능한 오버레이.
질문과 답이 대화 히스토리에 남지 않으므로 맥락 오염 없음.
Space, Enter, Esc로 닫는다.

`/btw`는 이미 아는 것을 확인할 때, 서브에이전트는 새 정보를 찾아올 때.

## /rewind (슬 65)

```
/rewind
```

ESC를 두 번 눌러도 동일. 각 prompt마다 자동 체크포인트가 잡혀 있어 잘못된 방향을 선택적으로 되감는다.

### 복원 옵션

- 코드만 복원
- 대화만 복원
- 코드 + 대화 모두 복원

### /clear vs /compact vs /rewind

| 명령 | 용도 |
|------|------|
| /clear | 새 주제 시작 |
| /compact | 전체 대화 압축 |
| /rewind | 특정 시점 선택 복구 + 압축 |

bash로 직접 바꾼 파일은 추적하지 않는다. Git 대체 아님.

## /compact (슬 66)

```
/compact
```

또는 남길 정보를 명시:

```
/compact DE 분석 결과와 다음 단계만 남기고 압축해줘.
```

Context 50%부터 조치 권장.

## 토큰 절약 (슬 67)

- 한글 1글자 약 2~3 토큰, 영어 1단어 약 1 토큰
- 비싼 작업은 사전 압축
- 서브에이전트로 중간 추론을 메인 윈도우에서 격리

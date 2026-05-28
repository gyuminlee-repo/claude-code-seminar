# agent-view · 다중 에이전트 시각화 (슬 80)

## 시나리오
여러 서브에이전트를 병렬로 실행할 때, 메인 세션 한 화면에서 Wave 0 병렬 -> Wave 1 합치기 흐름을 한눈에 본다. Claude Code 기본 시각화 도구.

## 사전 지식 · git worktree

브랜치별 독립 폴더. 여러 에이전트가 같은 repo의 다른 브랜치를 동시에 작업할 수 있다.

```bash
git worktree add ../feature feature-branch
```

`../feature` 폴더에 격리된 작업 환경이 한 줄로 생성된다.

## 병렬 실행 다이어그램

```
[main] ─┬─▶ [Agent A] ─┐
        ├─▶ [Agent B] ─┤─▶ [verify] ─▶ done
        └─▶ [Agent C] ─┘
```

## 활용 시나리오

- 독립 작업 2~5개를 동시에 띄울 때 진행 상황을 한 화면에서 추적
- 같은 파일·디렉토리를 수정할 가능성이 있으면 worktree 격리 필수
- Wave 0 (병렬 실행) 후 Wave 1 (verify·merge)로 합치는 패턴

## 핵심 학습 포인트
- agent-view는 별도 설치 없이 기본 제공되는 시각화 UI
- worktree 격리로 같은 repo 안에서 충돌 없이 병렬 작업 가능
- 병렬 -> 검증 -> 합치기 3단 패턴이 가장 안전

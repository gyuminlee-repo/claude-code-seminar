# /statusline 터미널 상태 표시줄 (슬 79, 81)

## 시나리오
터미널 하단에 모델, 컨텍스트 사용량, 도구 활동을 실시간 표시. `/compact` 타이밍을 놓치지 않기 위한 상시 대시보드.

## 보여주는 정보 (예)

```
[Opus | Max] my-project git:(main*)
Context █████░░ 45% | Usage 25% (1h/5h)
도구 활동: Edit auth.ts | Read x3
```

## 편의성 설치 · 플러그인 사용

```
Github에서 claude-dashboard 설치해
```

원본: https://github.com/uppinote20/claude-dashboard

## 플러그인 3단계 (슬 79)

```
/plugin marketplace add <owner/repo>
```

```
/plugin install 이름@마켓플레이스
```

```
/이름:명령
```

## 핵심 학습 포인트
- statusline은 컨텍스트가 얼마나 찼는지 실시간 확인하는 핵심 UI
- 플러그인은 스마트폰 앱 설치와 비슷한 흐름 (검색 -> 설치 -> 사용)
- 필요한 기능은 빌드 전에 먼저 찾는다 (search before building)

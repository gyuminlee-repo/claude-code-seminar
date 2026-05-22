---
date: 2026-05-18
updated: 2026-05-18
type: reference
project: internal_seminar
tags:
  - claude-code
  - tmux
  - 세미나
  - 실습-프롬프트
  - hands-on
references:
  - $WORKSPACE_ROOT/cc/work/output/260513_seminar_kribb_internal_v2.pptx
  - $OBSIDIAN_VAULT/010.KRIBB/060.Lab_Seminar/260513_KRIBB_세미나_deck_빌드_결과.md
  - $OBSIDIAN_VAULT/010.KRIBB/060.Lab_Seminar/260501_CC세미나_완전판_outline.md
  - $OBSIDIAN_VAULT/020.Wiki_Knowledge/050.Vibe_coding/060.CLI/001.tmux_주요_키.md
  - $OBSIDIAN_VAULT/998.Claude_code/020.Memory/reference_gml_tmux_kit.md
---

# tmux 셋업 프롬프트 (세미나 실습용)

## 핵심

KRIBB 내부 세미나 청중이 Claude Code TUI 한 창에서 복붙 한 번으로 tmux Alt-키 환경을 만드는 실습 프롬프트. sudo 일절 금지, Alt+숫자(Claude Code TUI 점유 키) 제외, prefix-less 단축키, OS 분기 자동(macOS/Ubuntu/WSL2). 옵션 A(자립형 long-form) 대신 옵션 B(짧은 일임형) 채택. 슬라이드에 그대로 박을 수 있는 길이.

## 슬라이드 안내 한 줄

`sudo 없음 · Alt+숫자 없음 · 홈 디렉토리만 건드림`

## 실습 흐름 (청중 멘트 후보)

1. 터미널에서 `claude` 실행
2. 아래 프롬프트 박스 한 덩어리 복붙 → Enter
3. dry-run 차이 확인 → `y` 승인
4. `Alt+D`, `Alt+방향키`, `Alt+Z` 시연 (1~2분)

## 프롬프트 전문 (옵션 B 최종본)

```
내 머신에 tmux 단축키 환경을 만들어줘.

전제
- sudo 일절 금지. 시스템 디렉토리 쓰기 금지.
- 변경 범위는 ~/.tmux.conf와 ~/.tmux/ 만.

시작 전 확인
- Claude Code TUI가 점유하는 단축키 목록 먼저 확인 (claude --help, ? 키, 공식 docs).
- 충돌 키는 tmux 바인딩에서 제외하고 보고. Alt+1~0은 무조건 제외.

요구사항
- prefix는 Ctrl+B 유지, 실사용은 모두 prefix-less (`bind -n M-x`)
- 필수 바인딩:
  좌우 분할(Alt+D), 상하 분할(Alt+Shift+D),
  패인 이동(Alt+방향키), 패인 크기 조절(Alt+Shift+방향키),
  줌 토글(Alt+Z), 패인 닫기(Alt+W),
  새 윈도우(Alt+T), 이전/다음 윈도우(Alt+[ / Alt+]),
  설정 리로드(Alt+R)
- 윈도우 번호 점프는 tmux 기본 prefix 방식(Ctrl+B → 숫자) 사용. Alt+숫자 바인딩 금지.
- mouse on, history 50000줄, 256색 + truecolor
- 클립보드 OS 자동 분기 (macOS pbcopy / Linux xclip / WSL clip.exe)
- 윈도우 이전/다음 키는 conf에 `bind -n "M-[" previous-window` / `bind -n "M-]" next-window` 형태로 따옴표 처리 (대괄호는 tmux 파서에서 special character).
- TUI 충돌 키 확인 단계에서 docs 접근 불가 시: 알려진 충돌 목록(Alt+숫자, Esc 시퀀스 등)만 출력하고 청중에게 추가 충돌 키 있는지 물은 뒤 진행.

순서
1. OS 확인 (macOS / Ubuntu / WSL2)
2. `command -v tmux`로 설치 여부 확인.
   없으면 sudo 없이 깔 수 있는 명령 우선 제시 후 멈춤:
     macOS:  brew install tmux
     Linux:  mamba install -c conda-forge tmux  (또는 conda)
     마지막 선택지: sudo apt install -y tmux
   설치는 사용자가 직접. 완료 알려주면 재개.
3. 기존 ~/.tmux.conf 있으면 ~/.tmux.conf.backup.<날짜>로 백업
4. 위 요구사항대로 ~/.tmux.conf 작성 (Alt+숫자, TUI 충돌 키 제외)
5. tmux 실행 중이면 `tmux source-file ~/.tmux.conf`로 즉시 반영
6. macOS면 사용 중인 터미널 앱 물어보고 Option=Meta 설정법 안내
7. 시도해볼 단축키 5개 표 출력

실행 전 dry-run으로 변경 사항 먼저 보여주고 승인 받기.
```

## 설계 결정 메모

| 결정 | 이유 |
|---|---|
| sudo 금지 | 청중 환경(공용 서버·관리자 권한 없는 노트북) 안전 보장 |
| Alt+숫자 바인딩 금지 | Claude Code TUI 점유 키(subagent 선택 등)와 충돌. 윈도우 번호 점프는 tmux 기본 prefix(Ctrl+B → 숫자)로 우회 |
| prefix-less (`bind -n M-x`) | 모던 터미널 UX와 일관. 1단계 입력. prefix는 Ctrl+B 유지하여 호환성 확보 |
| OS 자동 분기 | macOS(brew + pbcopy), Ubuntu(mamba + xclip), WSL2(clip.exe). 청중 환경 사전 파악 불요 |
| dry-run 승인 게이트 | ~/.tmux.conf 덮어쓰기 전 차이 확인. 기존 설정 보존(`.backup.<날짜>`) |
| 옵션 B 채택 | 슬라이드 박스 한 화면 안에 들어가는 길이. 옵션 A 자립형 long-form은 청중이 한눈에 못 봄 |

## 시도용 단축키 5개 (시연 순서)

| 동작     | 키       |
| ------ | ------- |
| 좌우 분할  | Alt+D   |
| 패인 이동  | Alt+방향키 |
| 줌 토글   | Alt+Z   |
| 새 윈도우  | Alt+T   |
| 설정 리로드 | Alt+R   |


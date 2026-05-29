# Claude Code 입문 실습 자료

Claude Code 입문 세미나 실습용 파일 모음. 발표자 이규민.

세미나 슬라이드의 데모 단계에서 청중이 그대로 따라 할 수 있도록 입력 파일을 미리 준비.

## 빠른 시작

```bash
git clone https://github.com/gyuminlee-repo/claude-code-seminar.git
cd claude-code-seminar
claude
```

`claude` 실행 후 다음 프롬프트를 차례대로 시도.

## 파일 목록

| 파일 | 용도 | 등장 슬라이드 |
|------|------|--------------|
| `meeting-note.md` | raw 회의록. "회의록 형식으로 정리해줘"로 재정돈 데모 | 첫 프로젝트, 연구 자동화, 마지막 체크리스트 |
| `example.md` | Markdown 공용어 시각화 데모 | Section 01 기초 |
| `data/de_results.csv` | E. coli K-12 stress response DEG 30 유전자 (dnaK·groEL·rpoH·soxR 등) | Section 5 연구 자동화 |
| `risks.md` | 프로젝트 위험도 raw 메모. HTML 리포트 위험도 색상 표시 입력 | Slide 45 실습 3 HTML 리포트 |
| `tmux-setup-prompt.md` | tmux 분할·세팅 안내 프롬프트 (실습 환경 준비) | Section 02 설치와 로그인 (Slide 25) |
| `experiments/260520_od600.csv` | raw OD600 timecourse (16 timepoint × 3 rep) | Slide 50 Plan Mode (연구 자동화 템플릿) |
| `notes/260521_idea.md` | 다음 실험 아이디어 raw 메모 | Slide 50 Plan Mode |
| `analysis/sketch_rbs_fit.py` | 미완성 Python 분석 스크립트 (TODO 상태) | Slide 50 Plan Mode |
| `prompts/02-email-draft.md` | 실습 2 prompt 시드. 미팅 노트로 회신 이메일 초안 작성 | Section 05 실습 2 |

## 데모 흐름 예시

### 1. 회의록 정리
```
이 폴더의 파일을 읽고, 무슨 작업 폴더인지 5줄로 설명해줘.
그다음 meeting-note.md를 회의록 형식으로 정리해줘.
수정 전에는 어떤 파일을 바꿀지 먼저 말해줘.
```

### 2. 미팅 노트 → 회신 이메일 초안
```
meeting-note.md 읽고, 미팅에서 결정된 사항과 내가 해야 할 액션을 추려서
정중한 톤의 회신 이메일 초안 markdown 으로 작성해줘.
수신자는 PI (이혜원 박사님), 발신자는 나(이규민) 가정.
```
상세 prompt 시드: `prompts/02-email-draft.md` 참조.

### 3. DEG 데이터 시각화
```
data/de_results.csv를 보고 가장 강하게 발현이 변한 유전자 5개를 알려줘.
이걸로 막대 그래프 Python 스크립트를 expression_plot.py로 만들어줘.
```

### 4. HTML 리포트
```
방금 분석한 내용을 results/report.html로 정리해줘. 표와 그래프를 포함해서.
```

## 슬라이드별 prompt 인덱스

청중은 발표 중 슬라이드에 나오는 명령을 그대로 복붙할 수 있습니다.

| 슬라이드 | 주제 | 파일 |
|---|---|---|
| 슬 48 | CLAUDE.md 작성 | [templates/CLAUDE.md.template](./templates/CLAUDE.md.template) |
| 슬 50 | 골든패스 6단계 | [prompts/04-golden-path-6steps.md](./prompts/04-golden-path-6steps.md) |
| 슬 54 | 실습 1 · Markdown 노트 정리 | [prompts/01-markdown-notes.md](./prompts/01-markdown-notes.md) |
| 슬 55 | 실습 2 · 이메일 초안 | [prompts/02-email-draft.md](./prompts/02-email-draft.md) |
| 슬 56 | 실습 3 · HTML 리포트 | [prompts/03-html-report.md](./prompts/03-html-report.md) |
| 슬 60-67 | Section 06 명령어 cheatsheet | [prompts/06-commands-cheatsheet.md](./prompts/06-commands-cheatsheet.md) |
| 슬 61 | Plan Mode 실습 | [prompts/05-plan-mode.md](./prompts/05-plan-mode.md) |
| 슬 72 | 최소 SKILL.md 골격 | [templates/skill-minimal.md.template](./templates/skill-minimal.md.template) |
| 슬 73 | /clip 스킬 만들기와 사용 | [prompts/07-clip-skill.md](./prompts/07-clip-skill.md) |
| 슬 79, 81 | statusline + 플러그인 | [prompts/09-statusline-plugin.md](./prompts/09-statusline-plugin.md) |
| 슬 80 | agent-view + worktree | [prompts/08-agent-view.md](./prompts/08-agent-view.md) |
| 슬 90 | 1페이지 자동화 plan | [templates/automation-plan.md](./templates/automation-plan.md) |

## 청중 환경 권장

- macOS 또는 WSL2 Ubuntu
- Node.js 또는 Claude Code 설치
- VS Code 또는 다른 텍스트 에디터

## 학습 후 다음 단계

세미나 슬라이드의 도입 로드맵(Day 1 → Week 2) 따라 진행.

1. 자기 프로젝트 폴더에서 `claude` 실행
2. `CLAUDE.md`에 자기 작업 규칙 한 줄씩 추가
3. 반복 작업은 스킬로 묶기

## 라이선스

CC0. 자유롭게 복사, 수정, 재배포.

# Claude Code 입문 실습 자료

KRIBB 사내 세미나(2026-05-29) 실습용 파일 모음. 발표자 이규민.

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
| `papers/crispri-functional-genomic-screening.pdf` | CRISPRi functional genomic screening 논문 PDF | Slide 47 5분 라이브 데모 (PDF 요약) |
| `experiments/260520_od600.csv` | raw OD600 timecourse (16 timepoint × 3 rep) | Slide 50 Plan Mode (연구 자동화 템플릿) |
| `notes/260521_idea.md` | 다음 실험 아이디어 raw 메모 | Slide 50 Plan Mode |
| `analysis/sketch_rbs_fit.py` | 미완성 Python 분석 스크립트 (TODO 상태) | Slide 50 Plan Mode |

## 데모 흐름 예시

### 1. 회의록 정리
```
이 폴더의 파일을 읽고, 무슨 작업 폴더인지 5줄로 설명해줘.
그다음 meeting-note.md를 회의록 형식으로 정리해줘.
수정 전에는 어떤 파일을 바꿀지 먼저 말해줘.
```

### 2. DEG 데이터 시각화
```
data/de_results.csv를 보고 가장 강하게 발현이 변한 유전자 5개를 알려줘.
이걸로 막대 그래프 Python 스크립트를 expression_plot.py로 만들어줘.
```

### 3. HTML 리포트
```
방금 분석한 내용을 results/report.html로 정리해줘. 표와 그래프를 포함해서.
```

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

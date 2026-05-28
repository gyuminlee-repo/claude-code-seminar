# 실습 3 · HTML 리포트 (슬 56)

## 시나리오
한 프로젝트 폴더의 현황, 결정 사항, 다음 액션, 위험도를 한 페이지 HTML 리포트로 정리한다. 검토용 산출물은 HTML로, 원본 규칙과 기록은 Markdown으로 분리한다.

## 입력
- 이 repo 전체 (`meeting-note.md`, `risks.md`, `data/`, `experiments/` 등)

## Claude 명령

```
이 폴더 내용을 바탕으로
한 페이지 HTML 리포트를 만들어줘.

포함:
- 진행 현황 요약
- 결정 사항 표
- 다음 액션 체크리스트
- 위험도 색상 표시

파일명: report/report.html
```

## 기대 출력 (구조)
- `report/report.html` 단일 파일
- 진행 현황 요약 (상단 summary 박스)
- 결정 사항 표 (HTML table)
- 다음 액션 체크리스트 (checkbox 또는 bullet)
- 위험도 표시 (low/med/high를 녹·황·적 색상으로)

## 핵심 학습 포인트
- 지침은 Markdown, 산출물은 HTML로 분리하면 검토자에게 보내기 좋음
- 항목 4개를 명시하면 누락 없이 한 페이지로 합성됨
- 출력을 별도 폴더에 저장해 입력과 산출물 경계가 명확해짐

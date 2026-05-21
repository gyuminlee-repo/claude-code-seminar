오늘 lab meeting 휘갈김

5/22 월 오전 10시 좀 늦게 시작 (PI 다른 회의 끝나고 헐레벌떡 오심, 한 10분 늦음)
센터 4층 회의실. 나(박지훈), 정수영 한도윤 학생.
김민서 교수님 — 처음에 커피 들고 들어오심

---

지훈 (나) — GFP RBS variant library
- 지난주 transformation 한거 colony pick 18개 → Sanger 시퀀싱 결과 어제 도착
- 6단계 RBS 강도 분포는 어느정도 잡힘. 그런데 클론 몇 개가 좀 이상함
  · 4번 클론 — 백본 일부 deletion 의심됨 (서열 갭). 다시 prep 해야할듯
  · 7번 클론 — chromatogram에 mixed peak. contamination이거나 콜로니가 mixed 였던듯
  · 11번 클론 — 의도 안 한 단순 mutation 1개 추가됨. 이건 그냥 빼고 갈지 고민
- 수요일에 plate reader (BMG 기존거) 잡아둠. OD600 / 혀랑 GFP 측정. 96 well 두 plate
- 다음 단계 — RBS 강도랑 GFP 발현 상관관계 fitting. Anderson promoter 시리즈 (BBa_J23100 ~ J23119) 데이터랑 비교해서 reference curve로 쓸지
- PI 코멘트 — "이거 abstract 들어갈만한 결과니까 raw data 정리 잘 해둬라" → ㅇㅋ

수영 — Gibson assembly 또 막힘
- 이번이 3번째 시도임. colony 4개 나왔는데 positive 2개. 효율 50%
- 첫번째 시도는 0/8, 두번째 1/6 이었으니 점점 나아지긴 하는데 너무 느림
- PI 의견 — insert:vector 비율 3:1로 올리자. fragment 농도 측정 nanodrop 말고 Qubit으로 다시 잡으라고
  (nanodrop은 RNA/protein contam 때문에 과대측정 가능성)
- 내(박사후) 의견 — NEB HiFi assembly mix 50°C 60분 → 75분으로 늘려보기. fragment 길어서 시간 더 필요할수도. BsaI digestion 시간도 4시간 → 6시간 옵션
- 백본 자체를 새로 prep 해야 하는지는 미해결. 다음 주 결정하기로
- SnapGene 시뮬레이션 결과랑 실제 결과 살짝 안 맞음 — overhang 1bp 차이 의심됨. primer 디자인 다시 봐야할듯
- 수영이 표정 좀 지쳐있음. "이거 4번째도 안되면 어떡하죠" 라고 — 괜찮다고는 했는데

도윤 — 대장균 코돈 최적화
- human Lysozyme E.coli 발현용 코드 거의 완성. Python 스크립트
- CAI 0.78까지 끌어올림. 참고로 JCat 비교 0.81, IDT codon optimizer 0.79 — 비슷한 수준
- PI 팦드백 — "CAI만 보면 안된다, GC% 같이 봐야". 현재 평균 GC 52%인데 일부 high-GC region 65% 넘는 구간 있음. 균일성 떨어짐
- 다음 주까지 추가할거
  → %MinMax 분석 (Clarke & Clark 2008 metric) 넣기
  → BL21 tRNA pool 데이터 기반으로 rare codon 분포 다시 보기
  → high-GC stretch는 codon swap으로 평탄화 시도
- 도윤이 코드 깃헙에 올려놓는다 했는데 아직 안 올라옴. 내가 review 하기로

---

6월 미생물학회 abstract
- 마감 6월 5일 (목)
- 1저자 박지훈 확정, 2저자 정수영
- figure 2개 무조건 (PI 강조). 정량 데이터 필수
- 정수영 Gibson trouble shooting 내용 supplementary로 넣을지 — PI는 일단 보류. positive 결과 위주로 가자고
- abstract draft 내가 5/26까지 1차 작성하기로. PI 검토ㅎ 후 5/29 미팅에서 finalize
- 아 일정 빡빡

plate reader 새거 도입 검토
- 견적 3군데 받음
  * BMG CLARIOstar
  * Tecan Infinite M Nano+
  * BioTek Synergy H1
- 도윤이가 정리. 다음 주 견적 비교 표 + 사양 비교 가져오기
- BMG 기존거는 그대로 둘건지 폐기인지 — 미정. 그렁 보면 백업으로 둘듯
- 예산 라인 어디서 끌어올지는 PI가 행정 통해 확인

외부 협업 (안건 외였는데 미팅 끝나기 직전 나옴)
- 옆 lab 최은서 박사님이 우리 pUC19-mCherry plasmid 공유 요청 메일 옴
- 미팅 끝나고 내가 처리 — glycerol stock 줄지 plasmid prep 해서 줄지 확인 후 회신
- MTA 필요한가? 같은 기관 내라 안 해도 될듯한데 PI한테 한번 물어봐야겠음

잡담 / PI 흘려서 한 말
- 다음 주부터 grant 준비 시작 — "다들 마음의 준비 좀" (PI)
- 6월 학회 출장 일정 다음 미팅에서 확정. 셋 다 갈지 둘만 갈지
- 신입 석사 면접 6월 둘째 주 예정. 후보 2명
- 회식 다음 주 금요일쯤 — 일단 검토만

---

내 할일 ★ (까먹지말것)
1. 도윤이 코돈 최적화 코드 review (깃헙 푸시 받자마자)
2. 수영 Gibson 새 조건 셋업 도와주기 — 수요일까지
3. 학회 abstract draft 작성 — 5/26 (월)까지 1차
4. 최은서 박사님께 plasmid 공유 메일 — 오늘 안에
5. 내 Sanger 결과 raw data 정리 + plate reader 결과 합쳐서 figure 초안
6. 4번 11번 클론 처리 어떻게 할지 결정 (drop or re-prep)

다음 미팅 5/29 (화) 오전 10시 — 같은 회의실
PI 그때 grant 얘기 또 꺼낼듯, 미리 마음 준비

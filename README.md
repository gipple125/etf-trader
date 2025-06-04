# 📈 ETF 자동화 시스템

이 프로젝트는 Python과 MySQL을 기반으로 한 **ETF 투자 기록 및 매수 전략 자동화 시스템**입니다.  
정액 매수, RSI 매매 전략, Telegram 알림 등의 기능을 순차적으로 구현하며,  
데이터는 MySQL에 저장되고, 학습 기록은 Notion에 병행 관리됩니다.

---

## ✅ 기능 요약 (진행 중 기능 포함)

- [x] MySQL 기반 ETF 정보 DB 구축
- [x] Python → MySQL 자동 연동
- [x] `.env`로 민감 정보 보안 처리
- [ ] RSI 매수 전략 구현
- [ ] Telegram 알림 시스템 연동
- [ ] 백테스트 및 리밸런싱 시스템
- [ ] Notion 연계 학습 기록 자동화

---

## 🧱 폴더 구조

```text
etf-system/
├── db/                  # DB 스키마 및 샘플 데이터
│   └── init_schema.sql
│
├── src/                 # Python 자동화 코드
│   ├── db_connector.py
│   ├── config_loader.py
│   └── strategy_rsi.py
│
├── docs/                # 문서 및 가이드
│   └── setup_guide.md
│
├── logs/                # 실행 로그
│
├── tests/               # 테스트 코드
│
├── .env                 # 환경변수 파일 (추적 제외됨)
├── .gitignore           # Git 추적 제외 설정
├── requirements.txt     # Python 패키지 목록
└── README.md            # 📌 현재 이 문서

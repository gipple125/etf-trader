# 📊 ETF 자동화 투자 시스템

Python, MySQL, GitHub를 활용한 실전 ETF 매매 기록 및 전략 실행 자동화 시스템입니다.

---

## 📁 프로젝트 개요

- **목표**: ETF 거래 기록, 전략 분석, 자동 매매 시뮬레이션 및 확장을 위한 시스템 구축
- **사용자 환경**
  - 초기 투자금: 100만원
  - 월 추가 투자금: 약 10만원
  - 사용 증권사: 신한금융투자
- **기술 스택**
  - Python 3.x
  - MySQL Community Edition
  - VS Code + GitHub
  - dotenv, pymysql 등

---

## 📂 폴더 구조

```
etf-trader/
│
├── config/                # 설정 관리
│   ├── __init__.py
│   ├── config_loader.py   # .env 로딩
│   └── db_connector.py    # DB 연결
│
├── insert/                # 거래 삽입 스크립트
│   └── insert_trade_log.py
│
├── db/
│   └── init_schema.sql    # 테이블 생성 스크립트
│
├── .env                   # DB 설정 정보 (비공개)
├── .gitignore             # Git에 포함하지 않을 파일 목록
├── requirements.txt       # 의존성 패키지 목록
└── README.md              # 프로젝트 설명 파일
```

---

## ✅ 개발 단계별 진행 현황

| 단계 | 항목 | 완료 여부 |
|------|------|------------|
| 1단계 | 개발환경 및 가상환경 구성 | ✅ |
| 2단계 | MySQL DB 구축 및 테이블 설계 | ✅ |
| 3단계 | Python DB 연결 및 거래 삽입 구현 | ✅ |
| 4단계 | 전략 분석 및 자동화 (진행 예정) | ⏳ |
| 5단계 | 텔레그램 연동 및 자산 확장 (예정) | 🔜 |

---

## ⚙️ 초기 설정 (.env 예시)

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=etf_db
```

---

## 💾 데이터베이스 테이블 요약

### `etf_info`  
ETF 기본 정보 테이블

| 컬럼 | 설명 |
|------|------|
| etf_code | ETF 코드 |
| etf_name | ETF 이름 |
| provider | 운용사 |
| asset_class | 자산군 |
| expense_ratio | 총보수 |
| inception_date | 상장일 |

---

### `etf_trade_log`  
거래 내역 기록 테이블

| 컬럼 | 설명 |
|------|------|
| id | 고유 ID (PK) |
| etf_code | ETF 코드 (FK) |
| trade_type | BUY / SELL |
| quantity | 수량 |
| price | 단가 |
| fee | 수수료 |
| total_cost | 총비용 |
| trade_date | 거래일시 (자동 생성) |

---

## 🐍 실행 방법

1. 가상환경 활성화
```bash
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

2. 거래 기록 삽입 실행
```bash
python insert/insert_trade_log.py
```

---

## 🧱 향후 계획

- ✅ 전략 로직 작성 (RSI, 이동평균 등)
- ✅ 실시간 시그널 연동
- ✅ 텔레그램 알림
- ✅ 해외주식 등 자산군 확장
- ✅ 백테스트 기능 추가

---

## 📌 기타

- 이 프로젝트는 Notion 학습 관리 시스템 **"만능노트"**와 함께 학습 기록을 병행합니다.
- 데이터베이스는 추후 타 프로젝트들과 통합 운용할 예정이며, 현재 `MySQL Community Edition`으로 구성되어 있습니다.

---

> © 2025. 민우식 세무회계사무소. All rights reserved.

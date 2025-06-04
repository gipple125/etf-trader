import sys
import os

# 루트 경로 강제 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import pymysql
from config.db_connector import get_connection

def insert_trade(trade_data):
    """
    거래 내역을 etf_trade_log 테이블에 삽입합니다.
    :param trade_data: dict 형식의 거래 데이터
    """
    query = """
        INSERT INTO etf_trade_log (
            etf_code, trade_type, quantity, price, fee, total_cost
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (
                trade_data["etf_code"],
                trade_data["trade_type"],
                trade_data["quantity"],
                trade_data["price"],
                trade_data.get("fee", 0),
                trade_data.get("total_cost", trade_data["price"])
            ))
        conn.commit()
        print("✅ 거래 삽입 완료")
    except Exception as e:
        print(f"❌ 거래 삽입 실패: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    # 예시 데이터
    trade = {
        "etf_code": "293180",
        "trade_type": "BUY",
        "quantity": 10,
        "price": 10000.00,
        "fee": 15.00,
        "total_cost": 10015.00
    }
    insert_trade(trade)

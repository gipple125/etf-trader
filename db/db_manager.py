import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

def insert_etf_price(symbol, price, time):
    conn = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME"),
        charset='utf8mb4'
    )
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO etf_price_log (etf_code, price, timestamp) VALUES (%s, %s, %s)"
            cursor.execute(sql, (symbol, price, f"2025-{time[:2]}-{time[2:4]} {time[4:]}:00"))
        conn.commit()
    finally:
        conn.close()

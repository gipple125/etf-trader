import mysql.connector
from config.config_loader import DB_CONFIG

def get_connection():
    """
    # 📌 MySQL 연결 객체 생성
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("✅ MySQL 연결 성공")
        return conn
    except mysql.connector.Error as err:
        print("❌ MySQL 에러:", err.errno, err.sqlstate, err.msg)
    except Exception as e:
        print("❌ 일반 예외:", type(e).__name__, str(e))
    return None

if __name__ == "__main__":
    get_connection()

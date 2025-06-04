from dotenv import load_dotenv
import os

# .env 파일 불러오기
load_dotenv()

# 환경변수에서 DB 설정값 읽기
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

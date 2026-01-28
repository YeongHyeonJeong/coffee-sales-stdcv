import os
import sqlite3
import pandas as pd

# 1) 경로 설정 (프로젝트 루트 기준)
CSV_PATH = os.path.join("data", "sales.csv")
DB_PATH = os.path.join("db", "coffee_sales.db")
TABLE_NAME = "sales"

def main():
    # 2) CSV 읽기
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CSV 파일을 찾을 수 없어요: {CSV_PATH}")

    df = pd.read_csv(CSV_PATH)

    # 3) DB 연결 (없으면 자동 생성)
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    try:
        # 4) 테이블로 적재 (기존 있으면 덮어쓰기)
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

        # 5) 적재 확인 (행 개수)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {TABLE_NAME};")
        count = cur.fetchone()[0]

        # 6) 컬럼 확인
        cur.execute(f"PRAGMA table_info({TABLE_NAME});")
        columns = cur.fetchall()

        print(f"✅ DB 생성/업데이트 완료: {DB_PATH}")
        print(f"✅ 테이블: {TABLE_NAME}, 행 개수: {count}")
        print("✅ 컬럼:")
        for col in columns:
            # col: (cid, name, type, notnull, dflt_value, pk)
            print(f" - {col[1]}")

    finally:
        conn.close()

if __name__ == "__main__":
    main()
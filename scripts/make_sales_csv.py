import pandas as pd
import random

random.seed(42)

PRODUCTS = [
    ("coffee", "Beverage", 3000),
    ("latte", "Beverage", 4500),
    ("americano", "Beverage", 4000),
    ("tea", "Dessert", 2500),
    ("cake", "Dessert", 5500),
    ("cookie", "Dessert", 2000),
    ("juice", "Food", 4000),
    ("sandwich", "Food", 6500),
    ("salad", "Food", 6000),
]

NUM_ROWS = 500   # 👈 여기 숫자만 바꾸면 데이터 크기 조절 가능

rows = []

for i in range(NUM_ROWS):
    product, category, price = random.choice(PRODUCTS)
    sales = random.randint(1, 50)

    rows.append({
        "id": i,
        "product": product,
        "price": price,
        "sales": sales,
        "category": category
    })

df = pd.DataFrame(rows)
df.to_csv("data/sales.csv", index=False)

print(f"✅ sales.csv 생성 완료 ({NUM_ROWS} rows)")
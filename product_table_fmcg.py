import pandas as pd

extended_skus = {
    "10g": 5,
    "20g": 10,
    "40g": 20,
    "70g": 35,
    "120g": 55,
    "200g": 90,
    "500g": 210,
    "1kg": 390,
    "Mini Pack": 10,
    "Small Pack": 25,
    "Regular Pack": 50,
    "Family Pack": 120,
    "Value Pack": 180
}

products = {
    "Nestle": {
        "Maggi": ("Food", "Instant Noodles", ["Spicy Pepper", "Spicy Manchurian"]),
        "KitKat": ("Food", "Chocolate", ["Bites", "Spread"])
    },
    "ITC": {
        "Bingo": ("Food", "Snacks", ["Masala Tadka", "Chilli Sprinkled"]),
        "Aashirvaad": ("Food", "Atta & Spices", ["Whole Wheat Atta", "Multigrain Atta"])
    },
    "P&G": {
        "Tide": ("Home Care", "Detergent", ["Lemon Fresh", "Jasmine Fresh"]),
        "Pampers": ("Baby Care", "Diapers", ["New Born", "Active Baby"])
    },
    "Cadbury": {
        "Oreo": ("Food", "Biscuits", ["Chocolate Creme", "Vanilla Creme"]),
        "5 Star": ("Food", "Chocolate", ["Classic", "Caramel"])
    }
}

rows = []
psku_id_counter = 1001
sku_id_counter = 5001

for brand, subbrands in products.items():
    for sub_brand, (category, sub_category, pskus) in subbrands.items():
        for psku in pskus:
            psku_id = f"PSKU{psku_id_counter}"
            psku_id_counter += 1

            for sku, price in extended_skus.items():
                rows.append([
                    brand,
                    sub_brand,
                    category,
                    sub_category,
                    psku,
                    sku,
                    psku_id,
                    f"SKU{sku_id_counter}",
                    price
                ])
                sku_id_counter += 1

columns = [
    "brand", "sub_brand", "category", "sub_category",
    "PSKU", "SKU", "PSKU_id", "SKU_id", "unit_price"
]

product_table = pd.DataFrame(rows, columns=columns)

print("Rows:", product_table.shape[0])
print("Columns:", product_table.shape[1])
print(product_table.head(10))

product_table.to_csv(
    "product_master_table.csv",
    index=False
)

print("CSV file created successfully: product_master_table.csv")


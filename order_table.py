import pandas as pd
import random
store_ids = [
    "STORE_001","STORE_002","STORE_003","STORE_004","STORE_005",
    "STORE_006","STORE_007","STORE_008","STORE_009","STORE_010",
    "STORE_011","STORE_012","STORE_013","STORE_014","STORE_015",
    "STORE_016","STORE_017","STORE_018","STORE_019","STORE_020",
    "STORE_021"]
sku_ids = [f"SKU_{str(i).zfill(4)}" for i in range(1, 131)]     # 130 SKUs
psku_ids = [f"PSKU_{str(i).zfill(3)}" for i in range(1, 27)]   # 26 PSKUs
transaction_ids = [f"TXN_{str(i).zfill(6)}" for i in range(1, 301)]  # duplicates allowed
num_orders = 10000
GST_RATE = 0.18  # 18% GST
order_data = []
for i in range(1, num_orders + 1):
    quantity = random.randint(1, 25)
    unit_price = random.randint(40, 400)  # realistic FMCG pricing
    order_amount = quantity * unit_price
    gst_amount = round(order_amount * GST_RATE, 2)
    total_amount = round(order_amount + gst_amount, 2)
    order_data.append({
        "order_id": f"ORD_{str(i).zfill(6)}",
        "transaction_id": random.choice(transaction_ids),
        "SKU_id": random.choice(sku_ids),
        "PSKU_id": random.choice(psku_ids),
        "store_id": random.choice(store_ids),"quantity": quantity,
        "order_date": random.choice(pd.date_range("2022-01-01", "2024-12-31")),
        "order_status": random.choice(["Placed", "Shipped", "Delivered", "Cancelled", "Returned"]),
        "order_amount": order_amount,
        "GST": gst_amount,"total_amount": total_amount})

order_df = pd.DataFrame(order_data)

assert order_df["order_id"].is_unique, "❌ order_id is not unique"
assert order_df["store_id"].isin(store_ids).all(), "❌ Invalid store_id found"
order_df.to_csv("order_table.csv", index=False)
print("✅ Order table created successfully")
print("📄 File exported as: order_table.csv")
print(order_df.head())

import pandas as pd
import random
from datetime import datetime

START_DATE = "2022-01-01"
END_DATE = "2024-12-31"
GST_RATE = 0.18

NUM_TRANSACTIONS = 5000  # you can increase if needed

store_ids = [f"STORE_{str(i).zfill(3)}" for i in range(1, 22)]
transaction_statuses = ["SUCCESS", "FAILED", "PENDING"]

date_range = pd.date_range(start=START_DATE, end=END_DATE, periods=NUM_TRANSACTIONS)

data = []

for i in range(NUM_TRANSACTIONS):
    quantity = random.randint(1, 10)
    unit_price = random.randint(50, 500)
    transaction_amount = quantity * unit_price
    gst_amount = round(transaction_amount * GST_RATE, 2)
    net_amount = round(transaction_amount + gst_amount, 2)
    data.append({
        "transaction_id": f"TXN_{str(i+1).zfill(6)}",
        "store_id": random.choice(store_ids),
        "transaction_date": date_range[i].date(),
        "order_id": f"ORD_{str(random.randint(1, 2000)).zfill(6)}",
        "transaction_status": random.choice(transaction_statuses),
        "quantity": quantity,
        "transaction_amount": transaction_amount,
        "GST": gst_amount,
        "net_amount": net_amount
    })

transaction_df = pd.DataFrame(data)
transaction_df = transaction_df.sort_values("transaction_date").reset_index(drop=True)
transaction_df.to_csv("transaction_table.csv", index=False)
print(transaction_df.head())
print("\nTotal Transactions:", len(transaction_df))

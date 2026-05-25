import pandas as pd
import random

random.seed(42)

store_types = [
    "hypermarket",
    "supermarket",
    "large",
    "medium",
    "small",
    "mobile"
]

store_ids = [f"STORE_{i:03d}" for i in range(1, 22)]

store_type_assigned = random.choices(store_types, k=21)

store_df = pd.DataFrame({
    "store_id": store_ids,
    "store_type": store_type_assigned
})

print(store_df)

store_df.to_csv("store_table.csv", index=False)

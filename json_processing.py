import pandas as pd
import json

# Step 1
with open("sample.json", "r") as file:
    data = json.load(file)

# Step 2
df_orders = pd.json_normalize(data, record_path=['orders'], meta=['customer_id', 'name', 'email'], sep='.')
order_totals = dict(zip(df_orders['order_id'], df_orders['total']))
print(order_totals)

# Step 3
df = pd.json_normalize(data,record_path=['orders', 'items'], meta=[['orders', 'order_id'], ['orders', 'total'], 'customer_id', 'name', 'email'], sep='.')

# Step 4
df.to_json("processed_orders.json", orient="records", indent=4)

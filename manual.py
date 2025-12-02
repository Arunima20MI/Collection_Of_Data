
import pandas as pd
data = {
    "Name": ["Ananya", "Smita", "Rahul"],
    "Age": [15, 20, 18],
    "Marks": [88, 76, 92]
}

df_manual = pd.DataFrame(data)

df_manual.to_csv("manual_data.csv", index=False)
print("manual_data.csv created")

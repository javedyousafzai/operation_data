import pandas as pd

# Load your file
df = pd.read_csv("partner2.csv", encoding="utf-8")

# Add sequence number per partner_id
df["seq"] = df.groupby("partner_id").cumcount() + 1

# Pivot to wide format
df_wide = df.pivot(index="partner_id", columns="seq", values="partner_name")

# Rename columns
df_wide.columns = [f"partner_{col}" for col in df_wide.columns]

# Reset index
df_wide = df_wide.reset_index()

# Save result
df_wide.to_csv("partners_pivoted.csv", index=False, encoding="utf-8")

print("Done. Output saved as partners_pivoted.csv")

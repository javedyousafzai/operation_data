import pandas as pd

input_file = "concatenated_partners.csv"
output_file = "partners_split.csv"

# Try reading with utf-8 first, fallback to latin-1 if needed
try:
    df = pd.read_csv(input_file, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(input_file, encoding="latin-1")

# Ensure column names are correct (strip accidental spaces)
df.columns = df.columns.str.strip()

# Split partner_name column on '|'
df["partner_name"] = df["partner_name"].fillna("").astype(str)
df["partner_name"] = df["partner_name"].str.split("|")

# Explode into separate rows
df_exploded = df.explode("partner_name")

# Clean whitespace around names
df_exploded["partner_name"] = df_exploded["partner_name"].str.strip()

# Remove empty partner names (if any)
df_exploded = df_exploded[df_exploded["partner_name"] != ""]

# Keep only required columns (optional, if other columns exist)
df_exploded = df_exploded[["document_id", "partner_name"]]

# Save result
df_exploded.to_csv(output_file, index=False, encoding="utf-8")

print("Done. Output saved to:", output_file)

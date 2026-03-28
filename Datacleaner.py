import pandas as pd

df = pd.read_csv("raw_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df.fillna("N/A", inplace=True)

# Normalize text
df['name'] = df['name'].str.title()

# Basic AI logic (example)
def clean_text(text):
    return text.strip().lower()

df['description'] = df['description'].apply(clean_text)

df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned successfully!")

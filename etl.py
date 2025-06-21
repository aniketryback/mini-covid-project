import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv"
    df = pd.read_csv(url)
    print("✅ Data loaded")
    print(f"Total rows: {len(df)}")
    return df

def clean_data(df):
    columns = ['location', 'total_cases', 'total_deaths', 'people_vaccinated']
    df = df[columns]
    df_cleaned = df.dropna()
    print(f"✅ Cleaned data — rows after cleaning: {len(df_cleaned)}")
    return df_cleaned

def save_csv(df, filename):
    os.makedirs("output", exist_ok=True)
    df.to_csv(f"output/{filename}", index=False)
    print(f"✅ Saved to output/{filename}")

def filter_vaccinated(df):
    filtered = df[df['people_vaccinated'] > 10_000_000]
    print(f"✅ Filtered countries with >10M vaccinated: {len(filtered)}")
    return filtered

def plot_top_10(df):
    top_10 = df.sort_values(by='people_vaccinated', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    plt.barh(top_10['location'], top_10['people_vaccinated'], color='skyblue')
    plt.xlabel("People Vaccinated")
    plt.ylabel("Country")
    plt.title("Top 10 Countries by Vaccination")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("output/top10_vaccinated.png")
    print("✅ Bar chart saved to output/top10_vaccinated.png")

# ---- Main ETL Flow ---- #
if __name__ == "__main__":
    df = load_data()
    cleaned_df = clean_data(df)
    save_csv(cleaned_df, "covid_cleaned.csv")

    filtered_df = filter_vaccinated(cleaned_df)
    save_csv(filtered_df, "vaccinated_over_10m.csv")

    plot_top_10(filtered_df)

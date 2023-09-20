import polars as pl
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data using polars and return a DataFrame."""
    return pl.read_csv(file_path)

def plot_country_trend(df, country):
    """Plot the trend for a given country."""
    country_df = df.filter(df["Entity"] == country).sort("Year")
    plt.plot(country_df["Year"].to_list(), country_df["Cost of a healthy diet"].to_list(), label=country)

def highest_cost_country_each_year(df):
    """Returns a DataFrame with the country having the highest cost each year."""
    return df.groupby("Year").apply(lambda g: g.sort("Cost of a healthy diet", reverse=True).head(1)).select(["Year", "Entity", "Cost of a healthy diet"])

def plot_highest_cost_country_bar_chart(df):
    """Plot bar chart for the country with the highest cost each year."""
    highest_cost_df = highest_cost_country_each_year(df)
    years = highest_cost_df["Year"].to_list()
    countries = highest_cost_df["Entity"].to_list()
    costs = highest_cost_df["Cost of a healthy diet"].to_list()

    plt.bar(years, costs, color='skyblue')
    for i, v in enumerate(countries):
        plt.text(years[i], costs[i] + 0.1, v, ha='center', va='bottom', fontsize=9)
    plt.title("Country with Highest Cost of a Healthy Diet Each Year")
    plt.xlabel("Year")
    plt.ylabel("Cost")
    plt.tight_layout()

def plot_top_countries_pie_chart(df, year):
    """Plot pie chart for the distribution of costs for the top 5 countries for a given year."""
    latest_df = df.filter(df["Year"] == year).sort("Cost of a healthy diet", reverse=True).head(5)
    countries = latest_df["Entity"].to_list()
    costs = latest_df["Cost of a healthy diet"].to_list()

    plt.pie(costs, labels=countries, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title(f"Top 5 Countries with Highest Cost of a Healthy Diet in {year}")
    plt.tight_layout()

if __name__ == "__main__":
    data_path = "data.csv"
    df = load_data(data_path)
    
    plt.figure(figsize=(10, 6))
    
    # Line chart for China and United States
    plot_country_trend(df, "China")
    plot_country_trend(df, "United States")
    plt.title("Trend of Cost of a Healthy Diet for China and US")
    plt.xlabel("Year")
    plt.ylabel("Cost")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Bar chart for highest cost country each year
    plt.figure(figsize=(10, 6))
    plot_highest_cost_country_bar_chart(df)
    plt.show()

    # Pie chart for top 5 countries for the latest year
    latest_year = df["Year"].max().to_list()[0]
    plt.figure(figsize=(10, 6))
    plot_top_countries_pie_chart(df, latest_year)
    plt.show()

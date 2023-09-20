import polars as pl
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data using polars and return a DataFrame."""
    return pl.read_csv(file_path)

def calculate_average_cost_per_year(df):
    """Calculate the average cost of a healthy diet per year."""
    return df.groupby("Year").agg(pl.col("Cost of a healthy diet").mean().alias("Average Cost"))

def plot_average_cost_per_year(df):
    """Plot the average cost of a healthy diet per year."""
    years = df["Year"].to_list()
    avg_cost = df["Average Cost"].to_list()
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, avg_cost, marker='o', linestyle='-', color='b')
    plt.title("Average Cost of a Healthy Diet per Year")
    plt.xlabel("Year")
    plt.ylabel("Average Cost")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data_path = "data.csv"
    df = load_data(data_path)
    avg_cost_df = calculate_average_cost_per_year(df)
    print(avg_cost_df)
    plot_average_cost_per_year(avg_cost_df)

import polars as pl

def load_data(file_path):
    """Load data using polars and return a DataFrame."""
    return pl.read_csv(file_path)

def calculate_average_cost_per_year(df):
    """Calculate the average cost of a healthy diet per year."""
    return df.groupby("Year").agg(pl.col("Cost of a healthy diet").mean().alias("Average Cost"))

if __name__ == "__main__":
    data_path = "data.csv"
    df = load_data(data_path)
    avg_cost_df = calculate_average_cost_per_year(df)
    print(avg_cost_df)

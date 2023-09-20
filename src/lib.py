import polars as pl

def load_data_from_lib(file_path):
    """Load data using polars from the lib."""
    return pl.read_csv(file_path)

def calculate_average_cost_per_year_from_lib(df):
    """Calculate the average cost of a healthy diet per year from the lib."""
    return df.groupby("Year").agg(pl.col("Cost of a healthy diet").mean().alias("Average Cost"))

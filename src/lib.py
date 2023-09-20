import polars as pl

def read_data(file_path):
    return pl.read_csv(file_path)

def calculate_average_cost_by_country(df, country):
    return df.filter(df["Entity"] == country).select(pl.col("Cost of a healthy diet").mean().alias("Average Cost")).collect()[0]["Average Cost"][0]

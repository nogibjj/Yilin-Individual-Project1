import sys
sys.path.append('../src')
from script import load_data, calculate_average_cost_per_year
import polars as pl

def test_load_data():
    df = load_data("../data.csv")
    assert df.shape == (8, 4)
    assert df.columns == ["Entity", "Code", "Year", "Cost of a healthy diet"]

def test_calculate_average_cost_per_year():
    data = {
        "Entity": ["A", "A", "B", "B"],
        "Code": ["ALB", "ALB", "DZA", "DZA"],
        "Year": [2017, 2018, 2017, 2018],
        "Cost of a healthy diet": [3.9, 4.0, 3.7, 3.8]
    }
    df = pl.DataFrame(data)
    result = calculate_average_cost_per_year(df)
    assert result.shape == (2, 2)
    assert result.columns == ["Year", "Average Cost"]

import polars as pl
from src.lib import read_data, calculate_average_cost_by_country

def test_read_data():
    data = read_data("data.csv")
    assert isinstance(data, pl.DataFrame)
    assert data.shape == (7, 4)

def test_calculate_average_cost_by_country():
    data = read_data("data.csv")
    avg_cost_albania = calculate_average_cost_by_country(data, "Albania")
    avg_cost_algeria = calculate_average_cost_by_country(data, "Algeria")
    
    assert round(avg_cost_albania, 3) == 4.19
    assert round(avg_cost_algeria, 3) == 3.792

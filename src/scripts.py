from lib import read_data, calculate_average_cost_by_country

def main():
    data = read_data("data.csv")
    avg_cost_albania = calculate_average_cost_by_country(data, "Albania")
    avg_cost_algeria = calculate_average_cost_by_country(data, "Algeria")

    print(f"Average cost for a healthy diet in Albania: {avg_cost_albania}")
    print(f"Average cost for a healthy diet in Algeria: {avg_cost_algeria}")

if __name__ == "__main__":
    main()

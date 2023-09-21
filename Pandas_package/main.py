import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def descriptive_statistics(data):
    return data.describe()

def visualize_data(data):
    # Create a new figure with a specified size
    plt.figure(figsize=(10, 8))
    
    # Histogram for each column in data
    for column in data.columns:
        plt.hist(data[column], bins=30, alpha=0.5, label=column)
    
    plt.title("Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend(loc="upper right")
    plt.show()
    
    # Boxplot for each column in data
    data.boxplot()
    plt.title("Boxplot")
    plt.ylabel("Value")
    plt.show()

if __name__ == "__main__":
    data = load_data("data/data_sample.csv")
    print(descriptive_statistics(data))
    visualize_data(data)

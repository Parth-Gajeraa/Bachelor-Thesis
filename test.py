import numpy as np
import pandas as pd

def main():
    np.random.seed(42)
    
    data = np.random.randint(1, 101, size=(10, 3))
    
    df = pd.DataFrame(data, columns=['A', 'B', 'C'])
    print("Initial DataFrame:")
    print(df)
    
    df['D'] = df['A'] + df['B']
    print("\nDataFrame after adding column 'D' (A + B):")
    print(df)
    
    print("\nSummary statistics of the DataFrame:")
    print(df.describe())
    
    mean_c = np.mean(df['C'])
    print("\nMean of column 'C' computed using numpy:", mean_c)

if __name__ == "__main__":
    main()

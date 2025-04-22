from pyspark.sql import SparkSession

def main():
    # Create a SparkSession
    spark = SparkSession.builder \
        .appName("PySparkExample") \
        .getOrCreate()
    
    # Sample data: list of tuples (Name, Age)
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    columns = ["Name", "Age"]
    
    # Create a DataFrame using the sample data
    df = spark.createDataFrame(data, columns)
    print("Initial DataFrame:")
    df.show()
    
    # Filter the DataFrame for people with Age greater than 30
    df_filtered = df.filter(df.Age > 30)
    print("Filtered DataFrame (Age > 30):")
    df_filtered.show()
    
    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()

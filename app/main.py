from app.data.ingestion import load_csv
from app.data.inspection import (
    get_dataset_shape, 
    get_data_types, 
    get_missing_values, 
    get_duplicates, 
    get_descriptive_statistics)


def main():
    dataset = load_csv("datasets/sales.csv")
    print(dataset)

    print("\n--- DATASET DIMENSIONS ---")
    print(get_dataset_shape(dataset))

    print("\n--- DATASET TYPES ---")
    print(get_data_types(dataset))
    
    print("\n--- MISSING VALUES ---")
    print(get_missing_values(dataset))
    
    print("\n--- DUPLICATES ---")
    print(get_duplicates(dataset))

    print("\n--- DATASET DESCRIPTIVE STATISTICS ---")
    print(get_descriptive_statistics(dataset))
    


if __name__ == "__main__":
    main()
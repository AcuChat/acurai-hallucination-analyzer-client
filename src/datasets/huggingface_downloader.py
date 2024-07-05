import json
import argparse
from datasets import load_dataset

def save_hf_dataset_to_json(dataset_name, file_name):
    # Load the dataset from Hugging Face
    dataset = load_dataset(dataset_name)

    # Convert the dataset to a dictionary
    dataset_dict = {split: dataset[split].to_dict() for split in dataset}

    # Write the dataset dictionary to a JSON file
    with open(file_name, 'w') as f:
        json.dump(dataset_dict, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Download a Hugging Face dataset and save it as a JSON file.")
    parser.add_argument('dataset_name', type=str, help='The name of the Hugging Face dataset to download.')
    parser.add_argument('file_name', type=str, help='The name of the JSON file to save the dataset to.')

    args = parser.parse_args()

    save_hf_dataset_to_json(args.dataset_name, args.file_name)

if __name__ == "__main__":
    main()

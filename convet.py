import os
import pandas as pd

# Function to read and process text files, then save to a single CSV
def convert_text_to_csv(directory, output_csv):
    data = []  # List to hold data from all text files

    # Iterate through all files in the given directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Process only .txt files
            file_path = os.path.join(directory, filename)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the content of the text file
                content = file.read()

                # Append the data to the list
                data.append({"filename": filename, "content": content})

    # Convert the list to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)
    print(f"CSV file created successfully: {output_csv}")

# Example usage
directory = "/Desktop/ClinicalReadings/MCUCXR_0001_0.txt"
 # Replace with the directory containing your .txt files
output_csv = "output.csv"  # Replace with your desired CSV output path
convert_text_to_csv(directory, output_csv)

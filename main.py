import zipfile
import os
import gzip
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def un_zip():
    # Path to the uploaded zip file
    zip_file_path = r"C:\Users\Tymek\Desktop\_Reddit_Twitter_Data_Analysis\datasets\0819_UkraineCombinedTweetsDeduped" \
                    r".csv.gzip.zip"
    zip_file_path = zip_file_path.replace('\\', '/')
    # Unzipping the file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall("./")


def check_file_header(file_path):
    try:
        with open(file_path, 'rb') as file:
            header = file.read(4)
            file.seek(0, 2)  # Move the cursor to the end of the file
            size = file.tell()
        print("Header:", header)
        print("Size:", size, "bytes")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", e)


def un_gzip_file(gzip_file_path, output_file_path):
    # Decompress the gzip file
    with gzip.open(gzip_file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def gzip_to_dataframe(gzip_file_path):
    # Read the gzip file into a pandas dataframe
    df = pd.read_csv(gzip_file_path, compression='gzip', header=0, sep=',', quotechar='"')
    return df

file_gzip = "./datasets/0819_UkraineCombinedTweetsDeduped.csv.gzip"

df = gzip_to_dataframe(file_gzip)

# filter out non-English tweets

df = df[df["language"] == "en"]


# get number of rows
df_clean = pd.DataFrame(columns=["location", "text", "extractedts", "hashtags", "tweetid"])
# leave location, text, date , hashtags an id
df_clean = df[["location", "text", "extractedts", "hashtags", "tweetid"]]

#print(df_clean["text"].sample(10), df_clean.shape[0])

df_clean = df_clean.dropna()

print(df_clean.shape[0])

print(df_clean["location"].unique())

df_clean["location"] = df_clean["location"].str.lower()

# extractedts to datetime
df_clean["extractedts"] = pd.to_datetime(df_clean["extractedts"])



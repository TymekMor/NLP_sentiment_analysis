# NLP_sentiment_analysis
Analysis of public sentiment towards war in Ukraine in years 2022-2023, based on twitter dataset-sentiment analysis. Using pre-trained and fine tuned NLP models.

# sentimental_analysis_textblob.ipynb
This Python script conducts sentiment analysis on a dataset of tweets related to the Ukraine War using the TextBlob library. It preprocesses the data, extracts sentiment scores (polarity and subjectivity), and saves the processed results in batches. The code facilitates the exploration of sentiment trends within the dataset for understanding public sentiment during the specified period.

# Concatenation.ipynb 
This Python script consolidates sentiment analysis results calculated in chunks, concatenates them into a single DataFrame, and writes the combined data to a Parquet file. The data is sorted chronologically based on the 'extractedts' timestamp, and the resulting file covers a period of 30 days. This consolidation simplifies further analysis and visualization of sentiment trends over the specified time frame.

# Plots.ipynb 
This Python script utilizes Matplotlib and Seaborn to generate insightful plots based on sentiment analysis results from a large dataset of tweets. The visualizations include histograms of polarity and subjectivity values, the number of tweets per hour, tweets per day over time, and polarity/subjectivity trends over time. Additionally, it creates a composite plot showcasing normalized polarity, subjectivity, and tweet count over time. The script provides key statistics, such as the total number of tweets, the period covered, and correlations between sentiment metrics. The analysis offers a comprehensive overview of sentiment dynamics in the dataset.

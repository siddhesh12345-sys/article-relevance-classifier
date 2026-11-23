# Article Relevance Classifier

## Project Overview
The Article Relevance Classifier is a Python-based application that identifies whether news and blog articles are relevant or irrelevant to the film, television, streaming, and OTT industry.

## Features
- Extracts article content from URLs.
- Classifies articles as Relevant or Irrelevant.
- Uses predefined keywords and rules for classification.
- Generates CSV files containing classification results.
- Displays results through an interactive Streamlit dashboard.
- Allows users to upload CSV files and view classification results.

## Technologies Used
- Python
- Streamlit
- Pandas
- HTML Parsing
- CSV

## Project Files
- `app.py` – Streamlit dashboard.
- `article_classifier.py` – Article classification logic.
- `urls.txt` – Input article URLs.
- `result.csv` – Classification output.
- `requirements.txt` – Python dependencies.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the classifier:

```bash
python article_classifier.py --file urls.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to access the dashboard.

## Purpose
This project helps automate the process of identifying industry-related articles and organizing their results for easier analysis.
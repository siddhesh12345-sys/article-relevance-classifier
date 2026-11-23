
import streamlit as st
import pandas as pd
from pathlib import Path

# Page settings
st.set_page_config(
    page_title="Article Classifier",
    page_icon="📰",
    layout="wide"
)

st.title("📰 Article Relevance Classifier")
st.caption("Film | Television | OTT | Streaming")

# Load existing CSV
csv_path = Path(__file__).parent / "results.csv"

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV",
    type=["csv"]
)

try:
    if uploaded_file:
        df = pd.read_csv(uploaded_file, encoding="utf-8-sig")
    elif csv_path.exists():
        df = pd.read_csv(csv_path, encoding="utf-8-sig")
    else:
        st.error("results.csv not found. Run your classifier first.")
        st.stop()

except Exception as e:
    st.error(f"Error reading CSV: {e}")
    st.stop()

if df.empty:
    st.warning("No article results found.")
    st.stop()

# Find classification column
possible_columns = [
    "Relevant / Irrelevant",
    "Classification",
    "Label"
]

classification_col = next(
    (c for c in possible_columns if c in df.columns),
    None
)

if classification_col is None:
    st.error("Classification column not found in CSV.")
    st.write("Available columns:", list(df.columns))
    st.stop()

# Calculate totals
labels = df[classification_col].fillna("").astype(str).str.lower()

relevant = labels.eq("relevant")
irrelevant = labels.eq("irrelevant")

total = len(df)
relevant_count = int(relevant.sum())
irrelevant_count = int(irrelevant.sum())

# Dashboard metrics
st.subheader("Classification Summary")

c1, c2, c3 = st.columns(3)

c1.metric("Total Articles", total)
c2.metric("Relevant", relevant_count)
c3.metric("Irrelevant", irrelevant_count)

st.divider()

# Search and filters
st.subheader("Explore Articles")

search = st.text_input("Search by article URL or text")

filter_option = st.selectbox(
    "Filter articles",
    ["All", "Relevant", "Irrelevant"]
)

filtered_df = df.copy()

if filter_option == "Relevant":
    filtered_df = filtered_df[
        filtered_df[classification_col].astype(str).str.lower() == "relevant"
    ]

elif filter_option == "Irrelevant":
    filtered_df = filtered_df[
        filtered_df[classification_col].astype(str).str.lower() == "irrelevant"
    ]

if search:
    matches = filtered_df.astype(str).apply(
        lambda col: col.str.contains(
            search, case=False, na=False
        )
    ).any(axis=1)

    filtered_df = filtered_df[matches]

st.write(f"Showing {len(filtered_df)} articles")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# Download filtered results
st.download_button(
    "Download Results CSV",
    data=filtered_df.to_csv(index=False).encode("utf-8-sig"),
    file_name="filtered_results.csv",
    mime="text/csv"
)

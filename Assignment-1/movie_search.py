import pandas as pd
from sentence_transformers import SentenceTransformer, util
import os
import sys


# -----------------------------
# Load dataset safely
# -----------------------------
def load_movies_csv(filename="movies.csv"):
    """
    Load movies.csv from the same directory as this script.
    Returns:
        pd.DataFrame: DataFrame containing the movie data
    Raises:
        FileNotFoundError: If the CSV file is missing
        pd.errors.EmptyDataError: If the CSV file is empty
        pd.errors.ParserError: If the CSV file is malformed
    """
    try:
        csv_path = os.path.join(os.path.dirname(__file__), filename)
        df = pd.read_csv(csv_path)

        if "plot" not in df.columns:
            raise ValueError("CSV file must contain a 'plot' column.")

        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found in {os.path.dirname(__file__)}")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        sys.exit(1)
    except pd.errors.ParserError:
        print("Error: The CSV file is malformed.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error while loading CSV: {e}")
        sys.exit(1)


# -----------------------------
# Load model safely
# -----------------------------
def load_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Load the SentenceTransformer model.
    Returns:
        SentenceTransformer object
    Raises:
        Exception if model fails to load
    """
    try:
        return SentenceTransformer(model_name)
    except Exception as e:
        print(f"Error loading model '{model_name}': {e}")
        sys.exit(1)


# -----------------------------
# Search function
# -----------------------------
def search_movies(query, top_n=5):
    """
    Search movies by semantic similarity of plot descriptions.

    Args:
        query (str): Search query text
        top_n (int): Number of top results to return

    Returns:
        pd.DataFrame: DataFrame of top matching movies with similarity scores
    """
    try:
        if not query.strip():
            raise ValueError("Query cannot be empty.")

        # Encode query
        q_emb = model.encode([query], convert_to_numpy=True, normalize_embeddings=True)

        # Compute cosine similarities
        sims = util.cos_sim(q_emb, embeddings).cpu().numpy().flatten()

        # Get top N indices
        idx = sims.argsort()[::-1][:top_n]

        return df.iloc[idx].assign(similarity=sims[idx])

    except Exception as e:
        print(f"Error during search: {e}")
        return pd.DataFrame()


# -----------------------------
# Main setup
# -----------------------------
df = load_movies_csv()
model = load_model()
embeddings = model.encode(
    df["plot"].tolist(),
    convert_to_numpy=True,
    normalize_embeddings=True
)

# Example usage
if __name__ == "__main__":
    results = search_movies("space adventure with aliens", top_n=5)
    print(results)


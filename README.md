# movie-search-assignment 🎬

This project implements a semantic search engine for movie plots. Instead of relying on simple keyword matching, it uses **sentence embeddings** to understand the contextual meaning of your search query. This enables you to find movies using natural language descriptions, even if the exact words don't appear in the plot summary.



---

## 📂 Project Structure

The repository is organized as follows:

```
.
├── movie_search.py         # Core script implementing the search logic
├── movies.csv              # Sample dataset with movie titles and plots
├── requirements.txt        # Project dependencies
├── solution.ipynb          # Interactive Jupyter Notebook for demonstration
└── tests/
    └── test_movie_search.py  # Unit tests for the search functionality
```

---

## 🚀 Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* Python 3.8+
* `pip` package manager

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/movie-semantic-search.git](https://github.com/your-username/movie-semantic-search.git)
    cd movie-semantic-search
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🤖 How to Use

### 1. Explore in Jupyter Notebook

The easiest way to see the project in action is to run the `solution.ipynb` notebook, which walks through the entire workflow with examples and explanations.

```bash
jupyter notebook solution.ipynb
```

### 2. Use the Search Function

You can import and use the core search function `search_movies()` in your own Python scripts. The function takes a natural language `query` and the desired number of results `top_n` as input.

```python
from movie_search import search_movies

# Define your search query
query = "a sci-fi adventure with aliens"

# Get the top 5 most relevant movies
results = search_movies(query, top_n=5)

# Print the results
print(results)
```

The function returns a **pandas DataFrame** containing the `Movie Title`, `Plot Description`, and a `Similarity Score` that indicates how closely each movie matches your query.

---

## ✅ Running Tests

To ensure that everything is working correctly, you can run the unit tests from the root directory of the project:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 🛠️ Dependencies

This project relies on the following major libraries:

* **pandas**: For data manipulation and handling the CSV dataset.
* **sentence-transformers**: For generating sentence embeddings.
* **scikit-learn**: For calculating cosine similarity.
* **torch**: As a backend for the sentence transformer models.

---

## 📝 Notes

This project is intended for learning and demonstration purposes. The sample `movies.csv` is a small subset, but the search logic can be scaled to much larger datasets.

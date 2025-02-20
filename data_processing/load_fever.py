"""
LOAD FEVER DATA
"""

# Load dataset from Hugging Face
fever_dataset = load_dataset("fever/fever", 'v2.0')

# Convert to DataFrame for easy access

df_fever = pd.DataFrame(fever_dataset['validation'])

# 1. Convert DataFrame text to embeddings
fever_embeddings = model.encode(df_fever['claim'].tolist(), convert_to_numpy=True)

# 2. Create FAISS index
dim_fever = fever_embeddings.shape[1]  # Embedding dimension
index_fever = faiss.IndexFlatL2(dim_fever)  # Using L2 distance for simplicity

# Add embeddings to FAISS index
index_fever.add(fever_embeddings)

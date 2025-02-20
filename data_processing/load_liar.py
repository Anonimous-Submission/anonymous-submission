"""
LOAD LIAR DATA
"""

# Load dataset from Hugging Face
liar_dataset = load_dataset("liar", trust_remote_code=True)

# Convert to DataFrame for easy access

df_liar = pd.DataFrame(liar_dataset["train"])

# 1. Convert DataFrame text to embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings_liar = model.encode(df_liar['statement'].tolist(), convert_to_numpy=True)

# 2. Create FAISS index
dim_liar = embeddings_liar.shape[1]  # Embedding dimension
index_liar = faiss.IndexFlatL2(dim_liar)  # Using L2 distance for simplicity

# Add embeddings to FAISS index
index_liar.add(embeddings_liar)

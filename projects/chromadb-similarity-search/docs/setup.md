# ChromaDB Similarity Search - Setup Guide

## 🚀 Quick Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/assadAllah630/ai-engineering-portfolio.git
   cd ai-engineering-portfolio/projects/chromadb-similarity-search
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation**
   ```bash
   python -c "import chromadb; print('ChromaDB installed successfully!')"
   python -c "import sentence_transformers; print('SentenceTransformers installed successfully!')"
   ```

## 🧪 Running the Examples

### Book Similarity Search
```bash
python books_advanced_search.py
```

**Expected Output:**
- Collection creation confirmation
- Book data insertion
- Similarity search results for magical fantasy adventures
- Metadata filtering by genre and rating
- Combined search results

### Employee Similarity Search
```bash
python similarity_employeedata.py
```

**Expected Output:**
- Collection creation confirmation
- Employee data insertion
- Python developer search results
- Leadership role search results
- Department and experience filtering
- Combined search with location filters

## 🔧 Configuration Options

### Embedding Model
The project uses `all-MiniLM-L6-v2` by default. You can change this in both Python files:

```python
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"  # Change this to use different models
)
```

### Distance Metric
Currently using cosine similarity. Can be changed in collection configuration:

```python
configuration={
    "hnsw": {"space": "cosine"},  # Options: "cosine", "l2", "ip"
    "embedding_function": ef
}
```

### Collection Persistence
By default, collections are in-memory. For persistence, modify the client:

```python
# For persistent storage
client = chromadb.PersistentClient(path="./chroma_db")

# For in-memory (current setup)
client = chromadb.Client()
```

## 🐛 Troubleshooting

### Common Issues

1. **Import Error: No module named 'chromadb'**
   ```bash
   pip install chromadb==1.0.12
   ```

2. **Import Error: No module named 'sentence_transformers'**
   ```bash
   pip install sentence-transformers==4.1.0
   ```

3. **Memory Issues with Large Datasets**
   - Reduce `n_results` in queries
   - Use smaller embedding models
   - Implement pagination

4. **Slow Performance**
   - Use GPU if available: `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`
   - Consider using smaller embedding models
   - Optimize collection configuration

### Performance Optimization

1. **GPU Acceleration**
   ```bash
   # Install PyTorch with CUDA support
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

2. **Batch Processing**
   ```python
   # Process documents in batches
   batch_size = 100
   for i in range(0, len(documents), batch_size):
       batch = documents[i:i+batch_size]
       collection.add(documents=batch, ...)
   ```

3. **Index Optimization**
   ```python
   configuration={
       "hnsw": {
           "space": "cosine",
           "m": 16,  # Number of connections per layer
           "ef_construction": 200  # Higher values = better accuracy, slower build
       }
   }
   ```

## 📊 Monitoring and Logging

### Enable Debug Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Performance Metrics
```python
import time

start_time = time.time()
results = collection.query(query_texts=["your query"], n_results=5)
end_time = time.time()

print(f"Query took {end_time - start_time:.4f} seconds")
```

## 🔒 Security Considerations

1. **API Keys**: Store sensitive data in environment variables
2. **Data Privacy**: Ensure compliance with data protection regulations
3. **Access Control**: Implement proper authentication for production use
4. **Data Validation**: Validate input data before processing

## 🚀 Production Deployment

### Docker Setup
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "books_advanced_search.py"]
```

### Environment Variables
```bash
export CHROMA_DB_PATH="./data"
export EMBEDDING_MODEL="all-MiniLM-L6-v2"
export MAX_RESULTS=100
```

## 📚 Additional Resources

- [ChromaDB Documentation](https://docs.trychroma.com/)
- [SentenceTransformers Documentation](https://www.sbert.net/)
- [Vector Database Best Practices](https://docs.trychroma.com/guides/best-practices)

## 🤝 Support

For issues and questions:
1. Check the troubleshooting section above
2. Review ChromaDB documentation
3. Create an issue in the repository
4. Contact: assadAllah630@github.com
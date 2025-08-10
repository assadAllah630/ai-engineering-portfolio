# ChromaDB Similarity Search Project

## 🎯 Project Overview

This project demonstrates advanced similarity search capabilities using ChromaDB, a powerful vector database for AI applications. The project showcases two main use cases:

1. **Book Similarity Search** - Advanced book recommendation system with metadata filtering
2. **Employee Data Similarity Search** - HR talent matching and skill-based search

## 🚀 Features

### Book Similarity Search (`books_advanced_search.py`)
- **Semantic Search**: Find books based on themes, descriptions, and content
- **Metadata Filtering**: Filter by genre, rating, year, and other attributes
- **Combined Search**: Semantic + metadata filtering for precise results
- **Comprehensive Dataset**: 8 classic books with rich metadata

### Employee Similarity Search (`similarity_employeedata.py`)
- **Skill-Based Matching**: Find employees by skills and experience
- **Department Filtering**: Filter by department, location, experience level
- **Advanced Queries**: Complex search with multiple criteria
- **HR Analytics**: Talent matching and recruitment insights

## 🛠️ Technology Stack

- **ChromaDB**: Vector database for similarity search
- **SentenceTransformers**: Text embedding generation
- **Python**: Core programming language
- **all-MiniLM-L6-v2**: Efficient embedding model

## 📋 Requirements

```bash
chromadb==1.0.12
sentence-transformers==4.1.0
```

## 🏃‍♂️ Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Book Search**:
   ```bash
   python books_advanced_search.py
   ```

3. **Run Employee Search**:
   ```bash
   python similarity_employeedata.py
   ```

## 📊 Search Examples

### Book Search Features
- Find magical fantasy adventures
- Filter by genre (Fantasy, Science Fiction)
- Find highly-rated books (4.3+ stars)
- Combined search: dystopian themes with high ratings

### Employee Search Features
- Find Python developers with web experience
- Search for leadership and management roles
- Filter by department (Engineering, Marketing, HR)
- Find senior employees (10+ years experience)
- Location-based filtering (California cities)

## 🎨 Key Features

### Semantic Understanding
- Uses advanced embedding models for semantic search
- Understands context and meaning, not just keywords
- Supports natural language queries

### Metadata Filtering
- Filter by any metadata attribute
- Complex queries with AND/OR logic
- Range-based filtering (experience, ratings, years)

### Combined Search
- Semantic similarity + metadata filtering
- Precise results with multiple criteria
- Real-world application scenarios

## 📁 Project Structure

```
chromadb-similarity-search/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── books_advanced_search.py  # Book similarity search
├── similarity_employeedata.py # Employee data search
├── examples/                 # Usage examples
│   ├── book_queries.py      # Book search examples
│   └── employee_queries.py  # Employee search examples
└── docs/                    # Documentation
    ├── setup.md             # Setup instructions
    └── api_reference.md     # API documentation
```

## 🔧 Configuration

### Embedding Model
- **Model**: `all-MiniLM-L6-v2`
- **Dimensions**: 384
- **Distance Metric**: Cosine similarity
- **Performance**: Fast and efficient for production use

### Database Configuration
- **Collection Type**: In-memory (for demo)
- **Persistence**: Can be configured for disk storage
- **Indexing**: HNSW (Hierarchical Navigable Small World)

## 🎯 Use Cases

### For Book Recommendations
- E-commerce book stores
- Library management systems
- Reading recommendation engines
- Content discovery platforms

### For HR & Recruitment
- Talent matching systems
- Skill-based candidate search
- Team composition analysis
- Career development recommendations

## 🚀 Performance

- **Search Speed**: Sub-second response times
- **Accuracy**: High semantic similarity matching
- **Scalability**: Handles thousands of documents efficiently
- **Memory Usage**: Optimized for production environments

## 🔍 Advanced Features

### Query Types Supported
- **Semantic Search**: Natural language queries
- **Metadata Filtering**: Structured data queries
- **Combined Search**: Hybrid approach
- **Range Queries**: Numeric range filtering
- **Multi-value Filtering**: IN clauses for categories

### Customization Options
- Custom embedding models
- Different distance metrics
- Collection-specific configurations
- Metadata schema design

## 📈 Future Enhancements

- [ ] Web interface for interactive search
- [ ] Real-time data updates
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] API endpoints for integration
- [ ] Docker containerization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 👨‍💻 Author

**Assad Allah Alebrahim**
- AI Engineer & Business Intelligence Analyst
- 5+ years experience in database optimization and AI automation
- Specialized in RAG systems and vector databases

---

*This project demonstrates advanced ChromaDB capabilities for real-world similarity search applications.*
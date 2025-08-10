# Example Book Queries for ChromaDB Similarity Search
# This file demonstrates various query patterns for the book collection

import chromadb
from chromadb.utils import embedding_functions

def setup_book_collection():
    """Setup the book collection with sample data"""
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    client = chromadb.Client()
    collection = client.create_collection(
        name="example_book_collection",
        metadata={"description": "Example book collection for queries"},
        configuration={
            "hnsw": {"space": "cosine"},
            "embedding_function": ef
        }
    )
    
    # Sample book data
    books = [
        {
            "id": "book_1",
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "genre": "Classic",
            "year": 1925,
            "rating": 4.1,
            "pages": 180,
            "description": "A tragic tale of wealth, love, and the American Dream in the Jazz Age",
            "themes": "wealth, corruption, American Dream, social class",
            "setting": "New York, 1920s"
        },
        {
            "id": "book_2",
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "genre": "Classic",
            "year": 1960,
            "rating": 4.3,
            "pages": 376,
            "description": "A powerful story of racial injustice and moral growth in the American South",
            "themes": "racism, justice, moral courage, childhood innocence",
            "setting": "Alabama, 1930s"
        },
        {
            "id": "book_3",
            "title": "1984",
            "author": "George Orwell",
            "genre": "Dystopian",
            "year": 1949,
            "rating": 4.4,
            "pages": 328,
            "description": "A chilling vision of totalitarian control and surveillance society",
            "themes": "totalitarianism, surveillance, freedom, truth",
            "setting": "Oceania, dystopian future"
        },
        {
            "id": "book_4",
            "title": "Harry Potter and the Philosopher's Stone",
            "author": "J.K. Rowling",
            "genre": "Fantasy",
            "year": 1997,
            "rating": 4.5,
            "pages": 223,
            "description": "A young wizard discovers his magical heritage and begins his education at Hogwarts",
            "themes": "friendship, courage, good vs evil, coming of age",
            "setting": "England, magical world"
        },
        {
            "id": "book_5",
            "title": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
            "genre": "Fantasy",
            "year": 1954,
            "rating": 4.5,
            "pages": 1216,
            "description": "An epic fantasy quest to destroy a powerful ring and save Middle-earth",
            "themes": "heroism, friendship, good vs evil, power corruption",
            "setting": "Middle-earth, fantasy realm"
        }
    ]
    
    # Create documents for embedding
    book_documents = []
    for book in books:
        document = f"{book['title']} by {book['author']}. {book['description']} "
        document += f"Themes: {book['themes']}. Setting: {book['setting']}. "
        document += f"Genre: {book['genre']} published in {book['year']}."
        book_documents.append(document)
    
    # Add to collection
    collection.add(
        ids=[book["id"] for book in books],
        documents=book_documents,
        metadatas=[{
            "title": book["title"],
            "author": book["author"],
            "genre": book["genre"],
            "year": book["year"],
            "rating": book["rating"],
            "pages": book["pages"]
        } for book in books]
    )
    
    return collection

def example_queries():
    """Demonstrate various query patterns"""
    collection = setup_book_collection()
    
    print("=== Book Query Examples ===\n")
    
    # 1. Semantic search for magical themes
    print("1. Finding books with magical themes:")
    results = collection.query(
        query_texts=["magical fantasy adventure with friendship and courage"],
        n_results=3
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['title']} by {metadata['author']} - Distance: {distance:.4f}")
    
    print("\n" + "="*50 + "\n")
    
    # 2. Search for classic literature
    print("2. Finding classic literature:")
    results = collection.query(
        query_texts=["classic American literature social themes"],
        n_results=3
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['title']} by {metadata['author']} - Distance: {distance:.4f}")
    
    print("\n" + "="*50 + "\n")
    
    # 3. Metadata filtering by genre
    print("3. Filtering by genre (Fantasy):")
    results = collection.get(
        where={"genre": "Fantasy"}
    )
    for i, doc_id in enumerate(results['ids']):
        metadata = results['metadatas'][i]
        print(f"  - {metadata['title']}: {metadata['genre']} ({metadata['rating']}★)")
    
    print("\n" + "="*50 + "\n")
    
    # 4. Filter by rating range
    print("4. Finding highly-rated books (4.3+):")
    results = collection.get(
        where={"rating": {"$gte": 4.3}}
    )
    for i, doc_id in enumerate(results['ids']):
        metadata = results['metadatas'][i]
        print(f"  - {metadata['title']}: {metadata['rating']}★")
    
    print("\n" + "="*50 + "\n")
    
    # 5. Combined search: dystopian themes with high ratings
    print("5. Finding highly-rated dystopian books:")
    results = collection.query(
        query_texts=["dystopian society control oppression future"],
        n_results=3,
        where={"rating": {"$gte": 4.0}}
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['title']} ({metadata['year']}) - {metadata['rating']}★")
        print(f"     Distance: {distance:.4f}")
    
    print("\n" + "="*50 + "\n")
    
    # 6. Search by author style
    print("6. Finding books by writing style (epic fantasy):")
    results = collection.query(
        query_texts=["epic fantasy quest adventure heroism"],
        n_results=2
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['title']} by {metadata['author']} - Distance: {distance:.4f}")
    
    print("\n" + "="*50 + "\n")
    
    # 7. Complex metadata filtering
    print("7. Finding classic books with high ratings:")
    results = collection.get(
        where={
            "$and": [
                {"genre": "Classic"},
                {"rating": {"$gte": 4.2}}
            ]
        }
    )
    for i, doc_id in enumerate(results['ids']):
        metadata = results['metadatas'][i]
        print(f"  - {metadata['title']}: {metadata['genre']} ({metadata['rating']}★)")

def advanced_queries():
    """Demonstrate more advanced query patterns"""
    collection = setup_book_collection()
    
    print("=== Advanced Book Query Examples ===\n")
    
    # 1. Multi-criteria search
    print("1. Finding fantasy books published after 1950:")
    results = collection.query(
        query_texts=["magical adventure fantasy world"],
        n_results=3,
        where={
            "$and": [
                {"genre": "Fantasy"},
                {"year": {"$gte": 1950}}
            ]
        }
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['title']} ({metadata['year']}) - Distance: {distance:.4f}")
    
    print("\n" + "="*50 + "\n")
    
    # 2. Range-based search
    print("2. Finding books with 200-400 pages:")
    results = collection.get(
        where={"pages": {"$gte": 200, "$lte": 400}}
    )
    for i, doc_id in enumerate(results['ids']):
        metadata = results['metadatas'][i]
        print(f"  - {metadata['title']}: {metadata['pages']} pages")
    
    print("\n" + "="*50 + "\n")
    
    # 3. Semantic search with specific themes
    print("3. Finding books about social justice:")
    results = collection.query(
        query_texts=["social justice racial equality moral courage"],
        n_results=2
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['title']} by {metadata['author']} - Distance: {distance:.4f}")

if __name__ == "__main__":
    print("Running basic query examples...")
    example_queries()
    
    print("\n" + "="*60 + "\n")
    
    print("Running advanced query examples...")
    advanced_queries()
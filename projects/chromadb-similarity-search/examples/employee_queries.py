# Example Employee Queries for ChromaDB Similarity Search
# This file demonstrates various query patterns for the employee collection

import chromadb
from chromadb.utils import embedding_functions

def setup_employee_collection():
    """Setup the employee collection with sample data"""
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    client = chromadb.Client()
    collection = client.create_collection(
        name="example_employee_collection",
        metadata={"description": "Example employee collection for queries"},
        configuration={
            "hnsw": {"space": "cosine"},
            "embedding_function": ef
        }
    )
    
    # Sample employee data
    employees = [
        {
            "id": "employee_1",
            "name": "John Doe",
            "experience": 5,
            "department": "Engineering",
            "role": "Software Engineer",
            "skills": "Python, JavaScript, React, Node.js, databases",
            "location": "New York",
            "employment_type": "Full-time"
        },
        {
            "id": "employee_2",
            "name": "Jane Smith",
            "experience": 8,
            "department": "Marketing",
            "role": "Marketing Manager",
            "skills": "Digital marketing, SEO, content strategy, analytics, social media",
            "location": "Los Angeles",
            "employment_type": "Full-time"
        },
        {
            "id": "employee_3",
            "name": "Alice Johnson",
            "experience": 3,
            "department": "HR",
            "role": "HR Coordinator",
            "skills": "Recruitment, employee relations, HR policies, training programs",
            "location": "Chicago",
            "employment_type": "Full-time"
        },
        {
            "id": "employee_4",
            "name": "Michael Brown",
            "experience": 12,
            "department": "Engineering",
            "role": "Senior Software Engineer",
            "skills": "Java, Spring Boot, microservices, cloud architecture, DevOps",
            "location": "San Francisco",
            "employment_type": "Full-time"
        },
        {
            "id": "employee_5",
            "name": "Emily Wilson",
            "experience": 2,
            "department": "Marketing",
            "role": "Marketing Assistant",
            "skills": "Content creation, email marketing, market research, social media management",
            "location": "Austin",
            "employment_type": "Part-time"
        },
        {
            "id": "employee_6",
            "name": "David Lee",
            "experience": 15,
            "department": "Engineering",
            "role": "Engineering Manager",
            "skills": "Team leadership, project management, software architecture, mentoring",
            "location": "Seattle",
            "employment_type": "Full-time"
        },
        {
            "id": "employee_7",
            "name": "Sarah Clark",
            "experience": 8,
            "department": "HR",
            "role": "HR Manager",
            "skills": "Performance management, compensation planning, policy development, conflict resolution",
            "location": "Boston",
            "employment_type": "Full-time"
        },
        {
            "id": "employee_8",
            "name": "Chris Evans",
            "experience": 20,
            "department": "Engineering",
            "role": "Senior Architect",
            "skills": "System design, distributed systems, cloud platforms, technical strategy",
            "location": "New York",
            "employment_type": "Full-time"
        }
    ]
    
    # Create documents for embedding
    employee_documents = []
    for employee in employees:
        document = f"{employee['role']} with {employee['experience']} years of experience in {employee['department']}. "
        document += f"Skills: {employee['skills']}. Located in {employee['location']}. "
        document += f"Employment type: {employee['employment_type']}."
        employee_documents.append(document)
    
    # Add to collection
    collection.add(
        ids=[employee["id"] for employee in employees],
        documents=employee_documents,
        metadatas=[{
            "name": employee["name"],
            "department": employee["department"],
            "role": employee["role"],
            "experience": employee["experience"],
            "location": employee["location"],
            "employment_type": employee["employment_type"]
        } for employee in employees]
    )
    
    return collection

def example_queries():
    """Demonstrate various query patterns"""
    collection = setup_employee_collection()
    
    print("=== Employee Query Examples ===\n")
    
    # 1. Search for Python developers
    print("1. Finding Python developers:")
    results = collection.query(
        query_texts=["Python developer with web development experience"],
        n_results=3
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['name']} ({doc_id}) - Distance: {distance:.4f}")
        print(f"     Role: {metadata['role']}, Department: {metadata['department']}")
    
    print("\n" + "="*50 + "\n")
    
    # 2. Search for leadership roles
    print("2. Finding leadership and management roles:")
    results = collection.query(
        query_texts=["team leader manager with experience"],
        n_results=3
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['name']} ({doc_id}) - Distance: {distance:.4f}")
        print(f"     Role: {metadata['role']}, Experience: {metadata['experience']} years")
    
    print("\n" + "="*50 + "\n")
    
    # 3. Filter by department
    print("3. Finding all Engineering employees:")
    results = collection.get(
        where={"department": "Engineering"}
    )
    for i, doc_id in enumerate(results['ids']):
        metadata = results['metadatas'][i]
        print(f"  - {metadata['name']}: {metadata['role']} ({metadata['experience']} years)")
    
    print("\n" + "="*50 + "\n")
    
    # 4. Filter by experience range
    print("4. Finding employees with 10+ years experience:")
    results = collection.get(
        where={"experience": {"$gte": 10}}
    )
    for i, doc_id in enumerate(results['ids']):
        metadata = results['metadatas'][i]
        print(f"  - {metadata['name']}: {metadata['role']} ({metadata['experience']} years)")
    
    print("\n" + "="*50 + "\n")
    
    # 5. Filter by location
    print("5. Finding employees in California:")
    results = collection.get(
        where={"location": {"$in": ["San Francisco", "Los Angeles"]}}
    )
    for i, doc_id in enumerate(results['ids']):
        metadata = results['metadatas'][i]
        print(f"  - {metadata['name']}: {metadata['location']}")
    
    print("\n" + "="*50 + "\n")
    
    # 6. Combined search: experienced Python developers in tech cities
    print("6. Finding senior Python developers in major tech cities:")
    results = collection.query(
        query_texts=["senior Python developer full-stack"],
        n_results=5,
        where={
            "$and": [
                {"experience": {"$gte": 8}},
                {"location": {"$in": ["San Francisco", "New York", "Seattle"]}}
            ]
        }
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['name']} ({doc_id}) - Distance: {distance:.4f}")
        print(f"     {metadata['role']} in {metadata['location']} ({metadata['experience']} years)")

def advanced_queries():
    """Demonstrate more advanced query patterns"""
    collection = setup_employee_collection()
    
    print("=== Advanced Employee Query Examples ===\n")
    
    # 1. Search for specific skill combinations
    print("1. Finding employees with cloud and DevOps skills:")
    results = collection.query(
        query_texts=["cloud architecture DevOps infrastructure automation"],
        n_results=3
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['name']} - {metadata['role']} - Distance: {distance:.4f}")
    
    print("\n" + "="*50 + "\n")
    
    # 2. Search for HR professionals
    print("2. Finding HR professionals with strategic skills:")
    results = collection.query(
        query_texts=["strategic HR organizational development change management"],
        n_results=2,
        where={"department": "HR"}
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['name']} - {metadata['role']} - Distance: {distance:.4f}")
    
    print("\n" + "="*50 + "\n")
    
    # 3. Search for marketing specialists
    print("3. Finding marketing specialists with analytics skills:")
    results = collection.query(
        query_texts=["marketing analytics customer analytics campaign optimization"],
        n_results=2,
        where={"department": "Marketing"}
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['name']} - {metadata['role']} - Distance: {distance:.4f}")
    
    print("\n" + "="*50 + "\n")
    
    # 4. Complex filtering: senior engineers in specific locations
    print("4. Finding senior engineers in major tech hubs:")
    results = collection.get(
        where={
            "$and": [
                {"department": "Engineering"},
                {"experience": {"$gte": 10}},
                {"location": {"$in": ["San Francisco", "New York", "Seattle"]}}
            ]
        }
    )
    for i, doc_id in enumerate(results['ids']):
        metadata = results['metadatas'][i]
        print(f"  - {metadata['name']}: {metadata['role']} in {metadata['location']} ({metadata['experience']} years)")
    
    print("\n" + "="*50 + "\n")
    
    # 5. Search for full-time employees with specific experience range
    print("5. Finding full-time employees with 5-15 years experience:")
    results = collection.get(
        where={
            "$and": [
                {"employment_type": "Full-time"},
                {"experience": {"$gte": 5, "$lte": 15}}
            ]
        }
    )
    for i, doc_id in enumerate(results['ids']):
        metadata = results['metadatas'][i]
        print(f"  - {metadata['name']}: {metadata['role']} ({metadata['experience']} years)")

def hr_use_cases():
    """Demonstrate HR-specific use cases"""
    collection = setup_employee_collection()
    
    print("=== HR Use Cases ===\n")
    
    # 1. Succession planning - finding potential leaders
    print("1. Succession Planning - Finding potential leaders:")
    results = collection.query(
        query_texts=["leadership team management mentoring"],
        n_results=3,
        where={"experience": {"$gte": 8}}
    )
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['name']} - {metadata['role']} - Distance: {distance:.4f}")
    
    print("\n" + "="*50 + "\n")
    
    # 2. Team composition analysis
    print("2. Team Composition Analysis - Engineering team:")
    results = collection.get(
        where={"department": "Engineering"}
    )
    print(f"Engineering team composition ({len(results['ids'])} members):")
    for i, doc_id in enumerate(results['ids']):
        metadata = results['metadatas'][i]
        print(f"  - {metadata['name']}: {metadata['role']} ({metadata['experience']} years)")
    
    print("\n" + "="*50 + "\n")
    
    # 3. Skill gap analysis
    print("3. Skill Gap Analysis - Finding Python developers:")
    results = collection.query(
        query_texts=["Python programming development"],
        n_results=5
    )
    print("Python developers in the organization:")
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['name']} - {metadata['role']} - Distance: {distance:.4f}")

if __name__ == "__main__":
    print("Running basic employee query examples...")
    example_queries()
    
    print("\n" + "="*60 + "\n")
    
    print("Running advanced employee query examples...")
    advanced_queries()
    
    print("\n" + "="*60 + "\n")
    
    print("Running HR use case examples...")
    hr_use_cases()
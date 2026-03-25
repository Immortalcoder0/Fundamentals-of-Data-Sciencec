# AIM: To get hands-on experience with Neo4j and understand how to manage and query graph databases. [cite: 474, 475]
# DESCRIPTION: Neo4j stores data as nodes, relationships, and properties. [cite: 477]
# It focuses on relationships, making it ideal for social networks and recommendation systems. [cite: 478]

// Cypher Queries
// 1. Create Nodes
CREATE (a: Person {name: 'Alice', age: 25}); [cite: 485, 486]
CREATE (b: Person {name: 'Bob', age: 27}); [cite: 487, 488]
CREATE (c: Person {name: 'Charlie', age: 30}); [cite: 489, 490]
// 2. Create Relationships
CREATE (a)-[: FRIENDS_WITH]->(b); [cite: 494]
CREATE (b)-[: FRIENDS_WITH]->(c); [cite: 495]
CREATE (a)-[: COLLEAGUE_OF]->(c); [cite: 497]
// 3. Retrieve All Nodes
MATCH (n) RETURN n; [cite: 499]
// 4. Retrieve All Relationships
MATCH (a)-[r]->(b) RETURN a, r, b; [cite: 500]

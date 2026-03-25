# AIM: To practice writing Cypher queries to interact with and analyze graph data in Neo4j. [cite: 536, 537]
# DESCRIPTION: Cypher (CQL) is the declarative language for Neo4j. [cite: 539]
# It allows creating/updating nodes, filtering patterns, and aggregating data relationships. [cite: 541, 542, 543]

// Cypher Queries
// 1. Find all people older than 26
MATCH (p: Person) WHERE p.age > 26 RETURN p.name, p.age; [cite: 547, 548, 549]
// 2. Count how many FRIENDS WITH relationships exist
MATCH (Person)-[r: FRIENDS_WITH]->(:Person) RETURN COUNT(r) AS TotalFriendships; [cite: 551, 552]
// 3. Find friends of a particular person (Alice)
MATCH (a: Person {name: 'Alice'})-[: FRIENDS_WITH]->(friends) RETURN friends.name AS FriendsOfAlice; [cite: 555, 556]
// 4. Find mutual connections
MATCH (a: Person)-[: FRIENDS_WITH]->(b: Person)-[: FRIENDS_WITH]->(c: Person) RETURN a.name AS Person, c.name AS MutualConnection; [cite: 558, 559]

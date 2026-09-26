---
# View Identification Metadata
view:
  id: http://example.com/project/views/dashboard_view
# Target OML description ontology context against which SPARQL queries execute
ontology: http://example.com/project/descriptionBundle#
---

# Gaming Setup Architectural Dashboard

<!-- ========================================================================= -->
<!-- 1. NETWORK CONNECTIVITY MATRIX (MATRIX VIEW)                              -->
<!-- ========================================================================= -->
## 1. Network Connectivity Matrix (Matrix View)

```matrix
PREFIX vocab: <http://example.com/method/vocabulary#>
PREFIX patterns: <http://example.com/method/patterns#>

SELECT ?row ?column (COUNT(?p1) AS ?value)
WHERE {
  ?p1 vocab:isPortOf ?row .
  
  # Matches any defined pattern link (Video, Audio, Data, or Power)
  ?p1 (patterns:connectsVideoTo|patterns:connectsAudioTo|patterns:connectsDataTo|patterns:suppliesPowerTo) ?p2 .
  
  ?p2 vocab:isPortOf ?column .
}
GROUP BY ?row ?column
```



<!-- 2. SYSTEM HARDWARE CONTAINMENT TREE (TREE VIEW)-->
## 2. System Hardware Containment Tree (Tree View)

```tree
---
containment: <http://example.com/method/vocabulary#contains>
---
PREFIX vocab: <http://example.com/method/vocabulary#>

CONSTRUCT {
  ?parent vocab:contains ?child .
} 
WHERE {
  ?child vocab:isContainedBy ?parent .
}
```



<!-- 3. Master Hardware & Specification Inventory (TABLE VIEW)-->
## 3. Master Hardware & Specification Inventory (Table View)

```table
PREFIX vocab: <http://example.com/method/vocabulary#>
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl:   <http://www.w3.org/2002/07/owl#>

SELECT ?Device ?Classification ?Brand ?PowerState
WHERE {
  ?device vocab:isPowered ?power .
  ?device rdf:type ?type .
  
  # Keep only the most specific subclass (filter out parent superclasses)
  FILTER NOT EXISTS {
    ?device rdf:type ?subType .
    ?subType rdfs:subClassOf ?type .
    FILTER(?subType != ?type)
  }
  
  # Exclude root OWL classes
  FILTER(?type != owl:Thing)
  
  BIND(STRAFTER(STR(?device), "#") AS ?Device)
  BIND(STRAFTER(STR(?type), "#") AS ?Classification)
  BIND(IF(?power, "ON", "OFF") AS ?PowerState)
  
  OPTIONAL { ?device vocab:brand ?Brand }
}
ORDER BY ?Classification ?Device
```





<!-- 4. SYSTEM WIRING TOPOLOGY (GRAPH VIEW)-->

## 4. System Wiring Topology (Graph View)

```graph
PREFIX vocab: <http://example.com/method/vocabulary#>
PREFIX patterns: <http://example.com/method/patterns#>

CONSTRUCT {
  ?sourceDevice ?link ?targetDevice .
}
WHERE {
  # Find ports belonging to source and target devices
  ?sourcePort vocab:isPortOf ?sourceDevice .
  ?targetPort vocab:isPortOf ?targetDevice .
  
  # Identify the specific connection link between those ports
  ?sourcePort ?link ?targetPort .
  
  # Filter for known connectivity properties
  FILTER (?link IN (
    patterns:connectsVideoTo, 
    patterns:connectsAudioTo, 
    patterns:connectsDataTo, 
    patterns:suppliesPowerTo, 
    vocab:connectsTo
  ))
}
```
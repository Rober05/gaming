---
template:
  id: http://example.com/method/templates/dashboard
  expose:
    - kind: compose
  params:
    - id: ontology
      defaultValue: ${context.ontology}
---

# Gaming Setup Architectural Dashboard

## 1. Network Connectivity Matrix (Matrix View)
* **Question:** Which components share common network pathways?
* **Evidence:** Cross-product matrix showing 2-hop path counts between devices and network endpoints.

```matrix
rowColumnLabel: "Device / Endpoint"
stylesheet:
  - selector: cell [Number(value) > 0]
    style:
      background-color: #d4edda
SELECT ?row ?column (COALESCE(?n, 0) AS ?value)
WHERE {
  ?row a [http://example.com/method/vocabulary#Component](http://example.com/method/vocabulary#Component) .
  ?column a [http://example.com/method/vocabulary#Component](http://example.com/method/vocabulary#Component) .
  OPTIONAL {
    SELECT ?row ?column (COUNT(*) AS ?n)
    WHERE {
      ?row [http://example.com/method/vocabulary#hasPort](http://example.com/method/vocabulary#hasPort) ?p1 .
      ?p1 [http://example.com/method/vocabulary#connectsTo](http://example.com/method/vocabulary#connectsTo) ?p2 .
      ?column [http://example.com/method/vocabulary#hasPort](http://example.com/method/vocabulary#hasPort) ?p2 .
    }
    GROUP BY ?row ?column
  }
}
```

---

## 2. System Hardware Containment Tree (Tree View)
* **Question:** How are hardware and software components structured across the setup?
* **Evidence:** Hierarchy showing component containment.

```tree
containment: [children]
containmentDirection: children
SELECT ?Component ?children WHERE {
  ?Component a [http://example.com/method/vocabulary#Component](http://example.com/method/vocabulary#Component) .
  OPTIONAL { ?Component [http://example.com/method/vocabulary#contains](http://example.com/method/vocabulary#contains) ?children }
}
```

---

## 3. Power Allocation Audit (Table View)
* **Question:** Which devices are currently powered on and active?
* **Evidence:** Query of active hardware state.

```table
orderBy: ["Device asc"]
SELECT ?Device ?IsPowered
WHERE {
  ?Device a [http://example.com/method/vocabulary#Component](http://example.com/method/vocabulary#Component) ;
          [http://example.com/method/vocabulary#isPowered](http://example.com/method/vocabulary#isPowered) ?IsPowered .
}
```
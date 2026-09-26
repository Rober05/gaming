import glob
from rdflib import Graph, Namespace, RDF, Literal

def analyze_system():
    g = Graph()
    
    # Load exported OWL/TTL files from build directory
    owl_files = glob.glob("build/owl/**/*.ttl", recursive=True) + glob.glob("build/owl/**/*.owl", recursive=True)
    if not owl_files:
        print("[-] No exported ontologies found in build/owl/. Run 'oml export -o build/owl' first.")
        return

    for f in owl_files:
        g.parse(f)

    print(f"[+] Successfully loaded {len(g)} RDF triples across {len(owl_files)} files.")
    
    VOCAB = Namespace("http://example.com/method/vocabulary#")
    PATTERNS = Namespace("http://example.com/method/patterns#")

    # 1. COMPUTED ANALYSIS 1: Active Power & Thermal Load Rollup

    print("\n=== COMPUTED ANALYSIS 1: ACTIVE POWER & THERMAL ROLLUP ===")
    
    total_watts = 0
    total_btu = 0
    
    query_power = """
    PREFIX vocab: <http://example.com/method/vocabulary#>
    SELECT ?dev ?watts ?btu WHERE {
        ?dev vocab:isPowered true .
        OPTIONAL { ?dev vocab:powerDrawWatts ?watts }
        OPTIONAL { ?dev vocab:thermalOutputBTU ?btu }
    }
    """
    
    for row in g.query(query_power):
        dev_name = str(row.dev).split("#")[-1]
        watts = int(row.watts) if row.watts else 0
        btu = int(row.btu) if row.btu else 0
        total_watts += watts
        total_btu += btu
        print(f"  - {dev_name:25s}: {watts:3d} W  |  {btu:4d} BTU/hr")

    print(f"\nTotal System Power Draw : {total_watts} W / 1000 W Budget Margin")
    print(f"Total System Thermal Load: {total_btu} BTU/hr / 3500 BTU/hr Limit")

    # 2. COMPUTED ANALYSIS 2: Storage Allocation Rollup

    print("\n=== COMPUTED ANALYSIS 2: STORAGE BUDGET ROLLUP ===")
    query_storage = """
    PREFIX vocab: <http://example.com/method/vocabulary#>
    SELECT ?game ?size ?storage ?capacity WHERE {
        ?game vocab:requiresStorage ?storage .
        ?game vocab:storageSizeGB ?size .
        ?storage vocab:storageCapacityGB ?capacity .
    }
    """
    for row in g.query(query_storage):
        game_name = str(row.game).split("#")[-1]
        storage_name = str(row.storage).split("#")[-1]
        print(f"  - Game: {game_name} ({row.size} GB) allocated on {storage_name} ({row.capacity} GB Total)")

    # 3. COMPUTED ANALYSIS 3: Video Interconnection Hop Count

    print("\n=== COMPUTED ANALYSIS 3: VIDEO INTERCONNECTION HOPS ===")
    query_hops = """
    PREFIX vocab: <http://example.com/method/vocabulary#>
    PREFIX patterns: <http://example.com/method/patterns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?srcPort ?tgtPort WHERE {
        ?link a/rdfs:subClassOf* patterns:VideoLink .
        ?link patterns:connectsVideoTo ?tgtPort .
    }
    """
    results = list(g.query(query_hops))
    print(f"Total Active Video Link Paths in Topology: {len(results)}")

if __name__ == "__main__":
    analyze_system()
---
ontology: http://example.com/project/descriptionBundle#
---

# Gaming Setup Architectural Model (OML)

An Ontological Modeling Language (OML) project that models, analyzes, and visualizes a 10-device gaming setup architecture. This repository defines component vocabularies, structural containment, port-level connectivity patterns, power allocation states, SWRL inference rules, and interactive markdown dashboard views.

---

## 🚀 Quick Navigation & Core Documentation

For in-depth documentation and live visual widgets, navigate directly to these key deliverables:

- 📊 **[Architectural Dashboard View](src/model/oml/example.com/project/dashboard_view.md)** — Renders the live SPARQL connectivity matrix, containment tree, hardware inventory table, and interactive topology graph.
- 📐 **[Methodology & Design Specification](src/method/oml/example.com/method/methodology.md)** — Covers the underlying modeling decisions, vocabulary definitions, link patterns, and SWRL inference rules.
- 🔍 **[System Analysis Report](src/analysis/ANALYSIS.md)** — Contains query documentation, reasoning output evaluations, and verification results.

---

## 1. System Hardware Scope

The system models **10 main electrical components**, their internal sub-components, ports, and software:

- **Consoles & Computing**: `xbox` (Series X), `pc` (Custom Build), `nintendoSwitch`
- **Displays**: `mainDisplay` (4K 120Hz), `monitor1080p` (1080p 144Hz)
- **A/V & Networking Hardware**: `hdmiSwitch` (Video Switch), `networkSwitch` (Network Device)
- **Peripherals & Storage**: `turtleBeachStealth700` (Headset), `controller`, `externalStorage`
- **Software & Structural Containment**: `consoleOS` (contained inside `xbox`), with ports contained inside their respective host devices.

---

## 2. Core Ontological Design & Methodology

The model is structured into reusable methodology layers (`src/method/`) and concrete instance models (`src/model/`). Full architectural specifications are detailed in **[methodology.md](src/method/oml/example.com/method/methodology.md)**.

1. **Vocabulary (`vocabulary.oml`)**: Defines hardware classes (`Console`, `Display`, `ComputingDevice`, `VideoSwitch`, `Peripheral`, `NetworkDevice`, `StorageDevice`, `Software`, `Port`), relationship entities (`connectsTo`, `hasPort`, `isContainedBy`, `routesVideoTo`, `routesAudioTo`, `routesDataTo`), and scalar attributes (`isPowered`, `brand`, `resolution`, `refreshRateHz`).
2. **Patterns (`patterns.oml`)**: Implements template-based relation instances for physical link types (`VideoLink`, `AudioLink`, `NetworkLink`).
3. **Inference Rules (`rules.oml`)**: Defines SWRL logical rules (`InferVideoRouting`, `InferAudioRouting`, `InferNetworkRouting`) to deduce high-level routing paths between host devices based on physical port connections.
4. **Description Model (`description.oml`)**: Instantiates all 10 hardware devices, assigns `vocab:isPowered true` properties, establishes port structures (`vocab:isPortOf`), defines hierarchical containment (`vocab:isContainedBy`), and connects devices via link patterns.
5. **Description Bundle (`descriptionBundle.oml`)**: Aggregates vocabularies and description graphs for reasoner processing.

---

## 3. Project Directory Structure

```bash
gaming/
├── src/
│   ├── analysis/
│   │   ├── ANALYSIS.md          # Analysis documentation and findings
│   │   ├── analyze.py           # Python SPARQL/RDF Graph analysis script
│   │   └── queries.rq           # Standard SPARQL analytical queries
│   ├── method/oml/[example.com/method/](https://example.com/method/)
│   │   ├── vocabulary.oml       # Domain concepts, properties, and relations
│   │   ├── patterns.oml         # Relation instances (VideoLink, AudioLink, NetworkLink)
│   │   ├── rules.oml            # SWRL rules for inferred routing
│   │   └── methodology.md       # Methodological documentation
│   └── model/oml/[example.com/project/](https://example.com/project/)
│       ├── description.oml      # 10-device instance definitions and connections
│       ├── descriptionBundle.oml# Bundled instance and vocabulary graph
│       ├── dashboard_view.md    # Interactive SPARQL dashboard widget source
│       └── oml.catalog.xml      # Project catalog mapping
├── build/                       # Output directory for compiled RDF/OWL & rendered docs
├── catalog.xml                  # Root catalog file
└── README.md                    # Project documentation
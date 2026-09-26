# Gaming Setup System Architecture Methodology

## Design Rationale & Scope
This design methodology provides a standardized, pattern-based approach for modeling consumer electronics, gaming consoles, displays, and peripheral interconnection topologies.

## Description Layout & Patterns
To avoid ad-hoc graph modeling, all connections between system elements must leverage one of four standardized relation patterns:
1. **VideoLink Pattern:** Captures HDMI/DisplayPort physical connections for high-bandwidth display paths.
2. **AudioLink Pattern:** Captures 3.5mm/Optical audio channels for headset and peripheral sound output.
3. **NetworkLink Pattern:** Models Ethernet/RJ45 paths for online matchmaking and console update traffic.
4. **PowerLink Pattern:** Defines power routing from switches or power supplies to active hardware.

## Rule-Driven Inference
The methodology incorporates automated SWRL reasoning to reduce manual relation creation:
* **Video Routing Rule:** Inferring video delivery based on port-level cable connections without requiring manual `routesVideoTo` statements.
* **Audio Routing Rule:** Automatically connecting active gaming devices to audio output endpoints upon port pairing.

## Trade-offs and Open Issues
* **Trade-off:** Using explicit `Port` instances increases overall instance count, but guarantees clear domain/range safety for cable connectivity.
* **Open Issue:** Multi-hop switch routing (e.g., Console -> Switch -> Receiver -> Display) requires recursive rule reasoning.
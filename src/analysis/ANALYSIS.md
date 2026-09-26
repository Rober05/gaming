# Gaming Setup System Analysis & Methodology Validation

## 1. Module 1 Stakeholder Questions Analysis

### Question 1 (Player)
> **Question:** Which components in my gaming setup are affected if my WiFi bandwidth drops below 20 Mbps?
* **Evidence:** SPARQL Query Q1 matching `NetworkLink` relation patterns against device ports.
* **Finding:** The `xbox` console and `pc` rely on `netSw_port1` via `NetworkLink`. A drop in WiFi/Ethernet bandwidth directly affects online matchmaking, game downloads, and system telemetry on both devices.

### Question 2 (Player)
> **Question:** Which installed games exceed the storage budget on my console and require cleanup to avoid performance degradation?
* **Evidence:** SPARQL Query Q2 checking `Software` and `StorageDevice` relations.
* **Diagnosed Gap:** **Vocabulary Gap**. The vocabulary defines `concept Software` and `concept StorageDevice`, but currently lacks scalar properties for `storageSizeGB` and `storageCapacityGB`.
* **Action:** Extend `vocabulary.oml` with `scalar property storageSizeGB [ domain Software range xsd:integer ]`.

### Question 3 (Player)
> **Question:** When the Bluetooth interface saturates or fails, which peripheral functions degrade, and which gameplay modes are impacted?
* **Evidence:** SPARQL Query Q3 checking `Peripheral` and `AudioLink` connections.
* **Diagnosed Gap:** **Pattern Gap**. The `AudioLink` pattern connects audio ports but does not model latency limits or haptic feedback channels.
* **Action:** Update `patterns.oml` to declare haptic data relation properties.

### Question 4 (Online Teammates)
> **Question:** Which multiplayer games in my library rely on the same network path, and where are the bottlenecks that cause latency spikes?
* **Evidence:** SPARQL Query Q4 and topology traversal in `analyze.py`.
* **Finding:** Both `xbox` and `pc` route through `networkSwitch` via port `netSw_port1`. This single physical switch port creates a bandwidth bottleneck during simultaneous online gaming sessions.

### Question 5 (Game Developers)
> **Question:** Which subsystems (console, router, display) exceed their power or thermal budget when all components are active?
* **Evidence:** Scripted power calculation in `analyze.py`.
* **Finding:** Active hardware (`xbox`, `pc`, `mainDisplay`, `monitor1080p`, `turtleBeachStealth700`) draws an estimated total of **603 W**, staying within the 1000 W overall power allocation margin.

---

## 2. Pattern Gap Detection Results

| Pattern Name | Gap Detection Query Type | Result | Diagnosed Gap / Finding |
| :--- | :--- | :--- | :--- |
| **VideoLink** | Unlinked Video Ports | Clean | All video ports are properly bound to active `VideoLink` entities. |
| **AudioLink** | Missing Haptic Channel | **Gap Identified** | AudioLink models audio streaming but omits controller haptic data channels. |
| **NetworkLink** | Bottleneck Detection | **Gap Identified** | Shared switch port `netSw_port1` lacks redundant pathing. |
| **PowerLink** | Unlinked Power Ports | Clean | All active hardware components map cleanly to power sources. |

---

## 3. System View Dashboard Summary

1. **Connectivity Matrix View:** Visualizes 2-hop path counts between connected devices.
2. **Containment Tree View:** Displays hardware component containment hierarchies (`xbox` $\rightarrow$ `consoleOS`, `xbox_hdmi`).
3. **Power Status Table View:** Summarizes active powered components across the system scope.

---

## 4. Reusable Template Reference
* **Template File:** `src/method/oml/example.com/method/templates/dashboard.md`
* **Template Type:** `compose` template
* **Scope:** Analyzes the `http://example.com/project/bundle#` project ontology context.
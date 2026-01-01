# Quantum Cybersecurity Experiments

This directory contains simulations and analysis scripts used for the research paper on Quantum Computing and Cybersecurity.

## Experiments Overview

### 1. BB84 Quantum Key Distribution (QKD) Simulation
- **Location**: `bb84_simulation/bb84_sim.py`
- **Description**: Simulates the BB84 protocol using Qiskit. It demonstrates how Alice and Bob can establish a secure key using quantum states and detect eavesdropping (via basis mismatch).
- **Key Finding**: Successfully established a shared secret key where bases matched for approximately 50% of the bits, confirming the theoretical efficiency of the protocol.

### 2. Shor's Algorithm Complexity Analysis
- **Location**: `shors_analysis/shors_complexity.py`
- **Description**: A mathematical comparison between the classical complexity of breaking RSA (using GNFS) and the quantum complexity (using Shor's Algorithm).
- **Output**: `shors_analysis/complexity_comparison.png`
- **Key Finding**: Visualizes the exponential vs. polynomial gap, highlighting why current RSA-2048/4096 standards are fundamentally insecure against large-scale quantum computers.

### 3. Post-Quantum Cryptography (PQC) Benchmarks
- **Location**: `pqc_benchmarks/pqc_sim.py`
- **Description**: Simulates the computational overhead of lattice-based PQC algorithms compared to classical methods.
- **Key Finding**: While PQC algorithms are computationally efficient (ms range), they introduce significant memory and bandwidth overhead due to larger key and signature sizes.

## How to Run
Ensure you have the required dependencies installed:
```bash
sudo pip3 install qiskit qiskit-aer numpy matplotlib
```
Run each script individually from the root directory.

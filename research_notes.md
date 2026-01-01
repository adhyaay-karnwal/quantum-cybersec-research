# Quantum Computing and Cybersecurity Research Notes

## 1. Core Threats to Current Cryptography
- **Shor's Algorithm**: Can factor large integers and solve discrete logarithms in polynomial time. This directly threatens:
    - **RSA**: Relies on the difficulty of integer factorization.
    - **ECC (Elliptic Curve Cryptography)**: Relies on the discrete logarithm problem.
    - **Diffie-Hellman**: Key exchange mechanism.
- **Grover's Algorithm**: Provides a quadratic speedup for unstructured search.
    - **Symmetric Encryption (AES)**: Effectively halves the key strength. AES-128 becomes equivalent to 64-bit security; AES-256 becomes equivalent to 128-bit security.
    - **Hash Functions (SHA-2, SHA-3)**: Reduces collision resistance, requiring larger output sizes.

## 2. Broader Consequences
- **"Harvest Now, Decrypt Later" (HNDL)**: Attackers capture encrypted data today to decrypt it once cryptographically relevant quantum computers (CRQCs) are available.
- **Identity and Trust**: Digital signatures (used for software updates, legal documents, and financial transactions) will become forgeable.
- **National Security**: Government secrets and diplomatic communications could be exposed retroactively.

## 3. Impact on AI and Humanity
- **Quantum-Enhanced AI (QML)**: Quantum computers can accelerate machine learning training and optimization.
    - **Malicious AI**: Could be used to find vulnerabilities faster or generate more sophisticated social engineering attacks.
    - **Defensive AI**: Could enable real-time threat detection at a scale impossible for classical computers.
- **Existential Risks**: The collapse of digital trust could lead to societal chaos, economic instability, and the failure of critical infrastructure (power grids, water systems) that rely on secure communication.

## 4. "Quantic Security" (Proposed Concept)
- **Definition**: A new paradigm of security that leverages quantum mechanics not just for defense, but as the fundamental layer of all digital interaction.
- **Key Components**:
    - **Quantum Key Distribution (QKD)**: Using entanglement and the uncertainty principle to ensure keys cannot be intercepted without detection.
    - **Post-Quantum Cryptography (PQC)**: Mathematical algorithms (lattice-based, code-based, etc.) that are resistant to both classical and quantum attacks.
    - **Quantum Random Number Generation (QRNG)**: Truly unpredictable entropy for cryptographic keys.
    - **Quantum-Safe AI**: AI models trained and operating within a quantum-secure framework.

## 5. The New Age of Security
- **Crypto-Agility**: The ability to swap cryptographic protocols seamlessly as new threats emerge.
- **Quantum Internet**: A network where information is transmitted via qubits, inherently secure due to the no-cloning theorem.

## 6. Post-Quantum Cryptography (PQC) Standards
NIST has finalized the first set of PQC standards (August 2024):
- **FIPS 203 (ML-KEM)**: Based on the CRYSTALS-Kyber algorithm. A lattice-based key encapsulation mechanism.
- **FIPS 204 (ML-DSA)**: Based on the CRYSTALS-Dilithium algorithm. A lattice-based digital signature scheme.
- **FIPS 205 (SLH-DSA)**: Based on the SPHINCS+ algorithm. A stateless hash-based digital signature scheme.
- **FALCON**: Another lattice-based signature scheme, expected to be finalized soon.

### Comparison of PQC Approaches:
| Approach | Mathematical Basis | Pros | Cons |
| :--- | :--- | :--- | :--- |
| **Lattice-based** | Shortest Vector Problem (SVP) | High efficiency, versatile (KEM & Signatures) | Larger key/signature sizes than classical |
| **Code-based** | Decoding random linear codes | Very fast, well-studied (McEliece) | Extremely large public keys |
| **Hash-based** | Collision resistance of hashes | Smallest security assumptions | Large signatures, often stateful |
| **Multivariate** | Solving systems of multivariate equations | Very small signatures | Large public keys, complex security proofs |

## 7. Quantum Key Distribution (QKD) vs. PQC
- **QKD**:
    - **Pros**: Information-theoretic security (physics-based), detects eavesdropping.
    - **Cons**: Requires specialized hardware (fiber/satellite), distance limitations, high cost.
- **PQC**:
    - **Pros**: Software-based, works on existing internet infrastructure, cost-effective.
    - **Cons**: Security relies on mathematical assumptions (unproven), vulnerable to future mathematical breakthroughs.

## 8. Defining "Quantic Security"
"Quantic Security" is not just a patch for existing systems; it is a holistic architecture where:
1. **Physical Layer**: Uses QKD for ultra-secure backbones and QRNG for entropy.
2. **Network Layer**: Implements PQC for end-to-end encryption across standard infrastructure.
3. **Application Layer**: Employs "Quantum-Safe AI" for real-time anomaly detection and crypto-agility.
4. **Human Layer**: Shifts from "trust but verify" to "quantum-verified identity," where digital signatures are backed by quantum-resistant proofs.

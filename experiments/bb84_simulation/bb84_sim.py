import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import random

def create_bb84_circuit(alice_bits, alice_bases):
    """
    Creates a BB84 circuit for Alice to send qubits to Bob.
    """
    n = len(alice_bits)
    circuits = []
    for i in range(n):
        qc = QuantumCircuit(1, 1)
        # Alice prepares the qubit
        if alice_bits[i] == 1:
            qc.x(0)
        if alice_bases[i] == 1: # 1 for Hadamard basis (X), 0 for Computational basis (Z)
            qc.h(0)
        circuits.append(qc)
    return circuits

def bob_measure(circuits, bob_bases):
    """
    Bob measures the qubits sent by Alice.
    """
    n = len(circuits)
    bob_results = []
    backend = Aer.get_backend('qasm_simulator')
    
    for i in range(n):
        qc = circuits[i]
        if bob_bases[i] == 1: # Bob chooses X basis
            qc.h(0)
        qc.measure(0, 0)
        
        # Run simulation
        new_circuit = transpile(qc, backend)
        job = backend.run(new_circuit, shots=1)
        result = job.result()
        counts = result.get_counts()
        measured_bit = int(list(counts.keys())[0])
        bob_results.append(measured_bit)
        
    return bob_results

def simulate_bb84(n_bits=100):
    print(f"--- Starting BB84 Simulation with {n_bits} bits ---")
    
    # 1. Alice generates random bits and bases
    alice_bits = [random.randint(0, 1) for _ in range(n_bits)]
    alice_bases = [random.randint(0, 1) for _ in range(n_bits)]
    
    # 2. Alice prepares and sends qubits
    circuits = create_bb84_circuit(alice_bits, alice_bases)
    
    # 3. Bob chooses random bases and measures
    bob_bases = [random.randint(0, 1) for _ in range(n_bits)]
    bob_results = bob_measure(circuits, bob_bases)
    
    # 4. Sifting: Alice and Bob compare bases
    final_alice_key = []
    final_bob_key = []
    
    for i in range(n_bits):
        if alice_bases[i] == bob_bases[i]:
            final_alice_key.append(alice_bits[i])
            final_bob_key.append(bob_results[i])
            
    # 5. Verification
    match = final_alice_key == final_bob_key
    print(f"Bases matched for {len(final_alice_key)} bits.")
    print(f"Keys match: {match}")
    
    if match:
        print(f"Final Key (first 20 bits): {final_alice_key[:20]}")
    
    return final_alice_key, final_bob_key

if __name__ == "__main__":
    simulate_bb84(50)

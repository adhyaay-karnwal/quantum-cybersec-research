import matplotlib.pyplot as plt
import numpy as np
import math

def classical_complexity(n_bits):
    """
    General Number Field Sieve (GNFS) complexity:
    exp((64/9 * n)^(1/3) * (log n)^(2/3))
    """
    n = n_bits * math.log(2)
    return np.exp((64/9 * n)**(1/3) * (math.log(n))**(2/3))

def quantum_complexity(n_bits):
    """
    Shor's Algorithm complexity:
    O(n^3) or O(n^2 log n log log n)
    """
    return n_bits**3

def plot_complexity():
    bits = np.arange(16, 2048, 16)
    classical = [classical_complexity(b) for b in bits]
    quantum = [quantum_complexity(b) for b in bits]
    
    plt.figure(figsize=(10, 6))
    plt.plot(bits, classical, label='Classical (GNFS)', color='red')
    plt.plot(bits, quantum, label="Quantum (Shor's)", color='blue')
    
    plt.yscale('log')
    plt.xlabel('Key Size (bits)')
    plt.ylabel('Operations (log scale)')
    plt.title("Cryptographic Breaking Complexity: Classical vs Quantum")
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    
    plt.savefig('/home/ubuntu/quantum-cybersec-research/experiments/shors_analysis/complexity_comparison.png')
    print("Complexity plot saved to experiments/shors_analysis/complexity_comparison.png")

if __name__ == "__main__":
    plot_complexity()

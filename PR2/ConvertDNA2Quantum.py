
import sys
import numpy as np
import math

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile

# , execute, BasicAer, IBMQ
from qiskit.visualization import plot_histogram, plot_bloch_multivector

# from qiskit.extensions import Initialize
from qiskit.circuit.library import Initialize

from qiskit.visualization import array_to_latex
from qiskit.quantum_info import Statevector

from qiskit_aer import AerSimulator

def DNA2QuantumCircuit(bitstring, qr, cr):
    """
    create a circuit for constructing the quantum superposition of the bitstring
    """
    n = math.ceil(math.log2(len(bitstring))) + 2                 #number of qubits
    assert n > 2, "the length of bitstring must be at least 2"

    qc = QuantumCircuit(qr, cr)

    #the probability amplitude of the desired state
    desired_vector = np.array([ 0.0 for i in range(2**n) ])     #initialize to zero

    print(len(desired_vector))

    display(array_to_latex(Statevector(desired_vector), prefix="\\ket{\\psi_0} = "))

    qc_init = QuantumCircuit(n) # Creación de compuertas circuitales para inicialización

    amplitude = np.sqrt(1.0/2**(n-2))

    for i, b in enumerate(bitstring):
        pos = i * 4
        if b == "T": 
            pos += 0
        elif b == "G":
            pos += 1
        elif b == "C":
            pos += 2
        elif b == "A":
            pos += 3
        desired_vector[pos] = amplitude

    display('The circuit state vector is', array_to_latex(Statevector(desired_vector), prefix="\\ket{\\psi_{initilized}} = "))

    init = Initialize(desired_vector)

    qc_init.append(init, qc_init.qubits)
    qc.append(qc_init, qr)
    qc.barrier(qr)

    print()
    return qc



def DNA2InvQuantumCircuit(bitstring, qr, cr):
    """
    create a circuit for constructing the quantum superposition of the bitstring
    """
    n = math.ceil(math.log2(len(bitstring))) + 2                 #number of qubits
    assert n > 2, "the length of bitstring must be at least 2"

    qc = QuantumCircuit(qr, cr)

    #the probability amplitude of the desired state
    desired_vector = np.array([ 0.0 for i in range(2**n) ])     #initialize to zero

    print(len(desired_vector))

    display(array_to_latex(Statevector(desired_vector), prefix="\\ket{\\psi_0} = "))

    inverse_qc_init = QuantumCircuit(n) # Creación de compuertas circuitales para inversión de la inicialización

    amplitude = np.sqrt(1.0/2**(n-2))

    for i, b in enumerate(bitstring):
        pos = i * 4
        if b == "T": 
            pos += 0
        elif b == "G":
            pos += 1
        elif b == "C":
            pos += 2
        elif b == "A":
            pos += 3
        desired_vector[pos] = amplitude

    display('The circuit state vector is', array_to_latex(Statevector(desired_vector), prefix="\\ket{\\psi_{initilized}} = "))

    init = Initialize(desired_vector)
    
    uncompute = init.gates_to_uncompute().decompose()

    inverse_qc_init.append(uncompute, inverse_qc_init.qubits)
    qc.append(inverse_qc_init, qr)

    qc.barrier(qr)
    for i in range(n):
        qc.measure(qr[i], cr[i])
    print()
    return qc    
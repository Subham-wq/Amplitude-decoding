from qiskit.circuit.library import UGate
import numpy as np
from qiskit import *



num_qubit = 3
qc = QuantumCircuit(num_qubit)
qc.rz(np.pi/3, 0)
qc.crz(np.pi / 3, 0, 1)
qc.crz(np.pi / 3, 0, 1)
t_list=[0,1,2]
UG = UGate(np.pi/3, 0, 0).control(2)
qc.append(UG,t_list)
qc.append(UG,t_list)
qc.append(UG,t_list)
qc.append(UG,t_list)

qc.draw()

from qiskit import QuantumCircuit,execute,BasicAer
import sys 
try:
    if(len(sys.argv) > 2 and sys.argv[2] == 'run'):
        newQc = QuantumCircuit.from_qasm_file('circuit.qasm')
        backend = BasicAer.get_backend('qasm_simulator')
        job = execute(newQc, backend, shots=int(sys.argv[1]))
        result = job.result()
        print("\n The results are: " + str(result.get_counts(newQc)) + "\n")
except Exception as inst:
    d = inst
    print(d)
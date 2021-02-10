def main():
    from qiskit import QuantumCircuit,execute,BasicAer
    import sys 
    try:
        if(len(sys.argv) > 1):
            filename = str(sys.argv[1])
        else:
            raise FileNotFoundError("\n File name must be specified on argument 1 \n")
        newQc = QuantumCircuit.from_qasm_file(filename)
        shots = 100
        if(len(sys.argv) > 2 and (sys.argv[2] == "d" or sys.argv[2] == "draw")):
            print("\n")
            print(newQc.draw())
            print("\n")
        elif(len(sys.argv) > 2):
            shots = int(sys.argv[2])
        if(len(sys.argv) > 3):
            shots = int(sys.argv[3])
        backend = BasicAer.get_backend('qasm_simulator')
        job = execute(newQc, backend, shots=shots)
        result = job.result()
        print("\n The results are: " + str(result.get_counts(newQc)) + "\n")
    except Exception as inst:
        d = inst
        print(d)
if __name__ == "__main__":
    main()
import qiskit

def blackBox(x):
	return x

qr = qiskit.QuantumRegister(2) # call two quantum bits (or qubits)
cr = qiskit.ClassicalRegister(1) # call a clasical bit

program = qiskit.QuantumCircuit(qr, cr)
# get |+> and |->
program.h(qr[0])
program.x(qr[1])
program.h(qr[1])
program.barrier()

# apply oracle function
funcX = blackBox(qr[1])
program.cx(qr[0], qr[1])
program.barrier()

# apply hadamard gate to qubit0
program.h(qr[0])
program.barrier()


program.measure(qr[0],cr)

job = qiskit.execute( program, qiskit.BasicAer.get_backend('qasm_simulator') )

print(job.result().get_counts())
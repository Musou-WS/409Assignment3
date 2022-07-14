import qiskit

def constant():
	program.x(qr[0])
def balanced():
	program.cx(qr[0], qr[1])

qr = qiskit.QuantumRegister(2) # call two quantum bits (or qubits)
cr = qiskit.ClassicalRegister(1) # call a clasical bit

program = qiskit.QuantumCircuit(qr, cr)
# get |+> and |->
program.h(qr[0])
program.x(qr[1])
program.h(qr[1])
program.barrier()

# apply oracle function
# funcX = blackBox(qr[1])
balanced()
program.barrier()

# apply hadamard gate to qubit0
program.h(qr[0])
program.barrier()


program.measure(qr[0],cr)

job1 = qiskit.execute( program, qiskit.BasicAer.get_backend('qasm_simulator') )

# ibmq
qiskit.IBMQ.save_account('your token',overwrite=True) #Replace the text my_token for your own token
qiskit.IBMQ.load_account() # load the token
provider = qiskit.IBMQ.get_provider("ibm-q")
backend = provider.get_backend('ibmq_lima') # select the name of the quatum computer to use
job2 = qiskit.execute(program, backend)

# show the result
print(job1.result().get_counts())

print(job2.result().get_counts())
#Reference
#https://leimao.github.io/blog/Deutsch-Algorithm/
#Lecture Notes "Weeks 7-8 2022.pdf"
#"program.barrier()" https://github.com/atilsamancioglu/QX07-DeutschAlgorithm
#"use X Gate to simulate constant functions" https://github.com/MakotoNakai/Deutch-Algorithm/blob/master/Deutch_constant.py
#"use IBMQ" https://fullstackquantumcomputation.tech/blog/post-tutorial-0-Hello-world/

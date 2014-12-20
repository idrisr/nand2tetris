// push constant 7
@7
D=A 
@256
M=D // put 7 into M[256]. also need to increment the stack pointer

// push constant 8
@8
D=A
@257
M=D

// add
// pops top two elements from stack
// saves result at top of stack
// update stack pointer
@256
M=M+D
0;JMP

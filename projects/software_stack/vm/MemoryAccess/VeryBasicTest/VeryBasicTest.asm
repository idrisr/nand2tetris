@12 // push constant 12
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // pop local 0
D=M
@0
D=A+D
@R5
M=D
@SP
A=M-1
D=M
@R5
A=M
M=D
@SP
M=M-1
@21 // push constant 21
D=A
@SP
A=M
M=D
@SP
M=M+1

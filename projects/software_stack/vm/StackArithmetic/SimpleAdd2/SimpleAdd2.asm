@9 // push constant 9
D=A
@SP
A=M
M=D
@SP
M=M+1
@8 // push constant 8
D=A
@SP
A=M
M=D
@SP
M=M+1
@2 // push constant 2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // add
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M+D

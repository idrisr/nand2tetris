@57 // push constant 57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31 // push constant 31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53 // push constant 53
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
@112 // push constant 112
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // sub
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M-D
@SP // neg
A=M-1
MD=-M
@SP // and
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M&D

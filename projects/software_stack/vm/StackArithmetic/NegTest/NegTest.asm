@42 // push constant 42
D=A
@SP
A=M
M=D
@SP
M=M+1
@16 // push constant 16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // neg
A=M-1
MD=-M
@SP // not
A=M-1
MD=!M

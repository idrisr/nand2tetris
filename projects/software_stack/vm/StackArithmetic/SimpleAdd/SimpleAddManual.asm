@7        // push 7
D=A
@SP
A=M
MD=D
@SP
M=M+1
@8        // push 8
D=A
@SP
A=M
MD=D
@SP
M=M+1

@SP       // add
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M+D

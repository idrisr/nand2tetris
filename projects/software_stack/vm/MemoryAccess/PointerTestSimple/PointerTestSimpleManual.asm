// push   constant   3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop    pointer    0
// goes into THIS
@SP
A=M-1
D=M
@3 // translate arg1 with arg2 directly to address
M=D
@SP
M=M-1

// push   constant   3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop    pointer    1
// goes into THAT
@SP
A=M-1
D=M
@4 // translate arg1 with arg2 directly to address
M=D
@SP
M=M-1

// push pointer 1
@4
D=M
@SP
A=M
M=D
@SP
M=M+1

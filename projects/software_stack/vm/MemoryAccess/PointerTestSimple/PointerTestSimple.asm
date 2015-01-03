@3030 // push   constant   3030
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // pop    pointer    0
A=M-1
D=M
@3
M=D
@SP
M=M-1
@3040 // push   constant   3040
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // pop    pointer    1
A=M-1
D=M
@4
M=D
@SP
M=M-1
@4 // push   pointer    1
D=M
@SP
A=M
M=D
@SP
M=M+1

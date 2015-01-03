@3030 // push   constant   3030
D=A
@SP
A=M
M=D
@SP
M=M+1
@pointer // pop    pointer    0
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
@3040 // push   constant   3040
D=A
@SP
A=M
M=D
@SP
M=M+1
@pointer // pop    pointer    1
D=M
@1
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
@32 // push   constant   32
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS // pop    this       2
D=M
@2
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
@46 // push   constant   46
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT // pop    that       6
D=M
@6
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
@3 // push   pointer    0
D=M
@SP
A=M
M=D
@SP
M=M+1
@4 // push   pointer    1
D=M
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
@THIS // push   this       2
D=M
@2
A=A+D
D=M
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
@THAT // push   that       6
D=M
@6
A=A+D
D=M
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

// push constant 16
@16
D=A
@256
M=D
@SP
M=M+1

// push constant 16
@16
D=A
@257
M=D
@SP
M=M+1

// eq
@SP
A=M-1
D=M
@SP
M=M-1

@SP
A=M-1
D=M-D

@SP
M=M-1

@L1.t // true
D;JEQ
@L1.f // false
(L1.f) // false
    @SP
    A=M
    M=0
    @L1.c  // continue
    0;JMP
(L1.t)
    @SP
    A=M
    M=-1
    @L1.c // continue
    0;JMP
(L1.c) 
@SP
M=M+1

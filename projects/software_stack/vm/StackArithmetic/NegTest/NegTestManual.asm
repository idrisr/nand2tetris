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
@257
D=M

@256
D=M-D
@L1.t // true
D;JEQ
@L1.f // false
(L1.f) // false
    @256
    M=0
    @L1.c  // continue
    0;JMP
(L1.t)
    @256
    M=-1
    @L1.c // continue
    0;JMP
(L1.c) 
    @SP
    M=M-1  // decrement stack pointer

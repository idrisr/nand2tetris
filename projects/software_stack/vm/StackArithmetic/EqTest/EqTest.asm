@17
D=A
@256
M=D
@SP
M=M+1

@16
D=A
@257
M=D
@SP
M=M+1

@257
D=M

@256
D=D-M
@L1
D;JGT
(L1.t) // true
@256
M=-1
@L1.c // continue

(L1.f) // false
@256
M=0
@L1.c  // continue
(L1.c) // continue
@SP
M=M+1  // increment stack pointer

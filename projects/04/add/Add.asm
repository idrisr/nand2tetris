// Adds R0 and R1 and stores the result in R2.  // (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.) 

@R0
D=M
@R1
D=D+M
@R2
M=D
@END

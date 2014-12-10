// Multiplies R0 and R1 and stores the result in R2.  // (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.) 

// loop setup
@0
D=M

@a
M=D

@1
D=M
@b
M=D

@i
M=0 // i=0

@2
M=0 // location for the product

// while loop
(LOOP)
    @i
    D=M
    @a
    D=D-M
    @END
    D;JEQ

    @b
    D=M

    @2
    M=D+M

    @i
    M=M+1
    @LOOP
    0;JMP
(END)

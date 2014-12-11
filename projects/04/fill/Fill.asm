@16384
D=A

@screen_start
M=D

@i
M=D // i=screen_start

@24575
D=A

@screen_end
M=D

(LOOP)
    @i
    D=M
    @screen_end
    D=M-D
    @END
    D;JLT

    @i    // i=i+1 (with new i left in D)
    A=M
    M=-1

    @i
    M=M+1

    @LOOP
    0;JMP
(END)

// This is the key to moving the address pointer around
// A=M
// M=D

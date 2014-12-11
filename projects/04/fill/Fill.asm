// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// constant value for 16384
@SCREEN
D=A

@i
M=D 

@SCREEN
D=A

@24575
D=A
@screen_end
M=D

(LOOP)
    @SCREEN
    D=A

    @i
    M=D 

    @SCREEN
    D=A

    @24575
    D=A
    @screen_end
    M=D

    @KBD
    D=M

    @TOGGLEOFF
    D;JEQ
    @TOGGLEON

// set screen to black
(TOGGLEON)
    @i
    D=M
    @screen_end
    D=M-D
    @LOOP
    D;JLT

    @i    // i=i+1 (with new i left in D)
    A=M
    M=-1

    @i
    M=M+1

    @TOGGLEON
    D;JMP

(TOGGLEOFF)
    @i
    D=M
    @screen_end
    D=M-D
    @LOOP
    D;JLT

    @i    // i=i+1 (with new i left in D)
    A=M
    M=0

    @i
    M=M+1

    @TOGGLEOFF
    D;JMP

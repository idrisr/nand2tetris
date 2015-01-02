// push constant 510
@510
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop temp 6
@SP
A=M-1
D=M
@11 // translate arg1 with arg2 directly to address
M=D
@SP
M=M-1

// push constant 415
@415
D=A
@SP
A=M
M=D
@SP
M=M+1

// push temp 6
// @R5
// D=M
// A=A+D
@11
D=M
@SP
A=M
M=D
@SP
M=M+1

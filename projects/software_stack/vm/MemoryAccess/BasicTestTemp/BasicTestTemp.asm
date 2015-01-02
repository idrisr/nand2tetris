// push constant 510
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop temp 6
@R5
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
// push constant 415
@415
D=A
@SP
A=M
M=D
@SP
M=M+1
// push temp 6
@R5
D=M
@6
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1

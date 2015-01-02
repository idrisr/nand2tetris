@10 // push constant 10
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // pop local 0
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
@21 // push constant 21
D=A
@SP
A=M
M=D
@SP
M=M+1
@22 // push constant 22
D=A
@SP
A=M
M=D
@SP
M=M+1
@ARG // pop argument 2
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
@ARG // pop argument 1
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
@36 // push constant 36
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS // pop this 6
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
@42 // push constant 42
D=A
@SP
A=M
M=D
@SP
M=M+1
@45 // push constant 45
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT // pop that 5
D=M
@5
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
@THAT // pop that 2
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
@510 // push constant 510
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // pop temp 6
A=M-1
D=M
@11
M=D
@SP
M=M-1
@LCL // push local 0
D=M
@0
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // push that 5
D=M
@5
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
@ARG // push argument 1
D=M
@1
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
@THIS // push this 6
D=M
@6
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // push this 6
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
@SP // sub
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M-D
@11 // push temp 6
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

@12 // push   constant   12
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // pop    local      1
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
@21 // push   constant   21
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // push   local      1
D=M
@1
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1

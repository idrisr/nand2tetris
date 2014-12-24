//// push constant 10
@12
D=A
// @256 // should use SP's M to do this!
@SP // this is going to be a common idiom
A=M //
M=D // end idiom
@SP
M=M+1 // SP=257, @256=12


//// pop local 0
// get the value pointed at by SP-1
@SP
A=M-1 // go to the address-1 of SP
D=M   // D = 12

// Get to the address pointed at by LCL ( or LCL - 1?)
@LCL
A=M // goto where LCL is pointed at
M=D // set its value to D

// incrememnt LCL's pointer
@LCL
M=M+1

// decrement SP's pointer
@SP
M=M-1
////

// @LCL = 11
// @SP = 256
// @10 = 12

//// push constant 21
@21
D=A
@SP
A=M
M=D
@SP
M=M+1

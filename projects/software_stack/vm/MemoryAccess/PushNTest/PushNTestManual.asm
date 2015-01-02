//// push constant 18
@18
D=A
// @256 // should use SP's M to do this!
@SP // this is going to be a common idiom
A=M //
M=D // end idiom
@SP
M=M+1 // SP=257, @256=12
////////////////////

////// pop local 8
// get LCL + arg2
@LCL
D=M
@8 // arg2
D=A+D
// set to TMP
@R5
M=D
// put SP in D
@SP
A=M-1 // go to the address-1 of SP
D=M   // D = 12

// set LCL+ arg2
@R5
A=M
M=D

// decrement SP
@SP
M=M-1
////////////////////

//// push constant 21
@21
D=A
@SP
A=M
M=D
@SP
M=M+1
////////////////////

//// push   local      8
@LCL
D=M
@8
A=A+D // address of local 8
D=M   // D = Local 8 value

@SP 
A=M
M=D
@SP
M=M+1

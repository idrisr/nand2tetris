// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/MemoryAccess/VeryBasicTest/VeryBasicTest.tst

// load VeryBasicTestManual.asm,
load VeryBasicTest.asm,
output-file VeryBasicTest.out,
compare-to VeryBasicTest.cmp,
//          SP            LCL           @SP-1           @LCL-1
output-list RAM[0]%D1.6.1 RAM[1]%D1.6.1 RAM[256]%D1.6.1 RAM[300]%D1.6.1;

set RAM[0] 256, // SP
set RAM[1] 300, // LCL
// set RAM[2] 400, // ARG
// set RAM[3] 3000,// THIS
// set RAM[4] 3010,// THAT

repeat 50 {
  ticktock;
}

output;

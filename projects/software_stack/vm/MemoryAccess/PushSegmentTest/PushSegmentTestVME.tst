// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/MemoryAccess/PushSegmentTest/PushSegmentTestVME.tst

load          PushSegmentTest.vm,
output-file   PushSegmentTest.out,
compare-to    PushSegmentTest.cmp,

//          SP            LCL           @SP-1           @LCL-1
output-list RAM[0]%D1.6.1 RAM[1]%D1.6.1 RAM[256]%D1.6.1 RAM[308]%D1.6.1;

set RAM[0] 256, // SP
set RAM[1] 300, // LCL

repeat 50 {
  vmstep;
}

output;

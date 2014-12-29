// this file is part of www.nand2tetris.org
// and the book "the elements of computing systems"
// by nisan and schocken, mit press.
// file name: projects/07/memoryaccess/pushsegmenttest/pushsegmenttest.tst

load PushSegmentTest.asm,
output-file PushSegmentTest.out,
compare-to PushSegmentTest.cmp,

//          SP            LCL           @SP-1           @LCL-1
output-list RAM[0]%D1.6.1 RAM[1]%D1.6.1 RAM[256]%D1.6.1 RAM[257]%D1.6.1;

set RAM[0] 256, // SP
set RAM[1] 300, // LCL

repeat 50 {
  ticktock;
}

output;

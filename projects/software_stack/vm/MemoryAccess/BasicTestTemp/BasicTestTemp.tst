// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/MemoryAccess/BasicTestTemp/BasicTestTemp.tst
// load BasicTestTemp.asm,
load BasicTestTempManual.asm,
output-file BasicTestTemp.out,
compare-to BasicTestTemp.cmp,
output-list
RAM[0]%D1.6.1 RAM[256]%D1.6.1    RAM[257]%D1.6.1;

set RAM[0] 256,
set RAM[1] 300,
set RAM[2] 400,
set RAM[3] 3000,
set RAM[4] 3010,

repeat 100 {
  ticktock;
}

output;

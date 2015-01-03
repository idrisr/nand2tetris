// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/MemoryAccess/PointerTestSimple/PointerTestSimple.tst

// load PointerTestSimpleManual.asm,
load PointerTestSimple.asm,
output-file PointerTestSimple.out,
compare-to PointerTestSimple.cmp,
output-list
RAM[0]%D1.6.1
RAM[3]%D1.6.1
RAM[4]%D1.6.1
RAM[256]%D1.6.1;

set RAM[0] 256,

repeat 450 {
  ticktock;
}

output;

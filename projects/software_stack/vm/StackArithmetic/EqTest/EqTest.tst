load EqTest.asm,
output-file EqTest.out,
compare-to EqTest.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set RAM[0] 256,

repeat 20 {
  ticktock;
}

output;

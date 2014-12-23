load          NegTest.asm,
output-file   NegTest.out,
compare-to    NegTest.cmp,
output-list
RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set RAM[0] 256,

repeat 20 {
  ticktock;
}
output;

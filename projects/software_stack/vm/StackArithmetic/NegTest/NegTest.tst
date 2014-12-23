load          NegTest.asm,
output-file   NegTest.out,
compare-to    NegTest.cmp,
output-list
RAM[0]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2 RAM[258]%D2.6.2 RAM[259]%D2.6.2
RAM[260]%D2.6.2
RAM[261]%D2.6.2;

set RAM[0] 256,

repeat 150 {
  ticktock;
}
output;

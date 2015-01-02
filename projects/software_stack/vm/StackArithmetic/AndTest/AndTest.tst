load          AndTest.asm,
output-file   AndTest.out,
compare-to    AndTest.cmp,
output-list
RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set RAM[0] 256,

repeat 150 {
  ticktock;
}
output;

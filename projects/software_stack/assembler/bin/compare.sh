#!/usr/bin/env bash

rm *hack > /dev/null

echo 'Checking Add...'
python ../assembler/assm_parser.py ../add/Add.asm > Add.hack
diff -yb --suppress-common-lines Add.hack ../add/Add.hack

echo 'Chekcing MaxL...'
python ../assembler/assm_parser.py ../max/MaxL.asm > MaxL.hack
diff -yb --suppress-common-lines MaxL.hack ../max/MaxL.hack

echo 'Checking PongL...'
python ../assembler/assm_parser.py ../pong/PongL.asm > PongL.hack
diff -yb --suppress-common-lines PongL.hack ../pong/PongL.hack

echo 'Checking RectL...'
python ../assembler/assm_parser.py ../rect/RectL.asm > RectL.hack
diff -yb --suppress-common-lines RectL.hack ../rect/RectL.hack

echo 'Checking Max...'
python ../assembler/assm_parser.py ../max/Max.asm > Max.hack
diff -yb --suppress-common-lines Max.hack ../max/Max.hack

echo 'Checking Pong...'
python ../assembler/assm_parser.py ../pong/Pong.asm > Pong.hack
diff -yb --suppress-common-lines Pong.hack ../pong/Pong.hack

echo 'Checking Rect...'
python ../assembler/assm_parser.py ../rect/Rect.asm > Rect.hack
diff -yb --suppress-common-lines Rect.hack ../rect/Rect.hack

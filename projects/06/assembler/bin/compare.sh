#!/usr/bin/env bash

rm *hack > /dev/null
python ../assembler/parser.py ../../max/MaxL.asm > Max.hack
diff -yb --suppress-common-lines Max.hack ../../max/MaxL.hack

python ../assembler/parser.py ../../add/Add.asm > Add.hack
diff -yb --suppress-common-lines Add.hack ../../add/Add.hack

python ../assembler/parser.py ../../pong/PongL.asm > Pong.hack 
diff -yb --suppress-common-lines Pong.hack ../../pong/PongL.hack

python ../assembler/parser.py ../../rect/RectL.asm > Rect.hack 
diff -yb --suppress-common-lines Rect.hack ../../rect/RectL.hack

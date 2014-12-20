#!/usr/bin/env bash

CPU=${HOME}'/learning/nand2tetris/tools/CPUEmulator.sh'

echo 'Checking Simple Add'
python ../vm/vm_parser.py ../StackArithmetic/SimpleAdd/SimpleAdd.vm > ../StackArithmetic/SimpleAdd/SimpleAdd.asm
${CPU} ../StackArithmetic/SimpleAdd/SimpleAdd.tst
diff -y ../StackArithmetic/SimpleAdd/SimpleAdd.out ../StackArithmetic/SimpleAdd/SimpleAdd.cmp

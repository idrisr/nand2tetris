#!/usr/bin/env bash

CPU=${HOME}'/learning/nand2tetris/tools/CPUEmulator.sh'
PROJ_HOME=${HOME}'/learning/nand2tetris'
SOFT_HOME=${PROJ_HOME}'/projects/software_stack'
VM_HOME=${SOFT_HOME}'/vm'
SCRIPT=${SOFT_HOME}/vm/vm/vm_parser.py

function write_asm(){
    base=${VM_HOME}/$1/$2/$2
    echo ${base}
    python ${SCRIPT} ${base}.vm > ${base}.asm
}

function emulator(){
    base=${VM_HOME}/$1/$2/$2
    ${CPU} ${base}.tst
    diff -yb ${base}.cmp ${base}.out | head
}

echo 'comparing simpleadd'
write_asm StackArithmetic SimpleAdd
emulator  StackArithmetic SimpleAdd

echo ''
echo 'comparing Equal Test'
#write_asm StackArithmetic EqTest
emulator  StackArithmetic EqTest

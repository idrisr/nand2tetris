#!/usr/bin/env bash

CPU=${HOME}'/learning/nand2tetris/tools/CPUEmulator.sh'
PROJ_HOME=${HOME}'/learning/nand2tetris'
SOFT_HOME=${PROJ_HOME}'/projects/software_stack'
VM_HOME=${SOFT_HOME}'/vm'
SCRIPT=${SOFT_HOME}/vm/vm/vm_parser.py

function write_asm(){
    base=${VM_HOME}/$1/$2/$2
    rm -f ${base}.asm
    python ${SCRIPT} ${base}.vm > ${base}.asm
}

function emulator(){
    base=${VM_HOME}/$1/$2/$2
    rm -f ${base}.out
    ${CPU} ${base}.tst
    #echo "diffing ${base}.cmp and ${base}.out"
    diff -yb --suppress-common-lines ${base}.cmp ${base}.out | head
}

function run_test(){
    echo ''
    echo "comparing $1 $2"
    write_asm $1 $2
    emulator  $1 $2
}

echo 'comparing SimpleAdd Test'
run_test StackArithmetic SimpleAdd

echo 'comparing SimpleAdd2 Test'
run_test StackArithmetic SimpleAdd2

echo 'comparing SimpleAdd EqTest'
run_test StackArithmetic EqTest

echo 'comparing SimpleAdd NegTest'
run_test StackArithmetic NegTest

echo 'comparing SimpleAdd AndTest'
run_test StackArithmetic AndTest

echo 'comparing Stack Arithmetic Test'
run_test StackArithmetic StackTest

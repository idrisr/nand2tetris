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

echo 'comparing EqTest Test'
run_test StackArithmetic EqTest

echo 'comparing NegTest Test'
run_test StackArithmetic NegTest

echo 'comparing AndTest Test'
run_test StackArithmetic AndTest

echo 'comparing StackTest Test'
run_test StackArithmetic StackTest

echo 'comparing Very Basic Memory Test'
run_test MemoryAccess VeryBasicTest

echo 'comparing Push N Test'
run_test MemoryAccess PushNTest

echo 'comparing Push Segment Test'
run_test MemoryAccess PushSegmentTest

echo 'comparing Basic Memory Test with Temp Segment'
run_test MemoryAccess BasicTestTemp

echo 'comparing Basic Memory Test'
run_test MemoryAccess BasicTest

echo 'comparing Simple Pointer Test Simple'
run_test MemoryAccess PointerTestSimple

echo 'comparing Simple Pointer Simple'
run_test MemoryAccess PointerTest

echo 'comparing Static Test'
run_test MemoryAccess StaticTest

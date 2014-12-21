#!/usr/bin/env bash

CPU=${HOME}'/learning/nand2tetris/tools/CPUEmulator.sh'
PROJ_HOME=${HOME}'/learning/nand2tetris'
SOFT_HOME=${PROJ_HOME}'/projects/software_stack'

SCRIPT=${SOFT_HOME}/vm/vm/vm_parser.py
SCRIPT_ARG=${SOFT_HOME}/vm/StackArithmetic/SimpleAdd/SimpleAdd.vm
SCRIPT_OUT=${SOFT_HOME}/vm/StackArithmetic/SimpleAdd/SimpleAdd.asm

TEST=${SOFT_HOME}/vm/StackArithmetic/SimpleAdd/SimpleAdd.tst
TEST_OUT=${SOFT_HOME}/vm/StackArithmetic/SimpleAdd/SimpleAdd.out
TEST_CMP=${SOFT_HOME}/vm/StackArithmetic/SimpleAdd/SimpleAdd.cmp

function write_asm(){
    rm -f ${SCRIPT_OUT} ${TEST_OUT};
    python ${SCRIPT} ${SCRIPT_ARG} > ${SCRIPT_OUT}
}

write_asm
echo ${SCRIPT_OUT}
cat ${SCRIPT_OUT}
${CPU} ${TEST}
diff -y ${TEST_OUT} ${TEST_CMP}

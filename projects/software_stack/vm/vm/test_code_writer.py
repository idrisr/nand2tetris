#!/usr/bin/env python

from unittest import TestCase
from code_writer import CodeWriter
from vm_command import VMCommand

class TestCodeWriter(TestCase):
    def setUp(self):
        self.cw = CodeWriter()

    def clear_stack(self):
        self.cw.stack = []
        self.cw.SP = 256

    def test_write_push_constant(self):
        """ test push constant [0-9]* """

        # empty stack
        self.clear_stack()

        # need to update SP, ie RAM[0]
        asm_command = ['@7', 'D=A', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']

        command = VMCommand('push constant 7')
        command.parse_command()
        self.cw.process_command(command)
        self.assertListEqual(asm_command, self.cw.assm)

    def test_write_two_push_constant(self):
        """ push contant [0-9]* twice in a row"""

        # empty stack
        self.clear_stack()

        asm_command = ['@7', 'D=A', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
        command = VMCommand('push constant 7')
        command.parse_command()
        self.cw.process_command(command)
        self.assertEqual(asm_command, self.cw.assm)

        command = VMCommand('push constant 8')
        command.parse_command()
        self.cw.process_command(command)
        asm_command = ['@8', 'D=A', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
        self.assertEqual(asm_command, self.cw.assm)

    def test_write_add_command(self):
        """
        test popping top two items off of stack, adding them, and putting
        the result back on the stack
        """

        # empty stack
        self.clear_stack()

        # put 7 & 8 on the stack to add
        self.cw.sp.push(7)
        self.cw.sp.push(8)

        command = VMCommand('add')
        command.parse_command()
        self.cw.process_command(command)

        self.assertEqual(self.cw.sp.stack[-1], 15, self.cw)
        assm_command = ['@256', 'M=M+D', '@SP', 'M=M-1']
        self.assertListEqual(assm_command, self.cw.assm)


    def test_write_arithmetic_eq(self):
        """ test eq """
        # empty stack
        self.clear_stack()

        # put 7 & 8 on the stack to add
        self.cw.sp.push(20)
        self.cw.sp.push(20)

        command = VMCommand('eq')
        command.parse_command()
        self.cw.process_command(command)
        self.assertEqual(self.cw.sp.stack[-1], -1, self.cw)

        assm_command = [
        '@257' , 'D=M'  , '@256'  , 'D=M-D' , '@L0'   , 'D;JEQ' , '@L1'  ,
        '(L1)' , '@256' , 'M=0'   , '@L2'   , '0;JMP' , '(L0)'  , '@256' ,
        'M=-1' , '@L2'  , '0;JMP' , '(L2)'  , '@SP'   , 'M=M-1'
        ]

        self.assertListEqual(assm_command, self.cw.assm)

    def test_neg(self):
        """ test taking negative of top item on stack """
        self.clear_stack()
        self.cw.sp.push(10)

        command = VMCommand('neg')
        command.parse_command()
        self.cw.process_command(command)
        assm_command = ['@SP', 'A=M-1', 'MD=-M']
        self.assertListEqual(assm_command, self.cw.assm)


    def test_pop_to_diff_stack(self):
        """ test pushing to segment. 0 arg2 """
        # push ten onto global stack
        self.cw.sp.push(10)

        # pop it off and it goes into local
        command = VMCommand('pop local 0')
        command.parse_command()
        self.cw.process_command(command)

        assm_command = ['@LCL', 'D=M', '@0', 'D=A+D', '@R5', 'M=D', '@SP',
                'A=M-1', 'D=M', '@R5', 'A=M', 'M=D', '@SP', 'M=M-1']

        self.assertListEqual(assm_command, self.cw.assm)

    def test_pop_non0_to_diff_stack(self):
        """ test pushing to segment. non 0 arg2 """
        # push ten onto global stack
        self.cw.sp.push(10)

        # pop it off and it goes into local
        command = VMCommand('pop local 8')
        command.parse_command()
        self.cw.process_command(command)

        assm_command = ['@LCL', 'D=M', '@8', 'D=A+D', '@R5', 'M=D', '@SP',
                'A=M-1', 'D=M', '@R5', 'A=M', 'M=D', '@SP', 'M=M-1']

        self.assertListEqual(assm_command, self.cw.assm)

    def test_pop_from_segment(self):
        """ test pushing from segment onto """
        prep_commands=['push constant 12',
                       'pop local 1',
                       'push constant 21']
        for _ in prep_commands:
            command = VMCommand(_)
            command.parse_command()

        command = VMCommand('push local 1')
        command.parse_command()
        self.cw.process_command(command)

        assm_command = ['@LCL', 'D=M', '@1', 'A=A+D', 'D=M', '@SP', 'A=M',
                'M=D', '@SP', 'M=M+1']

        self.assertListEqual(assm_command, self.cw.assm)

    def test_pop_from_temp(self):
        """ test popping from TMP segment """
        prep_commands = ['push constant 510']
        for _ in prep_commands:
            command = VMCommand(_)
            command.parse_command()

        command = VMCommand('pop temp 6')
        command.parse_command()
        self.cw.process_command(command)

        assm_command = ['@SP', 'A=M-1', 'D=M', '@11', 'M=D', '@SP', 'M=M-1']

        self.assertListEqual(assm_command, self.cw.assm)

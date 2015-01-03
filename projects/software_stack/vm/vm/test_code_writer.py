#!/usr/bin/env python

from unittest import TestCase
from code_writer import CodeWriter
from vm_command import VMCommand

class TestCodeWriter(TestCase):
    def setUp(self):
        self.cw = CodeWriter()

    def process_commands(self, commands):
        for _ in commands:
            command = VMCommand(_)
            command.parse_command()
            self.cw.process_command(command)

    def test_write_push_constant(self):
        """ test push constant [0-9]* """

        # need to update SP, ie RAM[0]
        asm_command = ['@7', 'D=A', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']

        commands = ['push constant 7']
        self.process_commands(commands)
        self.assertListEqual(asm_command, self.cw.assm)

    def test_write_two_push_constant(self):
        """ push contant [0-9]* twice in a row"""

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

        # put 7 & 8 on the stack to add
        commands = ['push constant 7', 'push constant 8', 'add']
        self.process_commands(commands);

        assm_command = ['@SP', 'A=M-1', 'D=M', '@SP', 'M=M-1', '@SP', 'A=M-1',
                'M=M+D']

        self.assertListEqual(assm_command, self.cw.assm)


    def test_write_arithmetic_eq(self):
        """ test eq """
        commands = ['push constant 20', 'push constant 20', 'eq']
        self.process_commands(commands)

        assm_command = ['@SP', 'A=M-1', 'D=M', '@SP', 'M=M-1', '@SP', 'A=M-1',
                'D=M-D', '@SP', 'M=M-1', '@L%s' % 0, 'D;JEQ', '@L%s' % 1,
                '(L%s)' % 1, '@SP', 'A=M', 'M=0', '@L%s' % 2, '0;JMP', '(L%s)' %
                0, '@SP', 'A=M', 'M=-1', '@L%s' % 2, '0;JMP', '(L%s)' % 2,
                '@SP', 'M=M+1']

        self.assertListEqual(assm_command, self.cw.assm)

    def test_neg(self):
        """ test taking negative of top item on stack """
        commands = ['push constant 10']
        self.process_commands(commands)

        command = VMCommand('neg')
        command.parse_command()
        self.cw.process_command(command)
        assm_command = ['@SP', 'A=M-1', 'MD=-M']
        self.assertListEqual(assm_command, self.cw.assm)


    def test_pop_to_diff_stack(self):
        """ test popping to segment. 0 arg2 """
        # push ten onto global stack
        commands=['push constant 10', 
               'pop local 0' ]
        self.process_commands(commands)

        # pop it off and it goes into local

        assm_command = ['@LCL', 'D=M', '@0', 'D=A+D', '@R5', 'M=D', '@SP',
                'A=M-1', 'D=M', '@R5', 'A=M', 'M=D', '@SP', 'M=M-1']

        self.assertListEqual(assm_command, self.cw.assm)

    def test_pop_non0_to_diff_stack(self):
        """ test pushing to segment. non 0 arg2 """
        # push ten onto global stack
        commands = ['push constant 10',
                    'pop local 8']
        self.process_commands(commands)

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
            self.cw.process_command(command)

        command = VMCommand('pop temp 6')
        command.parse_command()
        self.cw.process_command(command)

        assm_command = ['@SP', 'A=M-1', 'D=M', '@11', 'M=D', '@SP', 'M=M-1']

        self.assertListEqual(assm_command, self.cw.assm)

    def test_push_from_temp(self):
        """ test pushing from TMP segment """
        prep_commands = ['push constant 510',
                         'pop temp 6',
                         'push constant 415']

        for _ in prep_commands:
            command = VMCommand(_)
            command.parse_command()
            self.cw.process_command(command)

        command = VMCommand('push temp 6')
        command.parse_command()
        self.cw.process_command(command)

        assm_command = ['@11', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
        self.assertListEqual(assm_command, self.cw.assm)

    def test_push_from_segment(self):
        """ test pushing from segment onto global stack """
        commands = ['push constant 510',
                         'pop local 6',
                         'push local 6']
        self.process_commands(commands)

        assm_command = ['@LCL', 'D=M', '@6', 'A=A+D', 'D=M', '@SP', 'A=M',
            'M=D', '@SP', 'M=M+1']
        self.assertListEqual(assm_command, self.cw.assm)

    def test_pop_from_pointer(self):
        """ test popping to pointer """
        commands = ['push constant 3040', 'pop pointer 0']
        self.process_commands(commands)

        assm_command = ['@SP', 'A=M-1', 'D=M', '@3', 'M=D', '@SP', 'M=M-1']
        self.assertListEqual(assm_command, self.cw.assm)

    def test_push_from_pointer(self):
        """ test pushing to pointer """
        commands = ['push constant 3040', 'pop pointer 0', 'push pointer 0']
        self.process_commands(commands)

        assm_command = ['@3', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
        self.assertListEqual(assm_command, self.cw.assm)

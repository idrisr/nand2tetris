#!/usr/bin/env python

from unittest import TestCase
from code_writer import CodeWriter
from vm_command import VMCommand

class TestCodeWriter(TestCase):
    def setUp(self):
        self.cw = CodeWriter()
        self.cw.stack = [1, 2, 'idris', 'unbuckled', 'chapal']
        for _ in self.cw.stack:
            self.cw.SP+=1

    def clear_stack(self):
        self.cw.stack = []
        self.cw.SP = 256

    def test_write_push_constant(self):
        """ test push constant [0-9]* """

        # empty stack
        self.clear_stack()

        # need to update SP, ie RAM[0]
        command = "push constant 7"
        asm_command = '\n'.join(['@7', 'D=A',  '@256', 'M=D'])
        self.command = VMCommand(command)
        self.command.parse_command()
        self.cw.command = self.command
        self.cw.write_push()
        self.assertEqual(asm_command, self.cw.assm)

    def test_write_two_push_constant(self):
        """ push contant [0-9]* twice in a row"""

        # empty stack
        self.clear_stack()

        command = "push constant 7"
        asm_command = '\n'.join(['@7', 'D=A',  '@256', 'M=D'])
        self.command = VMCommand(command)
        self.command.parse_command()
        self.cw.command = self.command
        self.cw.write_push()

        command = "push constant 8"
        asm_command = '\n'.join(['@8', 'D=A', '@257', 'M=D'])
        self.command = VMCommand(command)
        self.command.parse_command()
        self.cw.command = self.command
        self.cw.write_push()
        self.assertEqual(asm_command, self.cw.assm)

    def test_write_add_command(self):
        """ 
        test popping top two items off of stack, adding them, and putting
        the result back on the stack 
        """

        # empty stack
        self.clear_stack()

        # put 7 & 8 on the stack to add
        command = "push constant 7"
        asm_command = '\n'.join(['@7', 'D=A',  '@256', 'M=D'])
        self.command = VMCommand(command)
        self.command.parse_command()
        self.cw.command = self.command
        self.cw.write_push()

        command = "push constant 8"
        asm_command = '\n'.join(['@8', 'D=A', '@257', 'M=D'])
        self.command = VMCommand(command)
        self.command.parse_command()
        self.cw.command = self.command
        self.cw.write_push()
        self.assertEqual(asm_command, self.cw.assm)

        command = "add"
        self.command = VMCommand(command)
        self.command.parse_command()
        # thisll be set in CodeWriter.process_command()
        self.cw.command = self.command
        self.cw.write_arithmetic()
        self.assertEqual(self.cw.stack[-1], 15, self.cw)

        l = ['@256', 'M=M+D']
        asm_command = '\n'.join(l)

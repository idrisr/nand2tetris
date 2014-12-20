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

    def test_SP(self):
        """ test SP stack pointer in the right place """
        SP_before = 256 + len(self.cw.stack)
        self.assertEqual(self.cw.SP, SP_before)

        self.cw.pop()
        self.assertEqual(self.cw.SP, SP_before-1)

    def test_pop(self):
        """ test pop'ing element of the stack """
        SP_before = self.cw.SP
        last_element = self.cw.stack[-1]
        p = self.cw.pop()
        self.assertEqual(last_element, p)
        self.assertEqual(SP_before - 1, self.cw.SP)

    def test_write_push_constant(self):
        """ test push constant [0-9]* """

        # empty stack
        self.clear_stack()
        command = "push constant 7"
        asm_command = '\n'.join(['@7', 'D=A',  '@256', 'M=D'])
        self.command = VMCommand(command)
        self.command.parse_command()
        write_out = self.cw.write_push(self.command)

        self.assertEqual(asm_command, write_out)

    def test_write_two_push_constant(self):
        """ push contant [0-9]* twice in a row"""

        # empty stack
        self.clear_stack()

        command = "push constant 7"
        asm_command = '\n'.join(['@7', 'D=A',  '@256', 'M=D'])
        self.command = VMCommand(command)
        self.command.parse_command()
        write_out = self.cw.write_push(self.command)

        command = "push constant 8"
        asm_command = '\n'.join(['@8', 'D=A', '@257', 'M=D'])
        self.command = VMCommand(command)
        self.command.parse_command()
        write_out = self.cw.write_push(self.command)
        self.assertEqual(asm_command, write_out)

    def test_add_command(self):
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
        write_out = self.cw.write_push(self.command)

        command = "push constant 8"
        asm_command = '\n'.join(['@8', 'D=A', '@257', 'M=D'])
        self.command = VMCommand(command)
        self.command.parse_command()
        write_out = self.cw.write_push(self.command)
        self.assertEqual(asm_command, write_out)

        command = "add"
        self.command = VMCommand(command)
        self.command.parse_command()
        result = self.cw.write_arithmetic(self.command)
        self.assertEqual(result, 15)

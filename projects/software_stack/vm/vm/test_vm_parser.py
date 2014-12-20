#!/usr/bin/env python

from unittest import TestCase
from vm_parser import VMParser
from vm_command import VMCommand
from os import environ, path, remove

class TestVMParser(TestCase):
    def setUp(self):
        file_name = path.join(environ['HOME'], 'tmp', 'tmp.asm')
        f = open(file_name, 'w')
        f.close()
        self.parser = VMParser(file_name)
        remove(file_name)

    def test_constructor(self):
        # for existing file
        self.assertTrue(isinstance(self.parser, VMParser))

    def test_constructor_file_not_there(self):
        # for no longer existing file
        file_name = path.join(environ['HOME'], 'tmp', 'tmp.asm')
        with self.assertRaises(SystemExit) as cm:
            self.parser.__init__(file_name)
        self.assertEqual(cm.exception.code, 1)

    def test_push(self):
        """ test recognizing push commands """
        command = 'push constant 7'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.assertEqual(self.parser.command.ctype, 'C_PUSH')

        command = 'PUSH CONSTANT 7'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.assertEqual(self.parser.command.ctype, 'C_PUSH')

        command = 'POP CONSTANT 7'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.assertNotEqual(self.parser.command.ctype, 'C_PUSH', self.parser.command)

    def test_pop(self):
        """ test recognizing pop commands """
        command = 'pop argument 7'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.assertEqual(self.parser.command.ctype, 'C_POP')

        command = 'pOp arguemnt 8'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.assertEqual(self.parser.command.ctype, 'C_POP')

        command = 'push CONSTANT 7'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.assertNotEqual(self.parser.command.ctype, 'C_POP')

    def test_add_arithmetic(self):
        """ test recognizing add commands """
        command = 'add'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.assertEqual(self.parser.command.ctype, 'C_ARITHMETIC')

        command = 'notadd'
        self.parser.command = VMCommand(command)
        with self.assertRaises(SystemExit) as cm:
            self.parser.command.set_ctype()
        self.assertEqual(cm.exception.code, 1)

        command = 'pop this'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.assertNotEqual(self.parser.command.ctype, 'C_ARITHMETIC')

    def test_sub_arithmetic(self):
        """ test recognizing sub commands """
        command = 'sub'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.assertEqual(self.parser.command.ctype, 'C_ARITHMETIC')

        command = 'push that'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.assertNotEqual(self.parser.command.ctype, 'C_ARITHMETIC', self.parser.command)


    def test_invalid_command(self):
        """ test for invalid command """
        command = 'subbie'
        self.parser.command = VMCommand(command)

        with self.assertRaises(SystemExit) as cm:
            self.parser.command.set_ctype()
        self.assertEqual(cm.exception.code, 1)

    def test_arg1(self):
        """ test parse out arg1 """
        command = 'push constant 21'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.parser.command.set_arg1()
        self.assertEqual('constant', self.parser.command.arg1), self.parser.command

        command = 'pop pointer 1'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.parser.command.set_arg1()
        self.assertEqual('pointer', self.parser.command.arg1, self.parser.command)

        command = 'add'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.parser.command.set_arg1()
        self.assertEqual('add', self.parser.command.arg1)

    def test_arg1_bad_command_type(self):
        """ test parse out arg1 """
        command = 'return sum'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()

        with self.assertRaises(SystemExit) as cm:
            self.parser.command.set_arg1()
        self.assertEqual(cm.exception.code, 1)

    def test_arg2(self):
        """ test parse out arg2 """
        command = 'push constant 21'
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.parser.command.set_arg1()
        self.parser.command.set_arg2()

        self.assertEqual('21', self.parser.command.arg2)
        self.assertEqual('constant', self.parser.command.arg1)

    def test_arg2_bad_command_type(self):
        """ test parse out arg2 with bad command type """
        command = 'add'
        self.command = command
        self.parser.command = VMCommand(command)
        self.parser.command.set_ctype()
        self.parser.command.set_arg1()

        with self.assertRaises(SystemExit) as cm:
            self.parser.command.set_arg2()
        self.assertEqual(cm.exception.code, 1)

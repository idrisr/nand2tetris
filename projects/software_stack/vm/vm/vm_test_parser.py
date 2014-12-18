#!/usr/bin/env python

from unittest import TestCase
from vm_parser import VMParser
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
        self.parser.current_command = 'push constant 7'
        self.parser.command_type()
        self.assertEqual(self.parser.cur_command_type, 'C_PUSH')

        self.parser.current_command = 'PUSH CONSTANT 7'
        self.parser.command_type()
        self.assertEqual(self.parser.cur_command_type, 'C_PUSH')

        self.parser.current_command = 'POP CONSTANT 7'
        self.parser.command_type()
        self.cur_command_type = None
        self.assertNotEqual(self.parser.cur_command_type, 'C_PUSH')

    def test_pop(self):
        """ test recognizing pop commands """
        self.parser.current_command = 'pop argument 7'
        self.parser.command_type()
        self.assertEqual(self.parser.cur_command_type, 'C_POP')

        self.parser.command = 'pOp arguemnt 8'
        self.parser.command_type()
        self.assertEqual(self.parser.cur_command_type, 'C_POP')

        self.parser.current_command = 'push CONSTANT 7'
        self.parser.command_type()
        self.cur_command_type = None
        self.assertNotEqual(self.parser.cur_command_type, 'C_POP')

    def test_add_arithmetic(self):
        """ test recognizing add commands """
        self.parser.current_command = 'add'
        self.parser.command_type()
        self.assertEqual(self.parser.cur_command_type, 'C_ARITHMETIC')

        self.parser.current_command = 'notadd'
        with self.assertRaises(SystemExit) as cm:
            self.parser.command_type()
        self.assertEqual(cm.exception.code, 1)

        self.parser.current_command = 'pop this'
        self.parser.command_type()
        self.assertNotEqual(self.parser.cur_command_type, 'C_ARITHMETIC')

    def test_sub_arithmetic(self):
        """ test recognizing sub commands """
        self.parser.current_command = 'sub'
        self.parser.command_type()
        self.assertEqual(self.parser.cur_command_type, 'C_ARITHMETIC')

        self.parser.current_command = 'push that'
        self.parser.command_type()
        self.assertNotEqual(self.parser.cur_command_type, 'C_ARITHMETIC')


    def test_invalid_command(self):
        """ test for invalid command """
        self.parser.current_command = 'subbie'

        with self.assertRaises(SystemExit) as cm:
            self.parser.command_type()
        self.assertEqual(cm.exception.code, 1)

    def test_arg1(self):
        """ test parse out arg1 """
        command = 'push constant 21'
        self.parser.current_command = command
        self.parser.command_type()
        self.parser.arg1()
        self.assertEqual('constant', self.parser.curr_arg1)

        command = 'pop pointer 1'
        self.parser.current_command = command
        self.parser.command_type()
        self.parser.arg1()
        self.assertEqual('pointer', self.parser.curr_arg1)

        command = 'add'
        self.parser.current_command = command
        self.parser.command_type()
        self.parser.arg1()
        self.assertEqual('add', self.parser.curr_arg1)

    def test_arg1_bad_command_type(self):
        """ test parse out arg1 """
        command = 'return sum'
        self.parser.current_command = command
        self.parser.command_type()

        with self.assertRaises(SystemExit) as cm:
            self.parser.arg1()
        self.assertEqual(cm.exception.code, 1)

    def test_arg2(self):
        """ test parse out arg2 """
        command = 'push constant 21'
        self.parser.current_command = command

        self.parser.command_type()
        self.parser.arg1()
        self.parser.arg2()

        self.assertEqual('21', self.parser.curr_arg2)
        self.assertEqual('constant', self.parser.curr_arg1)

    def test_arg2_bad_command_type(self):
        """ test parse out arg2 """
        command = 'add'
        self.parser.current_command = command
        self.parser.command_type()

        with self.assertRaises(SystemExit) as cm:
            self.parser.arg2()
        self.assertEqual(cm.exception.code, 1)

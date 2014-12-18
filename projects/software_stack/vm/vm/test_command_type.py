#!/usr/bin/env python

from unittest import TestCase
from command_type import VMCommandType

class Test_VMCommandType(TestCase):
    def setUp(self):
        self.vmct = VMCommandType()

    def test_push(self):
        """ test recognizing push commands """
        command = 'push constant 7'
        self.vmct.command_type(command)
        self.assertEqual(self.vmct.cur_command_type, 'C_PUSH')

        command = 'PUSH CONSTANT 7'
        self.vmct.command_type(command)
        self.assertEqual(self.vmct.cur_command_type, 'C_PUSH')

        command = 'POP CONSTANT 7'
        self.vmct.command_type(command)
        self.vmct.cur_command_type = None
        self.assertNotEqual(self.vmct.cur_command_type, 'C_PUSH')

    def test_pop(self):
        """ test recognizing push commands """
        command = 'pop argument 7'
        self.vmct.command_type(command)
        self.assertEqual(self.vmct.cur_command_type, 'C_POP')

        command = 'pOp arguemnt 8'
        self.vmct.command_type(command)
        self.assertEqual(self.vmct.cur_command_type, 'C_POP')

        command = 'push CONSTANT 7'
        self.vmct.command_type(command)
        self.vmct.cur_command_type = None
        self.assertNotEqual(self.vmct.cur_command_type, 'C_POP')

    def test_add_arithmetic(self):
        """ test add commands """
        command = 'add'
        self.vmct.command_type(command)
        self.assertEqual(self.vmct.cur_command_type, 'C_ARITHMETIC')

        command = 'notadd'
        with self.assertRaises(SystemExit) as cm:
            self.vmct.command_type(command)
        self.assertEqual(cm.exception.code, 1)

        command = 'pop this'
        self.vmct.command_type(command)
        self.assertNotEqual(self.vmct.cur_command_type, 'C_ARITHMETIC')

    def test_sub_arithmetic(self):
        """ test sub commands """
        command = 'sub'
        self.vmct.command_type(command)
        self.assertEqual(self.vmct.cur_command_type, 'C_ARITHMETIC')

        command = 'push that'
        self.vmct.command_type(command)
        self.assertNotEqual(self.vmct.cur_command_type, 'C_ARITHMETIC')


    def test_invalid_command(self):
        """ test for invalid command """
        command = 'subbie'

        with self.assertRaises(SystemExit) as cm:
            self.vmct.command_type(command)
        self.assertEqual(cm.exception.code, 1)

#!/usr/bin/env python

from unittest import TestCase
from parser import Parser
from os import environ, path


class TestParser(TestCase):
    def setUp(self):
        dir = environ['HOME']
        file = 'learning/nand2tetris/projects/06/add/Add.asm'
        self.parser = Parser(path.join(dir, file))

    def test_has_more_commands(self):
        commands = len(self.parser.buff)
        if commands > 0:
            self.assertTrue(self.parser.has_more_commands)
        else:
            self.assertFalse(self.parser.has_more_commands)

    def test_advance(self):
        command = '@2'
        self.parser.advance()
        self.assertEqual(self.parser.current_command, command)

        for i in xrange(3):
            self.parser.advance()
        command = 'D=D+A'
        self.assertEqual(self.parser.current_command, command)

        for i in xrange(100):
            self.parser.advance()
        self.assertEqual(self.parser.current_command, None)

    def test_command_type(self):
        command = '@2'
        self.parser.current_command = command
        self.parser.command_type()
        self.assertEqual(self.parser.current_command_type, 'A')

        command = '@LOOP'
        self.parser.current_command = command
        self.parser.command_type()
        self.assertEqual(self.parser.current_command_type, 'L')


        command = '@aLoop'
        self.parser.current_command = command
        self.parser.command_type()
        self.assertEqual(self.parser.current_command_type, 'L')

        command = 'D=D+A'
        self.parser.current_command = command
        self.parser.command_type()
        self.assertEqual(self.parser.current_command_type, 'C')

        command = 'D;JGT'
        self.parser.current_command = command
        self.parser.command_type()
        self.assertEqual(self.parser.current_command_type, 'C')

        command = 'invalid command'
        self.parser.current_command = command

        with self.assertRaises(SystemExit) as cm:
            self.parser.command_type()
        self.assertEqual(cm.exception.code, 1)

    def test_symbol(self):
        command = '@2'
        self.parser.current_command = command
        self.parser.symbol()
        self.assertEqual(self.parser.current_symbol, '2')

        command = '@16000'
        self.parser.current_command = command
        self.parser.symbol()
        self.assertEqual(self.parser.current_symbol, '16000')

    def test_dest(self):
        command = 'AMD=D+1'
        self.parser.current_command = command
        self.parser.dest()
        self.assertEqual(self.parser.current_dest, '111')

        command = 'null'
        self.parser.current_command = command
        self.parser.dest()
        self.assertEqual(self.parser.current_dest, '000')

        command = 'FUCK=D+1'
        self.parser.current_command = command
        with self.assertRaises(SystemExit) as cm:
            self.parser.dest()
        self.assertEqual(cm.exception.code, 1)

    def test_comp(self):
        command = 'AMD=D+1'
        self.parser.current_command = command
        self.parser.comp()
        self.assertEqual(self.parser.current_comp, '011111')

        command = 'AMD=D|A'
        self.parser.current_command = command
        self.parser.comp()
        self.assertEqual(self.parser.current_comp, '010101')

        command = 'D+1=FUCK'
        self.parser.current_command = command
        with self.assertRaises(SystemExit) as cm:
            self.parser.comp()
        self.assertEqual(cm.exception.code, 1)

        command = 'D;JGT'
        self.parser.current_command = command
        self.parser.comp()
        self.assertEqual(self.parser.current_comp, '001100')

        command = 'D=JGT'
        self.parser.current_command = command
        with self.assertRaises(SystemExit) as cm:
            self.parser.comp()

    def test_jump(self):
        command = 'D;JGT'
        self.parser.current_command = command
        self.parser.jump()
        self.assertEqual(self.parser.current_jump, '001')

        command = '0;null'
        self.parser.current_command = command
        self.parser.jump()
        self.assertEqual(self.parser.current_jump, '000')

        command = '150;JLT'
        self.parser.current_command = command
        self.parser.jump()
        self.assertEqual(self.parser.current_jump, '100')

        command = '10;WTF'
        self.parser.current_command = command
        with self.assertRaises(SystemExit) as cm:
            self.parser.jump()
        self.assertEqual(cm.exception.code, 1)

        command = '@2LOOP'
        self.parser.current_command = command
        with self.assertRaises(SystemExit) as cm:
            self.parser.jump()
        self.assertEqual(cm.exception.code, 1)

    def test_binarize_c_commands(self):
        #test case from Max.asm and Max.hack
        command = '0;JMP'
        bin_command = '1110101010000111'
        self.parser.current_command = command
        self.parser.binarize_c_command()
        self.assertEqual(self.parser.bin_current, bin_command)

        command = 'D;JGT'
        bin_command = '1110001100000001'
        self.parser.current_command = command
        self.parser.binarize_c_command()
        self.assertEqual(self.parser.bin_current, bin_command)

    def test_binarize_a_commands(self):
        command = '@14'
        bin_command = '0000000000001110'
        self.parser.current_command = command
        self.parser.binarize_a_command()
        self.assertEqual(self.parser.bin_current, bin_command)

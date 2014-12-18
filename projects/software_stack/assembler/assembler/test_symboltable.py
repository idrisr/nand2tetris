#!/usr/bin/env python

from unittest import TestCase
from os import path, environ
from assm_parser import AssmParser

class TestSymbolTable(TestCase):
    longMessage = True
    def setUp(self):
        dir = environ['HOME']
        file = 'learning/nand2tetris/projects/software_stack/assembler/rect/Rect.asm'
        self.parser = AssmParser(path.join(dir, file))

    def test_keys(self):
        self.assertTrue(self.parser.symbol_table.contains('@INFINITE_LOOP'))

    def test_reserved_address(self):
        """ test whether symbol table address being set properly """
        self.assertEqual(self.parser.symbol_table.get_address('@SCREEN'), 16384)
        self.assertEqual(self.parser.symbol_table.get_address('@R4'), 4)
        self.assertEqual(self.parser.symbol_table.get_address('@INFINITE_LOOP'),
                23, 'failure messaege')

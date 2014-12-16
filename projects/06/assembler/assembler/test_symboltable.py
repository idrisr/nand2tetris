#!/usr/bin/env python

from unittest import TestCase
from os import path, environ
from parser import Parser
from symboltable import SymbolTable

class TestSymbolTable(TestCase):
    longMessage = True
    def setUp(self):
        dir = environ['HOME']
        file = 'learning/nand2tetris/projects/06/rect/Rect.asm'
        parser = Parser(path.join(dir, file))
        self.symbol_table = SymbolTable(parser.buff)
        self.symbol_table.find_symbols()
        self.keys = [
                '@INFINITE_LOOP',
                 '@counter',
                 '@address',
                 '@LOOP',
                 ]

    def test_find_symbols_len(self):
        self.assertEqual(len(self.symbol_table.table), 27);
        for k in self.keys:
            self.assertIn(k, self.symbol_table.table)

    def test_get_address(self):
        addresses = range(1024, 1024 + len(self.keys))
        for k, v in zip(self.keys, addresses):
            self.assertEqual(self.symbol_table.get_address(k), v)

    def test_reserved_address(self):
        self.assertEqual(self.symbol_table.get_address('@SCREEN'), 16384)
        self.assertEqual(self.symbol_table.get_address('@R4'), 4)

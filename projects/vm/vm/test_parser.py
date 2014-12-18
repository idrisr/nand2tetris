#!/usr/bin/env python

from unittest import TestCase
from parser import Parser
from os import environ, path, remove

class TestParser(TestCase):
    def test_constructor(self):
        file_name = path.join(environ['HOME'], 'tmp', 'tmp.asm')
        f = open(file_name, 'w')
        f.close()

        p = Parser(file_name)
        self.assertTrue(isinstance(p, Parser))

        remove(file_name)

        with self.assertRaises(SystemExit) as cm:
            p = Parser(file_name)
        self.assertEqual(cm.exception.code, 1)

    def test_constructor_file_not_there(self):
        file_name = path.join(environ['HOME'], 'tmp', 'tmp.asm')

        with self.assertRaises(SystemExit) as cm:
            Parser(file_name)
        self.assertEqual(cm.exception.code, 1)

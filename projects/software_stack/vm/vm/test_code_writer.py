#!/usr/bin/env python

from unittest import TestCase
from code_writer import CodeWriter

class TestCodeWriter(TestCase):
    def setUp(self):
        self.cw = CodeWriter()
        self.cw.stack = [1, 2, 'idris', 'unbuckled', 'chapal']
        for _ in self.cw.stack:
            self.cw.SP+=1

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

    def test_write_push_pop(self):
        """ test write_push_pop function """
        pass
        #arg

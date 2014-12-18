#!/usr/bin/env python

from unittest import TestCase
from parser import Parser
from os import environ, path, remove
from StringIO import StringIO

class TestParser(TestCase):
    def setUp(self):
        file_name = path.join(environ['HOME'], 'tmp', 'tmp.asm')
        f = open(file_name, 'w')
        f.close()
        self.parser = Parser(file_name)
        remove(file_name)

    def test_comment_strip(self):
        """ test comment stripping """

        commands = """// this is a comment
        this is not a comment
        here is a trailing comment // comment
        """
        s = StringIO()
        s.write(commands)
        s.seek(0)
        self.parser.buff = s.readlines()
        self.parser.file_clean()
        l = ['this is not a comment',
        'here is a trailing comment']

        self.assertListEqual(l, self.parser.buff)

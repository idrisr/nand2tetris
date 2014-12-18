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

#!/usr/bin/env python

from unittest import TestCase
from vm_parser import VMParser
from os import environ, path, remove

class TestVMParser(TestCase):
    def test_constructor(self):
        file_name = path.join(environ['HOME'], 'tmp', 'tmp.asm')
        f = open(file_name, 'w')
        f.close()

        p = VMParser(file_name)
        self.assertTrue(isinstance(p, VMParser))

        remove(file_name)

        with self.assertRaises(SystemExit) as cm:
            p = VMParser(file_name)
        self.assertEqual(cm.exception.code, 1)

    def test_constructor_file_not_there(self):
        file_name = path.join(environ['HOME'], 'tmp', 'tmp.asm')

        with self.assertRaises(SystemExit) as cm:
            VMParser(file_name)
        self.assertEqual(cm.exception.code, 1)

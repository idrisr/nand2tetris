#!/usr/bin/env python

import sys
from parser import Parser

class VMParser(Parser):
    def __init__(self, file_name):
        # test file exists
        # if not exit 1
        try:
            self.file = open(file_name, 'r')
            self.file_name = file_name
            self.read_file()

        except IOError, e:
            print e
            sys.exit(1)
        finally:
            self.file.close()


    def command_type(self):
        pass


    def arg1(self):
        pass


    def arg2(self):
        pass

class CodeWriter(object):
    def __init__(self):
        pass


    def set_file_name(self):
        pass


    def write_arithmetic(self):
        pass


    def write_push_pop(self):
        pass


    def close(self):
        pass

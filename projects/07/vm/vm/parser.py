#!/usr/bin/env python

import sys

class Parser(object):
    def __init__(self, file_name):
        # test file exists
        # if not exit 1
        try:
            self.file = open(file_name, 'r')

        except IOError, e:
            print e
            sys.exit(1)


    def has_more_commands(self):
        pass

    def advance(self):
        pass

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

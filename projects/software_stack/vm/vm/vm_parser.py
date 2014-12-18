#!/usr/bin/env python

import sys
import re
from parser import Parser
from command_type import VMCommandType

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

        self.vmct = VMCommandType()

    def command_type(self):
        arith_commands = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']
        arith_re = r'|'.join(['^%s$' % _ for _ in arith_commands])
        funcs = {
            'C_ARITHMETIC' : lambda x : re.match(arith_re          , x , re.I) ,
            'C_PUSH'       : lambda x : re.match(r'^push\s.*$'     , x , re.I) ,
            'C_POP'        : lambda x : re.match(r'^pop\s.*$'      , x , re.I) ,
            'C_LABEL'      : lambda x : re.match(r'^label\s.*$'    , x , re.I) ,
            'C_GOTO'       : lambda x : re.match(r'^goto\s.*$'     , x , re.I) ,
            'C_IF'         : lambda x : re.match(r'^if\s.*$'       , x , re.I) ,
            'C_FUNCTION'   : lambda x : re.match(r'^function\s.*$' , x , re.I) ,
            'C_RETURN'     : lambda x : re.match(r'^return\s.*$'   , x , re.I) ,
            'C_CALL'       : lambda x : re.match(r'^call\s.*$'     , x , re.I)
        }

        self.cur_command_type = None
        for k, v in funcs.items():
            if v(self.current_command):
                self.cur_command_type = k
                break

        if self.cur_command_type is None:
            print '%s\tinvalid command' % (self.current_command, )
            sys.exit(1)

    def arg1(self):
        if self.cur_command_type == 'C_RETURN':
            print '%s\tInvalid Command Type' % (self.cur_command_type, )
            sys.exit(1)
        elif self.cur_command_type == 'C_ARITHMETIC':
            self.curr_arg1 = self.current_command
        else:
            self.curr_arg1 = self.current_command.split()[1]

    def arg2(self):
        if self.cur_command_type in {'C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL'}:
            self.curr_arg2 = self.current_command.split()[2]
        else:
            print '%s\tInvalid Command Type' % (self.cur_command_type, )
            sys.exit(1)

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

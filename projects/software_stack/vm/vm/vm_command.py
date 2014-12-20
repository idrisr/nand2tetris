#!/usr/bin/env python

import sys
import re

class VMCommand(object):
    def __init__(self, command):
        self.command = command

    def parse_command(self):
        self.set_ctype()
        self.set_arg0()
        self.set_arg1()

        if self.ctype in {'C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL'}:
            self.set_arg2()

    def set_ctype(self):
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

        self.ctype = None
        for k, v in funcs.items():
            if v(self.command):
                self.ctype = k
                break

        if self.ctype is None:
            print '%s\tinvalid command' % (self.command, )
            sys.exit(1)

    def set_arg0(self):
            pass

    def set_arg1(self):
        if self.ctype == 'C_RETURN':
            print '%s\tInvalid Command Type' % (self.ctype, )
            sys.exit(1)
        elif self.ctype == 'C_ARITHMETIC':
            self.arg1 = self.command
        else:
            self.arg1 = self.command.split()[1]

    def set_arg2(self):
        if self.ctype in {'C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL'}:
            self.arg2 = self.command.split()[2]
        else:
            print '%s\tInvalid Command Type' % (self.ctype, )
            sys.exit(1)

    def __repr__(self):
        attributes = ['command', 'type', 'arg0', 'arg1', 'arg2']
        return ''.join(['%s\n' % getattr(self, _, '') for _ in attributes])

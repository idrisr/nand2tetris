import re
import sys

class VMCommandType(object):
    def __init__(self):
        pass

    def command_type(self, command):
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
            if v(command):
                self.cur_command_type = k
                break

        if self.cur_command_type is None:
            print '%s\tinvalid command' % (command, )
            sys.exit(1)

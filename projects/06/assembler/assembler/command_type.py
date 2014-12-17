import re
import sys

class CommandType(object):
    def command_type(self):
        """
        returns the type of the current command

        returns one of:
        A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
        C_COMMAND for dest=comp; jump
        L_COMMAND (actually, pseudo-command) for (Xxx) where Xxx is a symbol
        """

        commands = {'A': (lambda x: re.match(r'^@.*$', x)),
                    'C': ((lambda x: re.match(r'^.*=.*$', x)),
                          (lambda x: re.match(r'^.*;.*$', x))),
                    'L': (lambda x: re.match(r'^\(.*\)$', x))
                        }

        if commands['A'](self.current_command):
            self.current_command_type = 'A'
        elif commands['C'][0](self.current_command) or commands['C'][1](self.current_command):
            self.current_command_type = 'C'
        elif commands['L'](self.current_command):
            self.current_command_type = 'L'
        else:
            print '%s\tinvalid syntax' % (self.current_command, )
            sys.exit(1)

#!/usr/bin/env python

from parser import Parser
from vm_command import VMCommand

class VMParser(Parser):
    """ holds memory state, like SP poinger """

    def __init__(self, file_name):
        super(VMParser, self).__init__(file_name)

    def advance(self):
        """
        Reads the next command from the input and makes it the current
        command.  Should be called only if hasMoreCommands is True.  Initially
        there is no current command
        """
        if self.has_more_commands():
            self.current_command = VMCommand(self.buff[self.command_i])
            self.command_i = self.command_i + 1
        else:
            self.current_command = None

if __name__ == '__main__':
    pass
    #while more commands:
        #code_writer(VMParser.cur_command)

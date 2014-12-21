#!/usr/bin/env python

from parser import Parser
from vm_command import VMCommand
from code_writer import CodeWriter
from os import path, environ
import sys

class VMParser(Parser):
    """ holds memory state, like SP poinger """
    def advance(self):
        """
        Reads the next command from the input and makes it the current
        command.  Should be called only if hasMoreCommands is True.  Initially
        there is no current command
        """
        if self.has_more_commands():
            self.command = VMCommand(self.buff[self.command_i])
            self.command_i = self.command_i + 1
        else:
            self.command = None

    def __repr__(self):
        attributes = ['self.buff', 'file_name', 'command_i']
        return ''.join(['%s\n' % getattr(self, _, '') for _ in attributes])


def main(vmfile):
    vmparser = VMParser(vmfile)
    cw = CodeWriter()

    while True:
        vmparser.advance()
        cw.process_command(vmparser.command)

        if not vmparser.has_more_commands():
            break


if __name__ == '__main__':
    try:
        vmfile = sys.argv[1]
    except IndexError:
        dir = environ['HOME']
        file = 'learning/nand2tetris/projects/software_stack/vm/StackArithmetic/SimpleAdd/SimpleAdd.vm'
        vmfile = path.join(dir, file)

    main(vmfile)

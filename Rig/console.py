from cmd import Cmd
import os
import sys
from platform import platform
from Hold.filesystem_gate import swallow_file, append_to_file, dump_in_file, are_files_in, is_file_in

class Cmdline(Cmd):
    history_file = "command_history.txt"
    completion_file = "autocomplete.txt"
    
    def __init__(self):
        super().__init__()
        if platform.__name__ == "Linux":
            self.rl = getattr(__import__('readline'))
        else:
            pass
        if (is_file_in(os.getcwd(), self.history_file, False)):
            self.history = self.recover_history()
        if (is_file_in(os.getcwd(), self.completion_file, False)):
            self.completion = self.recover_completion()
            
    def emptyline(self):
        pass
        
    def append_history(self, command):
        append_to_file(self.history_file, command)
        
    def append_autocomplete(self, keyword, command):
        append_to_file(self.completion_file, keyword + ':', command)
        
    def recover_history(self):
        history_contents = swallow_file(self.history_file)
        return(list([line.strip('\r') for line in history_contents.split('\n')]).reverse())
    
    def recover_completion(self):
        autocomplete_contents = swallow_file(self.completion_file)
        return(list([line for line in autocomplete_contents.split('\n')]))

    def nope(self):
        print("Nope, never heard of that. Sorry.")
        
    def std_loop(self):
        self.intro="Hello, what should I build?"
        self.completion_matches = list()
        self.completion_matches.append('mat')
        self.default="nope"
        self.prompt="Idle. ->"
        self.cmdloop()
cmd = Cmdline()
cmd.std_loop()
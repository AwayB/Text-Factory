from prompt_toolkit import prompt, print_formatted_text, ANSI
from prompt_toolkit.formatted_text import FormattedText
import pygments
import os
import sys
from platform import platform
from Hold.filesystem_gate import swallow_file, append_to_file, dump_in_file, are_files_in, is_file_in

text = FormattedText([
    ('#ff0066', 'Hello'),
    ('', ' '),
    ('#44ff00 italic', 'World'),
])

print_formatted_text(text)
print_formatted_text(ANSI('\x1b[31mhello \x1b[32mworld'))

# class Cmdline(prompt):
#     history_file = "command_history.txt"
#     completion_file = "autocomplete.txt"
    
#     def __init__(self):
#         super().__init__()
#         if (is_file_in(os.getcwd(), self.history_file, False)):
#             self.history = self.recover_history()
#         if (is_file_in(os.getcwd(), self.completion_file, False)):
#             self.completion = self.recover_completion()
            
#     def emptyline(self):
#         pass
        
#     def append_history(self, command):
#         append_to_file(self.history_file, command)
        
#     def append_autocomplete(self, keyword, command):
#         append_to_file(self.completion_file, keyword + ':', command)
        
#     def recover_history(self):
#         history_contents = swallow_file(self.history_file)
#         return(list([line.strip('\r') for line in history_contents.split('\n')]).reverse())
    
#     def recover_completion(self):
#         autocomplete_contents = swallow_file(self.completion_file)
#         return(list([line for line in autocomplete_contents.split('\n')]))

#     def default(self, line):
#         print("'"+ line +"'?", "Don't know that command, sorry.")
        
#     def do_parse(self, line):
#         print('parsing', line)
        
#     def do_EOF(self, line):
#         return True
        
#     def std_loop(self):
#         self.intro="Hello, what should I build?"
#         self.completion_matches = list()
#         self.completion_matches.append('mat')
#         self.prompt="Idle. ->"
#         self.cmdloop()
        
def engage():
    pass
    # cmd = Cmdline()
    # cmd.std_loop()

if __name__ == '__main__':
    engage()
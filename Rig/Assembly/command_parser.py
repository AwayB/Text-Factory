#This is where the given command is broken down and assembled into python-compatible commands.

flags_dict = rig_settings_recovery()

def _entry_to_exit(commands):
    """The first argument given to the Rig is tested for compatibility, as well as the last one.
    This is a security check so as to avoid possible false commands.
    Commands such as "Get Website and Find value in it" that ask for an 'it' aka a stored former Master that was never stored will be rejected."""
    status = ("order", "flag", "value")
    for entry in commands:
        if (entry)

def _rig_parse(command):
    """"""
    pass

def treat_command(command):
    """"""
    command_list = command.split(" ")
    _entry_to_exit(command_list)
    _rig_parse(command_list)
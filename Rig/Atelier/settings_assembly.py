import re


class std_settings():
    """Settings files can be any format, but they must eventually fall down to dicts, sets, lists or tuples.
    All specialised settings will eventually have to inherit from std_settings for serialization."""
    filename = None
    target = None
    
    dict_format = re.compile(r"\w+\n((\w+): (\w+)[ \n])*")
    iterable_format = re.compile("")
    comment_format = re.compile("(#.*\n)")
    iterables_format = None
    settings = None
    
    def __init__(self, filename, target=None):
        "On startup if given a filename and target settings value, it will automatically load that value into settings."
        self.filename = filename
        self.target = target
    
    def _comments_out(self):
        pass
    
    def append(self, appendix):
        pass
    
    def _reload(self, target):
        pass
    
    def _dict(self, target, format=None):
        format = self.dict_format if format == None else format 
    
    def _iterable(self, target, format=None):
        format = self.iterables_format if format == None else format 
        pass
    
    def _getByName(self, name):
        pass
    
    def _type_checker(self, feed):
        pass
    
    def parse_setting(self, setting):
        pass
    
    def parse_all(self, filename):
        pass
    
    
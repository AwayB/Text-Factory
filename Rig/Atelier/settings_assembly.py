
class std_settings():
    """Settings files can be any format, but they must eventually fall down to dicts, sets, lists or tuples.
    All specialised settings will eventually have to inherit from std_settings for serialization."""
    def __init__(self):
        pass
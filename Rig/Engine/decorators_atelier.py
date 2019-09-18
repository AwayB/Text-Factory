from utils import contents

def status(func):
    def current(**kwargs):
        contents(func.__dict__)
        return(func.__dict__)
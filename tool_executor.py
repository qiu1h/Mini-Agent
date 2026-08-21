import json
from tools import *

def executor(name, argument):
    func = Tool_Map[name]
    args = json.loads(argument)
    return func(**args)
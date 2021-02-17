import pandas as pd
import sys

def load_settings():
    params = sys.argv
    if params[1] == "-i":
        filename = params[2]
        return pd.read_json(filename)
    else:
        raise Exception("Unsupported parameter in command")



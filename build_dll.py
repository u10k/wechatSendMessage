# build_dll.py
from ctypes import *
import os

# Load the Python DLL
python_dll = cdll.LoadLibrary("python310.dll")

# Load the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))
send = CDLL(os.path.join(script_dir, "send_message.py"))

# Define the function signature
send.test.restype = c_char_p
send.test.argtypes = [c_char_p]

# Define a wrapper function that calls the Python script
def send_wrapper(str):
    return send.test(str.encode("utf-8"))

# Expose the wrapper function to C
SENDFUNC = CFUNCTYPE(c_char_p, c_char_p)(send_wrapper)

# Export the function
__all__ = ["SENDFUNC"]

from ctypes import *
# either
libc = cdll.LoadLibrary(r"libzkfp.so")
# or
#libc = CDLL("libc.so.6")

from ctypes import *
# either
libc = cdll.LoadLibrary("libzkfp.so")
# or
#libc = CDLL("libc.so.6")

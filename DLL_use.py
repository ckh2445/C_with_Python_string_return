import ctypes

def convert_ctype(x):
    return x.encode('utf-8')

def decode_ctype(x):
    return str(ctypes.c_char_p(x).value.decode('utf-8'))

mydll = ctypes.CDLL('./Make_DLL/x64/Release/Make_DLL.dll')

# my_id = "ckh2445"
# c_id = ctypes.c_char_p(my_id.encode('utf-8'))

# print(c_id)
# result = mydll.Login(my_id)

# print(result)
# result = ctypes.c_char_p(result.encode('utf-8'))

# print(result)


my_str = convert_ctype('hello world')
result = mydll.strTest(my_str)
result = decode_ctype(result)

print(result) # hello world
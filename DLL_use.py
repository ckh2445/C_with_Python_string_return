import ctypes

def convert_ctype(x):
    return x.encode('utf-8')

def decode_ctype(x):
    return str(ctypes.c_char_p(x).value.decode('utf-8'))

mydll = ctypes.CDLL('./Make_DLL/x64/Release/Make_DLL.dll')

my_str = convert_ctype('hello world')
# print(type(my_str))
# print(my_str)
result = mydll.strTest(my_str)
print('\n' + str(result))
result = decode_ctype(result)

print(result) # hello world
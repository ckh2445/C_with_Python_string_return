import ctypes

def convert_ctype(x):
    return x.encode('utf-8')

def decode_ctype(x):
    return str(ctypes.c_char_p(x).value.decode('utf-8'))

mydll = ctypes.CDLL('./Make_DLL/x64/Release/Make_DLL.dll')

my_id = "test_id".encode('utf-8')
my_pw = "test_pw".encode('utf-8')

result = mydll.Login(my_id,my_pw)

result = decode_ctype(result)
print('\n' + "test"+ '\n' +str(result))
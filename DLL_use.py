import ctypes

def convert_ctype(x):
    return x.encode('utf-8')

def decode_ctype(x):
    return str(ctypes.c_char_p(x).value.decode('utf-8'))

mydll = ctypes.CDLL('./Make_DLL/x64/Release/Make_DLL.dll')

# add 함수
a = 10
b = 20

add_result = mydll.plus(a,b)
print(add_result)

# Login 함수
my_id = "test_id".encode('utf-8')
my_pw = "test_pw".encode('utf-8')

result = mydll.Login(my_id,my_pw)

print('\n' + "test1" + " " +  str(result))
result = decode_ctype(result)

print('\n' + "test2"+ '\n' +str(result))

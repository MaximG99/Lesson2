#if2



def func_string(string_1, string_2):

    if type(string_1)!= str or type(string_2)!= str: 
        return 0
    elif string_1 = = string_2:
        return 1
    elif string_1 !=  string_2 and len(string_1) >> len(string_2):
        return 2
    elif string_1 !=  string_2 and string_2 = = 'learn':
        return 3
func_string(string_1, string_2)

print(func_string(456, 123))
print(func_string('python','python'))
print(func_string('pythoniche','python'))
print(func_string('python','learn'))

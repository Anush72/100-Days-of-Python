# Function with Outputs

def format_name(f_name,l_name):
    formated_name = f_name.title() +' ' + l_name.title()
    return formated_name

print(format_name('anush','giri'))


# why we use return output -- to pass the output in another function or use is as we want
def function_1(text):
    return text + text

def function_2(text):
    return text.title()


output = function_2(function_1('hello'))
print(output)
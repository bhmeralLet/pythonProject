# def -> to define a function
# method

def hello_there():
    print('hello there')
hello_there()
print('=================')


# with parameters
def hello_there(name):
    print('hello there', name)
hello_there('baha')
print('=================')

# return
# we do not need to give data type to the function for the return like Java
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'en':
        return 'Hello'
    else:
        return 'bipburp'

print(greet('en'), 'Baha')
print(greet('es'), 'Baha')
print(greet('34'), 'Baha')




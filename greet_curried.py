def greet_curried(greeting):
    def greet(name):
        print(greeting + ', ' + name)
    return greet

greet_hello = greet_curried('Hello')

greet_hello('German')
greet_hello('Ivan')

# или напрямую greet_curried
xxx=dict()
greet_curried('Hi')('Roma')
xxx["Hello"] = greet_curried('Hello')
xxx["Hi"] = greet_curried('Hi')
xxx["Привет"] = greet_curried('Привет')
xxx["Привет"]("Roma")
xxx["Hi"]("Roma")
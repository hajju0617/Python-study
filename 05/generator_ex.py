def generator_ex():
    yield '1'
    yield '2'
    yield '3'

generator_var = generator_ex()
print(type(generator_var))
print(next(generator_var))
print(next(generator_var))
print(next(generator_var))
print(next(generator_var))
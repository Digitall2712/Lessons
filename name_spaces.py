def test_function():
    a = 5
    b = a ** 3
    print(f'b from test_function:{b=:}')
    def inner_function():
        print("Я в области видимости функции test_function")
        b = a * 10
        print (f'b from inner_function:{b=:}')

    return inner_function()

test_function()  # executable
inner_function() # not visible from this namespace

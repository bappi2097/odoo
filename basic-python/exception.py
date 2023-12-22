def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print('division by zero')
    except NameError as err:
        print(err)
    else:
        print('result is', result)
    finally:
        print('executing finally clause')

divide(3, 0)
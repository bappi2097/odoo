def outerFunction(text):
    def innerFunction():
        print(text)

    return innerFunction

if __name__ == '__main__':
    myFunction = outerFunction('hello world')
    myFunction()
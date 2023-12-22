with open("workfile.txt", mode="a+") as file:
    file.write("hello world\n")
    file.seek(0)
    read_data = file.read()
    print(read_data)
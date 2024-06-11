def swapFileData():
    file1 = input("What is the first file name? ")

    file2 = input("What is the second file name? ")

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as a:
        data_b = a.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as a:
        a.write(data_a)

    print(f"{file1} after swap:\n{data_b}")
    print(f"{file2} after swap:\n{data_a}")

swapFileData()

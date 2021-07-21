if __name__ == '__main__':
    x = []
    for i in range(0, 3):
        print(str(i) + ". Give me number!")
        x.append(int(input("Type in: ")))
    x = sorted(x)
    print("The biggest number: " + str(x[2]))


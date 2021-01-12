if __name__ == "__main__":
    list_1 = [1, 2, 3, 4]
    for el in list_1:
        print(el, end=" ")
    print("general")
    for el in range(len(list_1)):
        print(list_1[el], end=" ")
    print("range")
    # ________________________________________
    list_2 = [5, 6, 7, 8]
    print(list(zip(list_1, list_2)), end=" ")
    print("zip")
    print("Zip:")
    for a,b in zip(list_1, list_2):
        print(a, b, sep=" - ")
    # ________________________________________
    print("Enumerate:")
    test_str = "A random"
    for index, el in enumerate(test_str):
        print(index, el, sep=" - ")



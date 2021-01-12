import namespaces


if __name__ == '__main__':
    atr_key = namespaces.__dict__.keys()
    print(list(atr_key))
    new_atr = [name for name in atr_key if  not name.startswith("__")]
    print(new_atr)
    namespaces.__dict__['function']()


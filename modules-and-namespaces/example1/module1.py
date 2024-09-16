print("--------------Running {0}--------------".format(__name__))

def pprint_dict(header, d):
    print("\n\n--------------{0}--------------".format(header))
    for key, value in d.items():
        print("{0} = {1}".format(key, value))

pprint_dict("module1.globals", globals())
print("--------------End of {0}--------------".format(__name__))
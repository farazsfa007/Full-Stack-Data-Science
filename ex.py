try:
    result = 10.0 / 0.0
except FloatingPointError as e:
    print("Caught an Floating poit error: {}".format(e) )
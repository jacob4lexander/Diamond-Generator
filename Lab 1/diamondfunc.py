def build_diamond(length:int, program:str):

    for i in range(length):
        if (i < int(length/2)):
            print((('*|*' * ((i * 2) + 1))).center((length *3), '-'))
        elif (i == int(length/2)):
            print(program.center((length*3), '-'))
        elif (i > int(length/2)):
            print((('*|*' * (((length - i) * 2) - 1))).center((length *3), '-'))

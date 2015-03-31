def member(x, xs):
    check = False
    
    for i in xs:
        if x == i:
            check = True
            break

    return check

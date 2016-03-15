def move(n, a, b, c):
    if n == 1:
        print('{0} ----> {1}'.format(a,c))
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

n = int(input("Please input hanoi layers: "))
move(n,"A","B","C")
    

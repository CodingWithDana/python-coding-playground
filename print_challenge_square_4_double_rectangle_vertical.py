for i in range(11):
    for j in range (11):
        if i == 0 or i == 10:
            print("*", end = ' ')
        else:
            if j == 0 or j == 5 or j == 10:
               print("*", end = ' ')
            else:
                print(" ", end = ' ')
    print()
    
    
    

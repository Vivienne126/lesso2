def square(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*" , end="  ")
            iteration=iteration+1
        print("")
    print(f"When n is {n} the iteration is {iteration} ")

#Complexity 0(n square)
square(5)
square(10)

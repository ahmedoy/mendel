import random

trait_dic = { "dom0":"black(dom)" , "rec0":"white(rec)" , "dom1":"tall(dom)" , "rec1":"short(rec)" }

def verdict(x):
    if dom[x] in off1[x]:
        #print("The final result for trait 1 is dominant")
        return("dom" + str(x))

    else:
        #print("The final result for trait 1 is recessive")
        print()
        return("rec"+str(x))




 
#dominant  traits
dom = ["X","Y"]
#recessive traits
rec = ["x","y"]



#traits
t1 = ["X","x"]
t2 = ["Y","y"]

#all

ALL = (t1,t2)



while True:

    
    #parent1
    #par1 =[["X","x"],["Y","y"]]
    ran1_1 = random.randint(0,1)
    ran1_2 = random.randint(0,1)
    z1_1 = ALL[0][ran1_1]
    z1_2 = ALL[1][ran1_2]
    z1 = [z1_1,z1_2]
    print(z1)

    #parent2
    #par2 = [["X","x"],["Y","y"]]
    ran2_1 = random.randint(0,1)
    ran2_2 = random.randint(0,1)
    z2_1 = ALL[0][ran2_1]
    z2_2 = ALL[1][ran2_2]
    z2 = [z2_1,z2_2]
    print(z2)

    #useless pat just for fun
    print()
    print("generating ...........")
    print()
    
    #offspring
    off1 = [[z1_1,z2_1],[z1_2,z2_2]] #DECLARING OFF SPRING
    print(off1)
    print()
    print(off1[0])
    print()
    print(off1[1])
    print()
    print()

    #deciding trait 1
    print(trait_dic[verdict(0)])
    print()

    #deciding trait 2   
    print(trait_dic[verdict(1)])
    print()
    
    #loop wait
    y = input()


    #parent 3
    


        




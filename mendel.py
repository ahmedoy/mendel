import random

#Rules , first dom means dominant trait , while rec means recessive trait
# dom + dom = dom
# dom + rec = dom
# rec + dom = dom
# rec + rec = rec
# so the recessive trait only appears if no dominant trait is there and thats the idea of the program to check if there is a dominant trait or not




#The traits with (dom) are dominant , while those with (rec) are recessive
#The list of keys and their corresponding traits , dom refers to dominant while rec refers to recessive ,  THE ONLY TRAITS TILL now refer to colour and length
trait_dic = { "dom0":"black(dom)" , "rec0":"white(rec)" , "dom1":"tall(dom)" , "rec1":"short(rec)" }


#a function that decides whether the offspring will be observed to have dominant or recessive trait
def verdict(x):
    if dom[x] in off1[x]:
        
        return("dom" + str(x))

    else:
        
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
    ran1_1 = random.randint(0,1)#random number to choose the first trait for parent 1
    ran1_2 = random.randint(0,1)#random number to choose second  trait  for parent 1
    z1_1 = ALL[0][ran1_1]
    z1_2 = ALL[1][ran1_2]
    z1 = [z1_1,z1_2]#final chosen traits from parent 1
    print(z1)

    #parent2
    ran2_1 = random.randint(0,1)#random number to choose the first trait for parent 2
    ran2_2 = random.randint(0,1)#random number to choose the second trait for parent 2
    z2_1 = ALL[0][ran2_1]
    z2_2 = ALL[1][ran2_2]
    z2 = [z2_1,z2_2]#final chosen traits from parent 2
    print(z2)

    
    print("generating ...........")
    print()
    
    #offspring
    off1 = [[z1_1,z2_1],[z1_2,z2_2]] # OFF SPRING inherited traits
    print(off1)
    print()
    print(off1[0])#showing the colour traits remember the X & x refer to colour
    print()
    print(off1[1])#showing the length traits  remember the Y & y refer to length
    print()
    print()

    #deciding trait 1
    print(trait_dic[verdict(0)])#running the function that decides whether the offspring has a  dominant colour  trait or not
    print()

    #deciding trait 2   
    print(trait_dic[verdict(1)])#running the function that decides whether the offspring has a  dominant length  trait or not
    print()
    
    #I made this so that the program does not keep looping till infinity 
    anything = input()



    


        




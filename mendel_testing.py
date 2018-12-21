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

#list of organisms]
dict_list_of_organis = [ ]

list_of_organis = [ ]



#generation index

gen_index = []




#a  tested but needs more trials combining function
def gen(par1,par2,off_name):
    #off1 = [[z1_1,z2_1],[z1_2,z2_2]] # OFF SPRING inherited traits
    
    off_name = [[par1[0],par2[0]],

                     [par1[1],par2[1]]


            ] 
    print( "Off spring number  :   "+str(i) +"  has the following traits :    " + str(off_name))
    print()
    print(off_name[0])#showing the colour traits remember the X & x refer to colour
    print()
    print(off_name[1])#showing the length traits  remember the Y & y refer to length
    print()
    print()




#a segregation function turning offspring 1 into parent
def seg(off):
    
    ran_off__1 = random.randint(0,1)
    ran_off__2 = random.randint(0,1)

    
    
    z_off__1 = off[0][ran_off__1]
    z_off__2 = off[1][ran_off__2]
    z_off = [z_off__1,z_off__2]
    print()
    print("z_off is " + str(z_off))
    print()
    print()
    print()
    
    
    
    






#a function that decides whether the offspring will be observed to have dominant or recessive trait
def verdict(x,off):
    if dom[x] in off[x]:
        
        return("dom" + str(x))

    else:
        
        print()
        return("rec"+str(x))




#parent selection function
def par_selection():
    #list of 4  available  organisms # TODO : TURN THIS NEXT BLOCK INTO FUNCTION
    global list_of_organis
    global list_of_organis_string
    
    ran_z_1 = random.randint(0,len(list_of_organis)-1)#random number to choose next parent 1
    ran_z_2 = random.randint(0,len(list_of_organis)-2)#random number to choose next parent 2

    
    global chosen_z_1
    chosen_z_1 = list_of_organis[ran_z_1]
    chosen_z_1_string = list_of_organis_string[ran_z_1]
    list_of_organis.remove(chosen_z_1)
    list_of_organis_string.remove(chosen_z_1_string)



    global chosen_z_2
    chosen_z_2 = list_of_organis[ran_z_2]
    chosen_z_2_string = list_of_organis_string[ran_z_2]

    
    print(str(chosen_z_1)+"  ------    " + chosen_z_1_string )
    
    print(str(chosen_z_2)+"  ------    " + chosen_z_2_string )
    




 
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
    #list of organisms
    list_of_organis = []

    #list of organisms strin
    list_of_organis_string=[]



    #offspring  that doesn't exist yet
    off=[]

    #offspring  parent  doesn't exist yet
    z_off=[]


    
    #parent1
    ran1_1 = random.randint(0,1)#random number to choose the first trait for parent 1
    ran1_2 = random.randint(0,1)#random number to choose second  trait  for parent 1
    z1_1 = ALL[0][ran1_1]
    z1_2 = ALL[1][ran1_2]
    z1 = [z1_1,z1_2] #final chosen traits from parent 1
    list_of_organis.append(z1)
    list_of_organis_string.append('z1')
    print("z1 is " + str(z1))

    #parent2
    ran2_1 = random.randint(0,1)#random number to choose the first trait for parent 2
    ran2_2 = random.randint(0,1)#random number to choose the second trait for parent 2
    z2_1 = ALL[0][ran2_1]
    z2_2 = ALL[1][ran2_2]
    z2 = [z2_1,z2_2]#final chosen traits from parent 1
    list_of_organis.append(z2)
    list_of_organis_string.append('z2')
    print("z2 is " + str(z2))


    #parent 3
    ran3_1 = random.randint(0,1)
    ran3_2 = random.randint(0,1)
    z3_1 = ALL[0][ran3_1]
    z3_2 = ALL[1][ran3_2]
    z3 = [z3_1,z3_2]
    print("z3 is  " + str(z3))
    list_of_organis.append(z3)
    list_of_organis_string.append('z3')
    print()

    
    print("generating ...........")
    print()
    
    #offspring(1)
    off1 = [[z1_1,z2_1],[z1_2,z2_2]] # OFF SPRING inherited traits
    print(off1)
    print()
    print(off1[0])#showing the colour traits remember the X & x refer to colour
    print()
    print(off1[1])#showing the length traits  remember the Y & y refer to length
    print()
    print()


    
    #deciding trait 1
    print(trait_dic[verdict(0,off1)])#running the function that decides whether the offspring has a  dominant colour  trait or not
    print()

    #deciding trait 2   
    print(trait_dic[verdict(1,off1)])#running the function that decides whether the offspring has a  dominant length  trait or not
    print()


    #turning offspring 1 into parent
    ran_off_1_1 = random.randint(0,1)
    ran_off_1_2 = random.randint(0,1)
    z_off_1_1 = off1[0][ran_off_1_1]
    z_off_1_2 = off1[1][ran_off_1_2]
    z_off_1 = [z_off_1_1,z_off_1_2]
    list_of_organis.append(z_off_1)
    list_of_organis_string.append('z_off_1')
    print()
    print("z_off_1 is " + str(z_off_1))
    print()
    print()
    print()

    # starting the loop
    print("Type number of generations wanted")

    while True:
        print("Type a letter for every generation")
        gen_num = input()
        if gen_num == '':
            break
        else:
            gen_index.append(gen_num)





    for i in gen_index:
        par_selection()
        gen(chosen_z_1,chosen_z_2,i)
        print()
        print()
        #deciding trait 1
        print(trait_dic[verdict(0,i)])#running the function that decides whether the offspring has a  dominant colour  trait or not
        print()

        #deciding trait 2   
        print(trait_dic[verdict(1,i)])#running the function that decides whether the offspring has a  dominant length  trait or not
        print()        
        print()
        print("transforming offspring  " + str(i) + "into parent")
        
    
    






    #I made this so that the program does not keep looping till infinity 
    anything = input()
    print()
    print()
    print()
    print()
    print("############################################################################################")
    print()
    print()
    print()
    print()
        




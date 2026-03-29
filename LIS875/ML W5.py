# # start_laser() # turn the laser on
# # size = int(input("How big? ")) # get user input
# # move_laser(0, size) # move to top left corner
# # end_laser() # turn the laser off
# # move_laser(0, 0) # move to the bottom left corner
# # move_laser(size, size) # move to top right corner
# # move_laser(0, 0) # move back to bottom left corner
# # from totally.real.package import start_laser, end_laser, move_laser # load laser tools
# # move_laser(size, 0) # move to bottom right corner
# from totally.real.package import start_laser, end_laser, move_laser # load laser tools
# size = int(input("How big? ")) # get user input
# move_laser(0, 0) # move to the bottom left corner
# start_laser() # turn the laser on
# move_laser(0, size) # move to top left corner
# move_laser(size, size) # move to top right corner
# move_laser(size, 0) # move to bottom right corner
# move_laser(0, 0) # move back to bottom left corner
# end_laser() # turn the laser off
# # I think it safe to say there are multiple correct orders, based # upon the specific 
# # move commands given I picked an order that makes the most sense to me, particularly 
# # given the inclusion of "back" in line 18

# # elif data.amountOwed > 0 and data.dueDate <= today: # if time left to pay
# # if data.amountOwed === 0: # if nothing owed
# # else: # else, they are past due
# # data = loadTotallyRealRenterInfo() # get info from our database
# #     print(f"You are past due! Please pay {data.amountOwed} immediately!")
# #     print("Thanks! Nothing Owed!")
# # today = new Date() # look up what today's date is
# #     print(f"You owe: {data.amountOwed}")
# today = new Date() # look up what today's date is
# data = loadTotallyRealRenterInfo() # get info from our database
# if data.amountOwed === 0: # if nothing owed
#     print("Thanks! Nothing Owed!")
# elif data.amountOwed > 0 and data.dueDate <= today: # if time left to pay
#     print(f"You owe: {data.amountOwed}")
# else: # else, they are past due
#     print(f"You are past due! Please pay {data.amountOwed} immediately!")

# #     return result
# # def multiply(a, b):
# #     result = a * b
# def multiply(a, b):
#     result = a * b
#     return result
# # def states the function without that the code is lost and doesn't know what is going 
# # on, then you have to define what result is else it is calling an undefined variable 

# # name = input("What is your name?")
# # place = input("Where are you from?")
# # print(f"Hello, {name}! I've heard that {place} is great!")

# noun = input("Give me one noun - ")
# verb = input("Give me one verb - ")
# adj = input("Give me one adjective - ")
# where = input("Where do you want to go right now? ")
# print(f"A tale of the travels of the {noun}. With their spirit full of {adj} they set off for {where}. It was a long and arduous journey but though {verb} they were able to make it, finally.")

# x = float(input("Give me x:"))
# y = float(input("Give me y:"))
# add = x + y
# sub = x - y
# mult = x * y
# div = x/y
# print(f"x + y = {add}, x - y = {sub}, x * y = {mult}, x/y = {div}")

# l1 = float(input("Your grade out of 5 on lab 1 - "))
# l2 = float(input("Your grade out of 5 on lab 2 - "))
# l3 = float(input("Your grade out of 5 on lab 3 - "))
# gpneed = 90 - l1 - l2 - l3
# print(f"According to your current grade, to receive an A in this class, you need to earn {gpneed} points. You got this!")

# v1 = float(input("What is the cost per carrot of the carrots you got? $"))
# q1 = float(input("how many carrots did you get? "))
# v2 = float(input("What is the cost per onion of the onions you got? $"))
# q2 = float(input("how many onions did you get? "))
# v3 = float(input("What is the cost per broccoli of the broccoli you got? $"))
# q3 = float(input("how many broccoli did you get - "))
# tot = (v1*q1)+(v2*q2)+(v3*q3)
# print(f"Your total today is ${tot}. Have fun with your cooking!")


# x=float(input("What is the length in feet? "))
# y=float(input("What is width in feet? "))
# z=float(input("What is height in feet? "))
# while True:
#     try: 
#         ui=int(input("If you want the area type 1, if you want the border type 2, if you want the volume type 3. "))
#     except ValueError:
#         print("Please type a number")
#         continue
#     if ui > 3:
#         print(" Invalid input. Please try again")
#         continue
#     elif ui == 0:
#         print(f"The length is {x}, width is {y}, height is {z}.")
#         continue
#     else:
#         break
# if ui==1:
#     print(f"The area is {x*y}ft")
# elif ui==2:
#     print(f"The border is {2*x+2*y}ft")
# elif ui==3:
#     print(f"The volume is {x*y*z}ft")


# a,b,c,d=map(int,input("Please type four numbers each seperated by a space - ").split()) 
# average=(a+b+c+d)/4

# if a<average:
#     print(f"The first number ({a}) is less than the average ({average})")
# else:
#     print(f"The first number ({a}) is greater than the average ({average})")
# if b<average:
#     print(f"The second number ({b}) is less than the average ({average})")
# else:
#     print(f"The second number ({b}) is greater than the average ({average})")   
# if c<average:
#     print(f"The third number ({c}) is less than the average ({average})")
# else:
#     print(f"The first number ({c}) is greater than the average ({average})")   
# if d<average:
#     print(f"The fourth number ({d}) is less than the average ({average})")
# else:
#     print(f"The fourth number ({d}) is greater than the average ({average})")
    
# if a>b and a>c and a>d:
#     print(f"The first number ({a}) is the largest")
# elif b>a and b>c and b>d:
#     print(f"The second number ({b}) is the largest")
# elif c>a and c>b and c>d:
#     print(f"The third number ({c}) is the largest")
# else:
#     print(f"The fourth number ({d}) is the largest")  
# if a<b and a<c and a<d:
#     print(f"The first number ({a}) is the smallest")
# elif b<a and b<c and b<d:
#     print(f"The second number ({b}) is the smallest")
# elif c<a and c<b and c<d:
#     print(f"The third number ({c}) is the smallest")
# else:
#     print(f"The fourth number ({d}) is the smallest")
    
# if a<b and b<c and c<d:
#     print(f"The numbers ({a}, {b}, {c}, & {d}) were entered in increasing order")
# elif a>b and b>c and c>d:
#     print(f"The numbers ({a}, {b}, {c}, & {d}) were entered in decreasing order")
# else:
#     print(f"The numbers ({a}, {b}, {c}, & {d}) were not entered in an order")

# ab=a+b
# bc=b+c
# cd=c+d  
# if ab<bc:
#     print(f"the sum of the first two numbers ({ab}) is less than the sum of the middle two numbers ({bc})")
# else:
#     print(f"the sum of the first two numbers ({ab}) is more than the sum of the second two numbers ({bc})")
# if bc<cd and bc>ab:
#     print(f"the sum of the middle two numbers ({bc}) is less than the sum of the last two numbers ({cd}) and therefore the sum of the last two numbers is the largest sum")
# elif bc<cd and bc<ab:
#     print(f"the sum of the middle two numbers ({bc}) is less than the sum of the last two numbers ({cd}) and therefore the sum of the middle two numbers is the smallest sum")
# elif bc>cd and bc>ab:
#    print(f"the sum of the middle two numbers ({bc}) is more than the sum of the last two numbers ({cd}) and therefore the sum of the middle two numbers is the largest sum")
# else:
#     print(f"the sum of the middle two numbers ({bc}) is more than the sum of the last two numbers ({cd}) and therefore the sum of the last two numbers is the smallest sum")

# from re import sub
# consent = False
# uresp = input("Do you consent to cookies? ")
# cleanuresp = sub(r"[^a-z]", "", uresp.lower())

# if cleanuresp in ("yes","yea","yeah","y","yep","i do","ye"): 
#     consent = True
# elif cleanuresp in ("sure","OK","whatever","IDK","i suppose","eh","why not","meh"):
#     consent = True
#     print("Due to an affirmative response you have consented")

# if consent==True:
#     print("Thank you for consenting to cookies, we hope they are delicious.")
# else:
#     print("You have not agreed. We WILL ask again next time you visit this website, because everyone loves cookies.")

# from random import random
# noun = "wood" # wood 70%, steel 10%, PVC 15%, aluminum 5%
# verb = "build" # build 60%, buy 10%, request 10%, find 20%
# adj = "black" # tan 30%, white 30%, black 30%, green 10%
# rollb = random()
# rollm = random()
# rolle = random()

# rolln = random() # a number between 0 (inclusive) and 1 (exclusive)
# if rolln<.05:
#     noun="aluminum"
# elif rolln<.2:
#     noun="PVC"
# elif rolln<.3:
#     noun="steel"

# rollv = random()
# if rollv<.1:
#     verb="buy"
# elif rollv<.2:
#     verb="request"
# elif rollv<.4:
#     verb="find"

# rolla = random()  
# if rolla<.1:
#     adj="green"
# elif rolla<.4:
#     adj="tan"
# elif rolla<.7:
#     adj="white"

# if rollb<(1/3):
#     print(f"Today is your first day on the job. You have been put in charge of all of the {noun} materials.")
#     if rollm<.5:
#         print(f"For some reason they trusted you to {verb} these materials. You have {round(10*random())} weeks to collect all of the required quantity")
#         if rolle<.5:
#             print(f"To make matters even more complicated the materials all have to be {adj}.")
#         else:
#             print(f"Though thankfully they are all {adj} which you have dealt with before.")
#     else:
#         print(f"You are a recent graduate and this is your first big task and you are very nervous. You have to {verb} {round(10*random())} dozen pieces")
#         if rolle<.5:
#             print(f"While all of them are {adj}, your mentor has thankfully worked with this version a lot before.")
#         else:
#             print(f"Unfortunately only half of them are {adj} which complicates matters.")
# elif rollb<(2/3):
#     print(f"Bob is the {noun} specialist. His job is to work with all of the {noun} materials.")
#     if rollm<.5:
#         print(f"Sometimes his job requires him to go about things in different manners. This week he has to {verb} the materials")
#         if rolle<.5:
#             print(f"He really hates having to deal with {adj} ones")
#         else:
#             print(f"Specifically he is tasked with {adj} ones.")
#     else:
#         print(f"Every single week he has to deal with different people wanting to {verb} the materials.")
#         if rolle<.5:
#             print(f"It is really complicated when they want {adj} ones.")
#         else:
#             print(f"This week everyone seems to want {adj} ones.")
# else:
#     print(f"Jim hates working with {noun}. It is what killed his father, but unfortunately it is his job.")
#     if rollm<.5:
#         print(f"What he hates the most is having to {verb} {round(10*random())} dozen every week. But it was his fathers' job and he has to continue his legacy.")
#         if rolle<.5:
#             print(f"Even when people want {adj} materials, the exact type that got his father killed.")
#         else:
#             print(f"Sometimes though, people want {adj} materials. Those weeks are better.")
#     else:
#         print(f"Though he hates his job, he does get the chance to travel when he goes to {verb} the materials, which he does enjoy.")
#         if rolle<.5:
#             print(f"He ggets to travel especially far when looking for {adj} materials.")
#         else:
#             print(f"When he has to find {adj} materials he is glum though cause they remind him of his father.")

# from random import randint
# a = randint(0,100)
# b = randint(0,100)
# c = randint(0,100)
# lie = randint(1,5)
# fa = randint(0,100)
# fb = randint(0,100)
# fc = randint(0,100)
# f=randint(1,3)

# print(f"axex = {a}, basilisk = {b}, & centaur = {c}, the lie is #{lie}, the fakes are - fake axex = {fa}, fake basilisk = {fb}, & fake centaur = {fc}.")

# print("You must guess how many legs each an Axex, a Basilisk, & a Centaur have. To determine this you may request to know how many legs some combination of the three have. You have five inquiries. However, I will lie exactly one time.")

# ha,hb,hc=map(int,input("Please type how many of each creature in the first combo with each number seperated by a space - ").split())
# if lie != 1:
#     print(f"There are {ha*a+hb*b+hc*c} legs in this combination.")
# else:
#     if f==1:
#         print(f"There are {ha*fa+hb*b+hc*c} legs in this combination.")
#     elif f==2:
#         print(f"There are {ha*a+hb*fb+hc*c} legs in this combination.")
#     else:
#         print(f"There are {ha*a+hb*b+hc*fc} legs in this combination.") 
      
# ha,hb,hc=map(int,input("Please type how many of each creature in the second combo with each number seperated by a space - ").split())  
# if lie != 2:
#     print(f"There are {ha*a+hb*b+hc*c} legs in this combination.")
# else:
#     if f==1:
#         print(f"There are {ha*fa+hb*b+hc*c} legs in this combination.")
#     elif f==2:
#         print(f"There are {ha*a+hb*fb+hc*c} legs in this combination.")
#     else:
#         print(f"There are {ha*a+hb*b+hc*fc} legs in this combination.")

# ha,hb,hc=map(int,input("Please type how many of each creature in the third combo with each number seperated by a space - ").split())       
# if lie != 3:
#     print(f"There are {ha*a+hb*b+hc*c} legs in this combination.")
# else:
#     if f==1:
#         print(f"There are {ha*fa+hb*b+hc*c} legs in this combination.")
#     elif f==2:
#         print(f"There are {ha*a+hb*fb+hc*c} legs in this combination.")
#     else:
#         print(f"There are {ha*a+hb*b+hc*fc} legs in this combination.")

# ha,hb,hc=map(int,input("Please type how many of each creature in the fourth combo with each number seperated by a space - ").split())        
# if lie != 5:
#     print(f"There are {ha*a+hb*b+hc*c} legs in this combination.")
# else:
#     if f==1:
#         print(f"There are {ha*fa+hb*b+hc*c} legs in this combination.")
#     elif f==2:
#         print(f"There are {ha*a+hb*fb+hc*c} legs in this combination.")
#     else:
#         print(f"There are {ha*a+hb*b+hc*fc} legs in this combination.")

# ha,hb,hc=map(int,input("Please type how many of each creature in the fifth and last combo with each number seperated by a space - ").split())        
# if lie != 5:
#     print(f"There are {ha*a+hb*b+hc*c} legs in this combination.")
# else:
#     if f==1:
#         print(f"There are {ha*fa+hb*b+hc*c} legs in this combination.")
#     elif f==2:
#         print(f"There are {ha*a+hb*fb+hc*c} legs in this combination.")
#     else:
#         print(f"There are {ha*a+hb*b+hc*fc} legs in this combination.")


# ga,gb,gc=map(int,input("Please type how many legs you think each creature has with each number seperated by a space - ").split())

# if ga==a and gb==b and gc==c:
#     print("Congratulations you have survived - I suppose.")
# else:
#     print("Yay me!, I get to eat you!")


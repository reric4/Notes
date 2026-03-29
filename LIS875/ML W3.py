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






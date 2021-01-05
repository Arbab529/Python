menuitem = ["[1] Menu choosing","[2] Topping addition in order","[3] Reordering","[4] Discounted deals","[5] Invoice printing"]
print("Hello, I am Food Ordering Bot")
print("-----------------------------------------------")
def order():
    listitems = ["[1] Burger Rs 500","[2] Pizza RS 1000","[3] Roll RS 100","[4] Cold Drink RS 80","[5] Fries RS 50"]
    for items in listitems:
        print(items)
        print("---------------------------------")
    x=" "
    selectitem =int(input("Select Your Item : "))
    if(selectitem==1):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
    elif(selectitem==2):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
    elif(selectitem==3):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
    elif(selectitem==4):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
    elif(selectitem==5):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
def reorder():
    order()
def topping():
    listitems = ["[1] Chicken Tikka","[2] Chicken Fajita","[3] Roll Mayo","[4] Chicken Afghani","[5] chinese Fries"]
    for items in listitems:
        print(items)
        print("---------------------------------")
    x=" "
    selectitem =int(input("Select Your Item : "))
    if(selectitem==1):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
    elif(selectitem==2):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
    elif(selectitem==3):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
    elif(selectitem==4):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
    elif(selectitem==5):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
def discountdeals():
    listitems = ["[1] 2 Pizza + Fries","[2] 1 large Pizza + Cold Drink","[3] Roll Mayo + Cold Drink","[4] Roll + 1 Pizza Large"]
    for items in listitems:
        print(items)
        print("---------------------------------")
    x=" "
    selectitem =int(input("Select Your Item : "))
    if(selectitem==1):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
    elif(selectitem==2):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
    elif(selectitem==3):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
    elif(selectitem==4):
        select=selectitem
        store=listitems[select]
        print(store)
        print("---------------------------------")
def script():
    print("Item name:"+item.x)
    print("Item Extra Topping: Chicken Fajita" +topping.x)
    print("Total Price: 1000PKR" price.x)
    print("Thanks For Ordering You Can pay cahon Deilvery")

if __name__ == "__main__":
    print("Here is the menu let's select your option")
    print("")
    print("---------------------------------")
    for items in menuitem:
        print(items)
        print("---------------------------------")
    while True:
        menuitemslct =int(input("Select Any one Option : "))
        if(menuitemslct==1):
            order()
        elif(menuitemslct==2):
            topping()
        elif(menuitemslct==3):
            reorder()
        elif(menuitemslct==4):
            discountdeals()
        elif(menuitemslct==5):
            script()
    
# response = ["Hi, Welcome!",
#             "Please Introduce Yourself and tell me for what job are you applying for?", 
#             "I hope you enjoy this conversation. \nGood bye take care.", 
#             "what is web development?",
#             "what is software development?",
#             "what are your weeknesses?",
#             "Why I hire you for this post?"]

# print("Hi I am your Mentor for practicing Inteview Question.")

# while True:
#     quest2 = input("YOU : ")

#     if ("hi" in quest2 or "hello" in quest2):
#         print("BOT : " + response[0] + " \n" +response[1])

#     elif ("bye" in quest2 or "exit" in quest2):
#         print("BOT : "+response[2])
#         break

#     elif ("web develop" in quest2):
#         print("BOT : "+response[3])  

#     elif ("software" in quest2):
#         print("BOT : "+response[4]) 

#     elif ("development" in quest2):
#         print("BOT : "+response[5])

#     elif ("perfect" in quest2 or "motivated" in quest2 or "hardworking" in quest2 or "work hard" in quest2):
#         print("BOT : "+response[6])
    
#     else:
#         print("Great, So what else you know about the post.")

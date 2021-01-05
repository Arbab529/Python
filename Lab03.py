# Task 01
# Write a program to create a basic chatbot application.

'''
response = ["Hi, How may I help you?", "I hope you enjoy this conversation. \nGood bye take care.",
            "RAM is Random-access memory is a form of computer memory that can be read and changed in any order, typically used to store working data and machine code.", 
            "Sorry, I didn't get you!", 
            "Computer is an Electronic machine that accept data as input and provide output by processing that data.",
            "You can google it to find more."]

print("Hi I am a Computer Specialist Ask me anything.")
while True:
    quest1 = input("YOU : ")

    if ("hi" in quest1 or "hello" in quest1):
        print("BOT : " + response[0])

    elif ("bye" in quest1 or "exit" in quest1):
        print("BOT : "+response[1])
        break

    elif ("what" in quest1 and "ram" in quest1 or "RAM" in quest1):
        print("BOT : "+response[2])

    elif ("what" in quest1 and "COMPUTER" in quest1 or "computer" in quest1):
        print("BOT : "+response[4])

    elif ("why" in quest1 or "keyborad" in quest1 or "ROM" in quest1 or "hardisk" in quest1):
        print("BOT : "+response[5])

    else:
        print("Sorry, I didn't get you!")
'''

# Task 02
# Make a questionnaire about yourself and get response from AI based chatbots before and after providing your information. Note: You can take assistance from chatbot examples on the internet.

# conversations = ["Hi","How can I help you","Select your sheet on https://www.codeindark.com","$300+ tax","Have A nice day","Good Bye"]
# i=0
# while True:
#     userinput = input("You: ")
#     if("hi" in userinput or "hello" in userinput or "salam" in userinput):
#         print(conversations[0]+" "+conversations[1])
#         i+=1
#     elif ("sheet" in userinput):
#         print(conversations[2])
#     elif ("price" in userinput or "amount" in userinput or "cost" in userinput):
#         i+=1
#         print(conversations[3])
#     elif ("thanks" in userinput or "ok" in userinput ):
#         print(conversations[4] +" "+conversations[5])
#         i+=1
#     else:
#         print("invalid response")




import queue as Q

def search(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return
    
    queue = Q.PriorityQueue()
    queue.put((0, [start]))
    
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        
        if end in node[1]:
            print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            break
        
        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))
        
def readGraph():
    lines = int( input("Give input for searching = ") )
    graph = {}
    
    for line in range(lines):
        line = input()


        tokens = line.split()
        node = tokens[0]
        graph[node] = { }
        
        for i in range(1, len(tokens) - 1, 2):
            # print(node, tokens[i], tokens[i + 1])
            # graph.addEdge(node, tokens[i], int(tokens[i + 1]))
            graph[node][tokens[i]] = int(tokens[i + 1])
    return graph

def main():
    graph = readGraph()
    search(graph, 'Multan', 'Kashmir')

main()
input()

# Multan Balochistan 5 
# Balochistan Sindh 9 Punjab 14 skardu 12 KPK 19 Islamabad 21
# skardu Balochistan 12 KPK 7
# Sindh Punjab 3 Balochistan 9 
# Punjab Islamabad 2 Sindh 3 Balochistan 14
# Islamabad Punjab 2 Gilgit 2 Kashmir 4 KPK 1 Balochistan 21
# KPK Islamabad 1 Gilgit 2 Balochistan 19 skardu 7
# Gilgit quetta 2 Islamabad 2 KPK 3 
# Kashmir quetta 2 Islamabad 4 
# quetta Kashmir 2 Gilgit 2 

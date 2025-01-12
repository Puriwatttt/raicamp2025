# txt = "rai"
# print (txt)


# fruits = ["apple", "banana"]
# fruits.append("orange")
# fruits.remove("apple")
# fruits.insert(1, "melon")
# for fruit in fruits:
#     print(f"This is a {fruit}.")

# i = 0
# while i < 3:
#     print(i)
#     i = i + 1

######### Dictionary in Moble Robot
#      A
#    /  \
#   B    C
#  / \    \
# D   E    F 


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start = 'A'
goal = 'E'
frontier = [start]
explored = set() # Use a set for unique(ignore duplicate append)

print(frontier, explored)

while (len(frontier)) > 0:
    current = frontier.pop() #Remove and put into varaible
    print(current)

    if current == goal:
        print("Goal reach")
        break
    print(f"neighbor of {current} is {graph[current]}") #เอาไว้เก็บทางแยกนะจ๊ะะ
    for neighbor in graph[current]:
        frontier.append(neighbor)

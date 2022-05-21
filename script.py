line_break = ''

# Hello User 

def hello():
    name = input('Please enter your name: ')
    print(f"Hello {name}, I hope you're doing well!")
    
hello()
print(line_break)

# Pack

def pack(a,b,c):
    return[a,b,c]

print("For my trip, I'm bringing a: ")
print(pack('sweater','sneakers','toothbrush'))
print(line_break)

# Eat Lunch
    
def eat_lunch(my_food):
    if len(my_food) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(my_food)):
            if i == 0:
                print(f"First, I eat {my_food[0]}")
            else:
                print(f"Next, I eat {my_food[i]}")
eat_lunch([])    
eat_lunch(['pizza', 'strawberries'])

User = input("Array that you want to display (single_D_array, two_D_array):")

list = ["Ke","Jang","Kevin"]
lists =  [ 
     ["Kevin","Jang","Jay"],
     [1,2,3,4,5]
]

def listname():
    for i in list:
        print(list)

def listname():
    for rock in lists:
        for rocks in rock:
            print(lists)

def choice():
    if User == "single_D_array":
        print(list)
    elif User == "two_D_array":
        print(lists)
    else:
        print("error")
        
result = choice()
print(result) 




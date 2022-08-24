def hello():
    return print("Greetings!")

def pack(par_1,par_2,par_3):
    return print([par_2,par_2,par_3])


def eat_lunch(lunch_list:list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty")
        return
    for i in range(len(lunch_list)):
        if i == 0:
            print("First I eat " + lunch_list[i])
        else:
            print(f"Next I eat {lunch_list[i]}")
    

    # Easiest way to loop through
    # for x in lunch_list:
    #     print(x)

l = ["Apple","Pizza","Soup","Pie"]

eat_lunch(l)

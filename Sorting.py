input_list = [-15, -26, 15, 1, 23, -64, 23, 76]
out_list = []

while input_list:
    min = input_list[0]  
    for x in input_list: 
        if x < min:
            min = x
    out_list.append(min)
    input_list.remove(min)    

print(out_list)
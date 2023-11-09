def linear_search(lst, item):
    steps = 0
    index_list = []
    for i in lst:
        steps += 1
        if i == item:
            index_list.append(steps-1)
    return (False, f"Steps: {steps}") if index_list == [] else (True, index_list, f"Steps: {steps}")

user_input = int(input('Enter how many values you want in the list: '))
data_type = input('Enter the data type you want in the list: ')
data_dic = {'int': int, 'float': float, 'str': str, 'bool': bool, 'list': list, 'tuple': tuple, 'set': set, 'dict': dict}
lst = []
try:
    for i in range(user_input):
        if data_type in data_dic:
            lst.append(data_dic[data_type](input('Enter the value: ')))
        else:
            raise TypeError
    search_item = input('Enter the item you want to search for: ')
    print(linear_search(lst, search_item))
except TypeError:
    print("Invalid data type")
except:
    print("Invalid Input")
    

        
    
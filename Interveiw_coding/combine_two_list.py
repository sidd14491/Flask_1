first_list = [1, 2, 2, 5]
second_list = [2, 5, 7, 9]
resulting_list = list(first_list)
resulting_list.extend(x for x in second_list if x not in resulting_list)
print resulting_list



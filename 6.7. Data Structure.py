# 配列：データを一列に並べた変数
for i in range(len(cols_x)-1):
    distance = math.sqrt((cols_x[i+1] - cols_x[i]) ** 2 + (cols_y[i+1]-cols_y[i]) ** 2)

# data type
値の型整数型(int), 浮動小数点型(float), 文字列型(str)

# データ構造
リスト、文字列、タプル、集合、辞書

"""list"""
city = ["Tokyo", "Kyoto", "Saporo", "Naha", "Sendai", "Hakata", "Nagoya"]
# show third one
print(city[2])
# change sixth one to "matuyama"
city[5] = "matuyama"
# add another list, should plus "[]"
city = city + ["hiroshima", "kanazawa"]
# repeat this list
city = city * 2
# retrieve a part of list
print(city[2:5])
# add an element to the end of list
print(city.append("Shibuya"))
# delete the last element of list
print(city.pop())
# delete a element of list by "index" and "same thing"
del city[1]
city.remove("Tokyo")
# Align this list
align = sorted(city)
print(align)


"""Tuple: a list cannot change element."Immutable": same as list"""
# create tuple use "()" rather than "[]"
grade_tuple = (10,20,30)
# convert tuple to list.
grade_list = list(grade_tuple)


"""Set: a list have no same value"""
# create a set use "{}"
rank = {"A", "B"}
# also can convert from list


"""Dictionary: a list designate by "key" rather than "Index""""
# create a dictionary
joho_score = {"E0123":60, "T2468":90, "M8901":45}
print(joho_score["E0123"])


"""homework"""
# create a dictionary
flight = {"JL813":"TAIBEI", "CX567":"HONGKONG", "KE722":"SEOUL",
          "MU730":"SHANGHAI", "NH873":"HONGKONG", "MM23":"TAIBEI",
          "SQ619":"SINGAPORE", "BR131":"TAIBEI"}

print(flight["CX567"])

#convert dictionary to list
flight_list = list(flight.values())
#convert list to set
flight_set = set(flight_list)
print(flight_set)


"""String"""
# Can do same operations as list
# also can use for loop

#create a string
message = "hello!"

# replease
print(message.replace("hello", "Hi"))
# convert string to list by "split"
message_list = message.split("!")
print(message_list)
# count the numbers
print(message.count("hello!"))
# if contains hello or not
print("hello" in message)


"""list comprehension: [...for ... in ... if...], can create list efficiently."""
# example: create a list
num_square = []
for num in [1,2,3,4,5]:
    num_square.append(num ** 2)
print(num_square)

num_square = [num ** 2 for num in [1,2,3,4,5]]
print(num_square)

# create string use [], set use {}, dictionary use {}
#create dictionary from two list by function zip
day_num = [1, 2, 3, 4, 5, 6, 7]
day_en = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

days = {num:en for (num,en) in zip(day_num,day_en)}
print(days)




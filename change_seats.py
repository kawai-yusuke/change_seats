import random

with open("members_list.txt", mode="r") as f:
    members = f.read()

    all_list = members.split("\n")

list1 = []
list2 = []
list3 = []

while True:
    random_member = random.choice(all_list)
    list1.append(random_member)
    all_list.remove(random_member)
    if len(list1) == 6:
        break

while True:
    random_member = random.choice(all_list)
    list2.append(random_member)
    all_list.remove(random_member)
    if len(list2) == 5:
        break

print(f"Table1: {list1[0]} {list1[1]} {list1[2]} {list1[3]} {list1[4]} {list1[5]}")
print(f"Table2: {list2[0]} {list2[1]} {list2[2]} {list2[3]} {list2[4]}")
print(f"Table3: {all_list[0]} {all_list[1]} {all_list[2]} {all_list[3]}")

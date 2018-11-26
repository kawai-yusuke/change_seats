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

while True:
    random_member = random.choice(all_list)
    list3.append(random_member)
    all_list.remove(random_member)
    if len(list3) == 4:
        break

# for user in list1:
#     print(user,end = "  ")

print(f"{list1[0]} {list1[1]} {list1[2]} {list1[3]} {list1[4]} {list1[5]}")
print(f"{list2[0]} {list2[1]} {list2[2]} {list2[3]} {list2[4]}")
print(f"{list3[0]} {list3[1]} {list3[2]} {list3[3]}")







# $ python seat_shuffle.py
# Table1: 横川 中川 鹿糠 美香子 大江 内田
# Table2: 吉田 則也 中俣 川合 三村
# Table3: 高橋 工藤 松本 杉村
#
# $ python seat_shuffle.py
# Table1: 工藤 三村 中俣 高橋 則也 川合
# Table2: 中川 美香子 大江 内田 横川
# Table3: 鹿糠 吉田 杉村 松本
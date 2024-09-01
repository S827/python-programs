years_experience = {
    'Luke': 3,
    'Kelly': 6,
    'Ken': 4,
    'Alex': 3,
    'Mary': 7
}

years = 0
index = 0

years_list = list[years_experience.items()]
print(years_list)
# while years < 5:
#     key, years = years_list[index]
#     print(key, value)
#     index += 1
years = 5
new_l = []
for k, v in years_experience.items():
    if years_experience[k] < 5:
        new_l.append([{k: v}])
print(new_l)

new_li = [k:v for k, v in years_list.items()]

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'JoJo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        # return len(self.color)
        return 5

    # def __del__(self):
    #     print('deleted')

    def __call__(self):
        return 'Yes?'

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
# OP: <__main__.Toy object at 0x000001DEE80A3D90>
print(action_figure.__str__())
print(str(action_figure))  # now it prints red

print(action_figure.__len__())
print(len(action_figure))
# del action_figure

print(action_figure())
print(action_figure['name'])

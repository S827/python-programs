class SuperList(list):  # if SuperList don't inherit from list, append wont work, and isubclass will return False
    # def __init__(self, lst):
    #     self.lst = lst

    def __len__(self):
        return 100

    # def __append__(self, item):
    #     self.item = item
    #     return (self.lst).append(self.item)


super_list1 = SuperList()

print(len(super_list1))

super_list1.append(5)
print(super_list1)
print(issubclass(SuperList, list))

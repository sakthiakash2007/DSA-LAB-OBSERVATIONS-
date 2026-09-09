class ListADT:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def delete(self, item):
        if item in self.items:
            self.items.remove(item)

    def search(self, item):
        return item in self.items

    def display(self):
        print("List:", self.items)


lst = ListADT()

lst.insert(10)
lst.insert(20)
lst.insert(30)

lst.display()

print("Search 20:", lst.search(20))

lst.delete(20)
lst.display()

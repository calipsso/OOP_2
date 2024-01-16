class Stadium:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __len__(self):
        return self.capacity

    def __add__(self, other):
        return Stadium(self.name + " " + other.name, self.capacity + other.capacity)

    def __eq__(self, other):
        return self.name == other.name and self.capacity == other.capacity


stadium1 = Stadium("Etihad Stadium", 11222)
stadium2 = Stadium("Etihad Stadium", 11222)

print(stadium1)
print(stadium2)
if stadium1 == stadium2:
    print("rovnaky")
else:
    print("rozny")
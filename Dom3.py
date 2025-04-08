class ClothesIteratorito:
    def __init__(self, clothes):
        self.clothes = clothes
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.clothes):
            item = self.clothes[self.index]
            self.index += 1
            if item.startswith("р"):
                return item
        raise StopIteration

clothes = ["рокля", "панталон", "риза", "яке", "пуловер", "ракия", "рокер", "чорапи", "шапка"]
clothes_iterator = ClothesIteratorito(clothes)
print("Дрехи започващи съ 'р':")
for item in clothes_iterator:
    print(item)

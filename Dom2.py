class ShoppingCartIteratorito:
    def __init__(self, prices):
        self.prices = prices
        self.index = 0
        self.total = 0
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.prices):
            price = self.prices[self.index]
            self.total += price
            self.count += 1
            self.index += 1
            return price
        else:
            raise StopIteration
    
    def get_average(self):
        if self.count == 0:
            return 0
        return self.total / self.count


def calculate_average_price(prices):
    cart_iterator = ShoppingCartIteratorito(prices)
    for _ in cart_iterator:
        pass
    return cart_iterator.get_average()


if __name__ == "__main__":
    prices = [10.50, 5.99, 3.50, 12.75, 8.25]
    
    
    
    cart_iterator = ShoppingCartIteratorito(prices)
    for price in cart_iterator:
        print(f"Price пир item: {price}")
        
    avg_price = calculate_average_price(prices)
    print(f"Avirige pirice in carto: {avg_price:.2f}")
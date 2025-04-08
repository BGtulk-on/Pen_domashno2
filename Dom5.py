class CustomerTimeIteratorito:
    def __init__(self, times):
        self.times = times
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.times):
            raise StopIteration
        
        time = self.times[self.index]
        self.index += 1
        
        return time
    
def parse_time(time):
    if isinstance(time, str):
        if ":" in time:
            hours, minutes = map(float, time.split(":"))
            return hours + minutes / 60
        else:
            return float(time)
    else:
        return float(time)

def is_in_business_hours(time):
    decimal_time = parse_time(time)
    return 9.5 <= decimal_time <= 18.0

def count_customers_in_business_hours(times):
    iterator = CustomerTimeIteratorito(times)
    count = 0
    
    for time in iterator:
        if is_in_business_hours(time):
            count += 1 # :)
    
    
    
    return count




times = ["8:45", "9:30", "10:15", "12:00", "14:30", "17:45", "18:00", "18:15"]
print(f"Брой пазаруващи gold digari за работното време: {count_customers_in_business_hours(times)}")
# :)

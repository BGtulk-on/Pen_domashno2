def count_weekly_steps(steps):
    steps_iterator = iter(steps)
    
    total_steps = 0
    
    try:
        while True:
            daily_steps = next(steps_iterator)
            total_steps += daily_steps
    except StopIteration:
        pass
    
    return total_steps

if __name__ == "__main__":
    weekly_steps = [8000, 10000, 7500, 9200, 11000, 5600, 12500]
    
    total = count_weekly_steps(weekly_steps)
    print(f"Totale: {total}")
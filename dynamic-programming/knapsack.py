items = [(3, 90), (7, 160), (2, 15)]
capacity = 20

def brute_force(items, capacity):   
    def top_down(capacity, n=len(items)):
        if capacity == 0 or n == 0: return 0
        weight, value = items[n-1]
        if weight > capacity:  return top_down(capacity, n-1)
        option1 = value + top_down(capacity - weight, n)
        option2 = top_down(capacity, n-1)
        return max(option1, option2)
    return top_down(capacity)

def dynamic_programming(items, capacity):
    value_at_capacity = [0] * (capacity + 1)

    for capacity, value in enumerate(value_at_capacity):
        max_value = value
        for weight, value in items:
            if weight > capacity: continue
            max_value = max(max_value, value + value_at_capacity[capacity-weight])
        value_at_capacity[capacity] = max_value
    
    return value_at_capacity[-1]
    

print(brute_force(items, capacity))

print(dynamic_programming(items, capacity))
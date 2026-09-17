print("Hello, I am Sarthak Bector, and my student ID is R02225237")

def mean_and_max(numbers):
    mean_value = sum(numbers) / len(numbers)
    max_value = max(numbers)
    return mean_value, max_value

data = [10, 20, 30, 40, 50]

mean_result, max_result = mean_and_max(data)

print("Mean:", mean_result)
print("Maximum:", max_result)

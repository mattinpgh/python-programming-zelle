# Write definitions for sum_n (sum of the first n natural numbers) and num_n_cubes (sum of the cubes of the first N natural numbers)

def sum_n(n=0, count =0):
    if n <= 0:
        return count
    count += n
    return sum_n(n - 1, count)

def sum_n_cubes(n=0, count=0):
    if n <= 0:
        return count
    count += (n ** 3)
    return sum_n_cubes(n - 1, count)

x = int(input("Provide an integer for calculating sums and cubes: "))
print(f"The sum of the first {x} natural numbers is {sum_n(x)}.")
print(f"The sum of the cubes of the first {x} natural numbers is {sum_n_cubes(x)}")

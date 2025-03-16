# Write a function to compute the nth Fibonacci number. Use that to solve ch 3, ex 16

def looping_fibonacci(n):
    for x in range(0, n-1):
        first_position = x if x < 1 else second_position
        second_position = 1 if x < 1 else added
        added = first_position + second_position
        print(f"First is {first_position}, second is {second_position}, and added is {added}")
    return added


print(looping_fibonacci(6))
#print(acc_fibonacci(10))

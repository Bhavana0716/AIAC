

import time
start_time = time.time() #start time measurement
nums = [i for i in range(1, 1000000)] #list of numbers from 1 to 1000000
squares = [n ** 2 for n in nums] #using list comprehension to square each number
print(len(squares))
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

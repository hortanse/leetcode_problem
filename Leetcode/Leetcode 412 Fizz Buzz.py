#Leetcode 412 Fizz Buzz

#Given an integer n, return a string array answer (1-indexed) where:

#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.

#Example 1:

#Input: n = 3
#Output: ["1","2","Fizz"]
#In a naive approach, we can iterate through the numbers from 1 to n and check if the number is divisible by 3 or 5 or both. If it is divisible by 3, we add "Fizz" to the answer list. If it is divisible by 5, we add "Buzz" to the answer list. If it is divisible by both 3 and 5, we add "FizzBuzz" to the answer list. If it is not divisible by either 3 or 5, we add the number itself to the answer list.
def fizzBuzz(n):
    answer = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer

print(fizzBuzz(30))
##Time Complexity: O(n)
##Space Complexity: O(1)
#Let's try to optimize the space complexity by using a dictionary to store the mappings of numbers to their corresponding strings.
def fizzBuzz(n):
    #define the dictionary
    mapping = {3: "Fizz", 5: "Buzzz"}
    answer = []

    for i in range(1, n + 1):
        temp = ""

         #check each divisor
        for divisor in mapping:
            if i % divisor == 0:
                 temp += mapping[divisor]
        if not temp:
            temp = str(i)
        answer.append(temp)
    return answer   
myMap = { (1,2): 3}
print(myMap[(1,2)])
mySet = set()
mySet.add((1,2))
print(mySet)
print((1,2) in mySet)

#Heap
import heapq
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

print(minHeap[0]) #min is always at index 0

while len(minHeap):
    print(heapq.heappop(minHeap))
#no max heap in python, use min heap and negate values
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))
#build heap from list
myList = [2,1,8,4,5]
heapq.heapify(myList)
print(myList)

while len(myList):
    print(heapq.heappop(myList))
#build a funcitons
def myFunc(n, m):
    return n * m

print(myFunc(3, 4))

#nested functions
def outerFunc(a, b):
    def innerFunc(c, d):
        return c + d
    return innerFunc(a, b)

print(outerFunc(3, 4))

#nonlocal keyword
def double(arr, val):
    def helper():
        for i, n in enumerate(arr):
            arr[i] *= 2
            # this will modify val outside helper scope
            nonlocal val
            val *= 2
    helper()
    print(arr, val)
nums = [1, 2]
val = 3
double(nums, val)
 
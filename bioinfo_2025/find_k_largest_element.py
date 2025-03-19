#Find the k largest elements in an unsorted list
#Using Min Heap

import heapq

def find_k_largest(nums, k):
    min_heap = [] #min heap of size of k

    for num in nums:
        heapq.heappush(min_heap, num) #push elements into heap
        if len(min_heap) > k:
            heapq.heappop(min_heap) #remove the smallest element to maintain size k
    return(min_heap) # min heap now contains the k largest elements

def find_k_smallest(nums, k):
    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num) #push elements by using negative 
        if len(max_heap) > k:
            heapq.heappop(max_heap) #remove the largest element
    return [-x for x in max_heap] #convert back to positive numbers
#or easliest way to use build-in function
def find_k_smallest2(nums, k):
    return heapq.nsmallest(k, nums)
#Test the function
nums = [3, 10, 5, 20, 7, 15]
k = 3
print(find_k_largest(nums, k))
print(find_k_smallest(nums, k))
    
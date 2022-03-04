def kthLargest(nums, k):
      nums.sort()
      if k ==1:
         return nums[-1]
      temp = 1
      return nums[len(nums)-k]
arr=[int(item) for item in input().split(" ")]
k=int(input())
print(kthLargest(arr, k))
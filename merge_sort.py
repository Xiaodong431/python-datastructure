def merge_sort(nums):
	half = len(nums) // 2
	if half < 1: return nums
	left, right = merge_sort(nums[:half]), merge_sort(nums[half:])
	for i in range(len(nums)-1,-1,-1):
		if not right or (left and left[-1] > right[-1]):
			nums[i] = left.pop()
		else:
			nums[i] = right.pop()
	return nums

print (merge_sort([10,2,4,24,4,-12,-34,-94,3493,190,98]))
print (merge_sort([9,8,7,6,5,4,3,2,1]))
print (merge_sort([1,2,3,4,5,6,7,8,9,10,11,12]))

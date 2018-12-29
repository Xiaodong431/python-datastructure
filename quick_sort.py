def quick_sort(nums):
	return qsort(nums,0,len(nums)-1)

def qsort(nums, begin, end):
	if begin >= end:
		return
	i = begin
	j = end
	pivot = nums[i + (j-i) // 2]
	while i <= j:
		while i <= j and nums[i] < pivot:
			i += 1
		while i <= j and nums[j] > pivot:
			j -= 1
		if i <= j:
			if i < j:
				nums[i], nums[j] = nums[j], nums[i]
			i += 1
			j -= 1

	qsort(nums, begin, j)
	qsort(nums, i, end)
	return nums

"""
print (quick_sort([1,2,3,12,2,341,2,2,23,-1,1]))
print (quick_sort([2,2,2,2,2,1,1,1,1]))
print (quick_sort([2,2,2,2,2,2,2,2]))
"""

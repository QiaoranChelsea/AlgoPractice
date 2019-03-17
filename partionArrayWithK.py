## 写一个函数把一个数组按第k个index的数进行排列，变成小于arr[k],等于arr[k],大于arr[k]的三部分。




def partitionArrayWithK(nums, k):
	if not nums:
		return []

	pivot = nums[k]
	l = 0
	r = len(nums)-1
	while l<= r :
		while l<=r and nums[l] < pivot:
			l += 1 
		while l<=r and nums[r] >= pivot:
			r -= 1 
		if l <= r :
			nums[l], nums[r] = nums[r], nums[l]
			l += 1 
			r -=1 

	r = len(nums) - 1 
	while l<= r :
		while l<=r and nums[l] == pivot:
			l += 1 
		while l<=r and nums[r] != pivot:
			r -= 1 
		if l <= r :
			nums[l], nums[r] = nums[r], nums[l]
			l += 1 
			r -=1 

	print(nums)
	return nums

nums1 = [6,7,8,1,3, 0,2,0,1,2,0,1,2,3,4,5,6]
partitionArrayWithK(nums1, 4)


def selection_sort(nums):
	n=len(nums)
	for i in range(0,n):
		min=i
		for j in range(i+1,n):
			if nums[j]<nums[min]:
				temp=nums[i]
				nums[i]=nums[j]
				nums[j]=temp
	return nums

def get_data():
	nums=[]
	while True:
		a=int(raw_input("Enter a number (-1 if done) : "))
		if a==-1:
			break
		nums.append(a)
	return nums
if __name__=='__main__':
	nums=get_data()
	print "Input data is : ",nums
	nums=selection_sort(nums)
	print "\nsorted data is : ",nums

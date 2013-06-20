def insertion_sort(nums):
	n=len(nums)
	for i in range(0,n):
		for j in range(i,0,-1):
			if nums[j]<nums[j-1]:
				temp=nums[j]
				nums[j]=nums[j-1]
				nums[j-1]=temp
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
	ms=insertion_sort(nums)
	print "\nsorted data is : ",nums

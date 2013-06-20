def bubble_sort(nums):
	n=len(nums)
	for i in range(0,n):
			for j in range(0,n-1-i):
				if nums[j]>nums[j+1]:
					temp=nums[j]
					nums[j]=nums[j+1]
					nums[j+1]=temp	
	return nums

def get_data():
	nums=[]
	while True:
		a=int(raw_input("Enter a number (-1 to exit) : "))
		if a==-1:
			break
		nums.append(a)
	return nums

if __name__=='__main__':
	nums=get_data()
	print "Input data is : ",nums
	nums=bubble_sort(nums)
	print "\nsorted data is : ",nums

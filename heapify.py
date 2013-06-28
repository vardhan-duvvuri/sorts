def make_heap(nums):
    n=len(nums)
    for i in range((n-2)/2,-1,-1):
        max_heap(nums,i,n-1)
    print "The heapified data is : "nums
def max_heap(nums,i,a):
    r=i
    while r*2+1 <= a:
        child=r*2+1
        if child+1<= a and nums[child]<nums[child+1]:
            child+=1
        if child<= a and nums[r]<nums[child]:
            temp=nums[r]
            nums[r]=nums[child]
            nums[child]=temp
            r=child
        else:
            return
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
	make_heap(nums)

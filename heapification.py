def make_heap(nums):
    n=len(nums)
    for i in range((n-2)/2,-1,-1):
        max_heap(nums,i)
    print nums
def max_heap(nums,i):
    l=(2*i)+1
    if l<=len(nums) and nums[l]>nums[i]:
        large=l
    else:
        large=i
    if l+1<len(nums) and nums[l+1]>nums[large]:
        large=l+1
    if large !=i:
        temp=nums[i]
        nums[i]=nums[large]
        nums[large]=temp
        max_heap(nums,large)
#def heap_sort(nums):
    #pass
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
	#nums=heap_sort(nums)
	#print "\nsorted data is : ",nums

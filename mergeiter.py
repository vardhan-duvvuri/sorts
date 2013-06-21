def merge(n):
	size=1
	m=len(n)
	while size<m:
		temp=[]
		l1=0
		k=0
		while l1+size < m:
			l2=l1+size
			h1=l2-1
			h2=l2+size-1
			if h2>=m:
				h2=m-1
			i=l1
			j=l2
			while i<=h1 and j<=h2:
				if n[i]<n[j]:
					temp.append(n[i])
					print temp
					i+=1
				else:
					temp.append(n[j])
					print temp
					j+=1
			while i<=h1:
				temp.append(n[i])
				i+=1
				print temp
			while j<=h2:
				temp.append(n[j])
				j+=1
				print temp
			l1=h2+1
		for i in range(l1,m):
			temp.append(n[i])
		for i in range(0,m):
			n[i]=temp[i]
		size*=2
	print "\nsorted data is : ",n
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
	merge(nums)

def quick_sort(a,l,r):
	if l<r:
		pivot=l
		i=l
		j=r
		while i<j:
			while a[i]<=a[pivot] and i<r:
				i+=1
			while a[j]>a[pivot]:
				j-=1
			if i<j:
				temp=a[i]
				a[i]=a[j]
				a[j]=temp
		temp=a[pivot]
		a[pivot]=a[j]
		a[j]=temp
		quick_sort(a,l,j-1)
		quick_sort(a,j+1,r)

def get_data():
	a=[]
	while True:
		b=int(raw_input("Enter a number (-1 if done) : "))
		if b==-1:
			break
		a.append(b)
	return a

if __name__=='__main__':
	a=get_data()
	print "Input data is : ",a
	quick_sort(a,0,len(a)-1)
	print "sorted data is : ",a

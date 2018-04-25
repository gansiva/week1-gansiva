def print_hi():
	print("HI")

def do_n(f,n):
	for i in range(n):
		f()

n=int(input("Enter the times you want to call a fn: "))
do_n(print_hi,n)


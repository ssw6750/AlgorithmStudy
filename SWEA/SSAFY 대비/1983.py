g = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, int(input()) + 1):
	n, k = map(int, input().split())
	ar = []

	s = 0
	for i in range(n):
		a, b, c = map(int, input().split())
		ar.append(a*0.35 + b*0.40 + c*0.20) 

	s = ar[k-1]
	ar.sort(reverse=True)

	ans = ar.index(s)//(n//10)
	
	print('#{} {}'.format(t, g[ans]))
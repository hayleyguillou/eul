sum = 1

for i in range(7830457):
	sum *=2
	sum = sum % 1000000000000
	
print(sum*28433 +1) 

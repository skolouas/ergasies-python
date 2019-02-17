numbers = map(int, raw_input('Enter numbers: ').split())
print("The numbers you entered are: "+str(numbers))
ind = 0
max_num = numbers[0]
final_sub_array = []
for i in numbers:
	sum_numbers = 0
	sub_array = []
	for j in range(ind,len(numbers)):
		sum_numbers = sum_numbers + numbers[j]
		sub_array.append(numbers[j])
		if sum_numbers > max_num:
			max_num = sum_numbers
			final_sub_array =list(sub_array)
	ind = ind + 1
#ektypwsh megistou kai ypolistas		
print("MAX: "+str(max_num)+" : "+str(final_sub_array))


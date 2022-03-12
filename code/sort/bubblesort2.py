def bubble_sort(input_list):
	L = len(input_list)
	Round_num = L-1

	for rnd in range(Round_num):
		Iterations_per_round = L - rnd
		for iteration in range(Iterations_per_round):
			for i in range(0, L-1-iteration):
				if input_list[i] > input_list[i+1]:
					swap_value_by_index(input_list, i, i+1)

def swap_value_by_index(a_list, a, b):
    a_list[b], a_list[a] = a_list[a], a_list[b]

input_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before sorting:")
print(input_list)
bubble_sort(input_list)
print("After bubble sort:")
print(input_list)

import numpy as np
import time
# Завдання 1

length_of_array = int(input('Enter the length of array: '))
new_array = np.random.randint(low=-100, high=101, size=length_of_array)

for index, element in enumerate(new_array):
    print(f'cell - {index}, value - {element}')

# Завдання 2

sort_direction_for_bubble_sort = input('Now we will sort the array with Bubble sort. Enter the direction of sort(ascending or descending): ')
start_time = time.time()
for i in range(length_of_array - 1):
    for j in range(length_of_array - i - 1):
        if new_array[j] > new_array[j + 1] and sort_direction_for_bubble_sort == 'ascending':
            new_array[j], new_array[j + 1] = new_array[j + 1], new_array[j]
        elif new_array[j] < new_array[j + 1] and sort_direction_for_bubble_sort == 'descending':
            new_array[j], new_array[j + 1] = new_array[j + 1], new_array[j]

print(new_array)
end_time = time.time()
duration = end_time - start_time
print('Duration of this method is: ', duration)

# Завдання 3


sort_direction_for_insertion_sort = input('Now we will sort the array with Insertion sort. Enter the direction of sort(ascending or descending): ')
start_time1 = time.time()

for i in range(1, length_of_array):
    current_value = new_array[i]
    j = i - 1
    if j >= 0 and new_array[j] > current_value and sort_direction_for_insertion_sort == "ascending":
       new_array[j + 1] = new_array[j]
       j -= 1
    elif j >= 0 and new_array[j] < current_value and sort_direction_for_insertion_sort == "descending":
        new_array[j + 1] = new_array[j]
        j -= 1

    new_array[j + 1] = current_value

print(new_array)
end_time1 = time.time()
duration1 = end_time1 - start_time1
print('Duration of this method is: ', duration1)

# Завдання 4

sort_direction_for_selection_sort = input('Now we will sort the array with Selection sort. Enter the direction of sort(ascending or descending): ')
start_time2 = time.time()
for i in range(length_of_array - 1):
    min_index = i
    for j in range(i + 1, length_of_array):
        if sort_direction_for_selection_sort == "ascending":
            if new_array[j] < new_array[min_index]:
                min_index = j
        elif sort_direction_for_selection_sort == "descending":
            if new_array[j] > new_array[min_index]:
                min_index = j

    new_array[i], new_array[min_index] = new_array[min_index], new_array[i]

print(new_array)

end_time2 = time.time()
duration2 = end_time2 - start_time2
print('Duration of this method is: ', duration2)

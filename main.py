from help_instrument import counters
from sort_algorithm.heap_sort import heapSort
from sort_algorithm.insertion_sort import insertionSort
from help_instrument.csv_reader import read_file_csv

if __name__ == '__main__':
    file = input("Enter please filename:")
    ships = read_file_csv(file)

    n = len(ships)
    heapSort(ships)
    print("Sorted ship using heapsort")
    for i in range(n):
        print(ships[i])


    insertionSort(ships)
    print("Sorted ship using insertsort")
    for i in range(n):
        print(ships[i])
    print("#############################")
    print("amount swap in insertsort")
    print(counters.swap_counter_insert)
    print("amount compare in insertsort")
    print(counters.compare_counter_insert)
    print("#############################")
    print("amount of swap in heapsort")
    print(counters.swap_counter_heap)
    print("amount compare in heapsort")
    print(counters.compare_counter_heap)
    print("#############################")



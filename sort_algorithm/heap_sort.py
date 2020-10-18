from help_instrument import counters


def compare_element_from_heapsort(first_element, second_element):
    counters.compare_counter_heap += 1
    if first_element > second_element:

        return True
    else:

        return False


def heapify(ships, n, i):
    largest = i
    l = 2 * i
    r = 2 * i + 1

    if l < n and compare_element_from_heapsort(ships[i].tonnages, ships[l].tonnages):
        largest = l

    if r < n and compare_element_from_heapsort(ships[largest].tonnages, ships[r].tonnages):
        largest = r

    if largest != i:
        ships[i], ships[largest] = ships[largest], ships[i]  # swap
        counters.swap_counter_heap += 1
        heapify(ships, n, largest)



def heapSort(ships):
    n = len(ships)

    for i in range(n, -1, -1):
        heapify(ships, n, i)


    for i in range(n - 1, 0, -1):
        ships[i], ships[0] = ships[0], ships[i]  # swap
        counters.swap_counter_heap += 1
        heapify(ships, i, 0)

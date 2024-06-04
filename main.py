from insertion_sort import insertion_sort
from merge_sort import merge_sort
from datetime import datetime
from random import randint
import pandas as pd

n1 = 1000
A1 = [randint(1,1000000000) for i in range(n1)]
n2 = 10000
A2 = [randint(1,1000000000) for i in range(n2)]
n3 = 100000
A3 = [randint(1,1000000000) for i in range(n3)]
n4 = 1000000
A4 = [randint(1,1000000000) for i in range(n4)]

# Insertion
start_time_total = datetime.now()

# A1
start_time_1 = datetime.now()
insertion_sort(A1, n1)
end_time_1 = datetime.now()

# A2
start_time_2 = datetime.now()
insertion_sort(A2, n2)
end_time_2 = datetime.now()

# A3
start_time_3 = datetime.now()
insertion_sort(A3, n3)
end_time_3 = datetime.now()

# A4
start_time_4 = datetime.now()
insertion_sort(A4, n4)
end_time_4 = datetime.now()

# Total
end_time_total = datetime.now()

insertion_1 = end_time_1 - start_time_1
insertion_2 = end_time_2 - start_time_2
insertion_3 = end_time_3 - start_time_3
insertion_4 = end_time_4 - start_time_4
insertion_total = end_time_total - start_time_total


# Merge
start_time_total = datetime.now()

# A1
start_time_1 = datetime.now()
merge_sort(A1, 0, n1)
end_time_1 = datetime.now()

# A2
start_time_2 = datetime.now()
merge_sort(A2, 0, n2)
end_time_2 = datetime.now()

# A3
start_time_3 = datetime.now()
merge_sort(A3, 0, n3)
end_time_3 = datetime.now()

# A4
start_time_4 = datetime.now()
merge_sort(A4, 0, n4)
end_time_4 = datetime.now()

end_time_total = datetime.now()

merge_1 = end_time_1 - start_time_1
merge_2 = end_time_2 - start_time_2
merge_3 = end_time_3 - start_time_3
merge_4 = end_time_4 - start_time_4
merge_total = end_time_total - start_time_total


total = {
    'InsertionSort': {
        f'{n1}': str(insertion_1),
        f'{n2}': str(insertion_2),
        f'{n3}': str(insertion_3),
        f'{n4}': str(insertion_4),
        'total': str(insertion_total)
    },
    'MergeSort': {
        f'{n1}': str(merge_1),
        f'{n2}': str(merge_2),
        f'{n3}': str(merge_3),
        f'{n4}': str(merge_4),
        'total': str(merge_total)
    }
}

print('\n\n\n',pd.DataFrame(total))

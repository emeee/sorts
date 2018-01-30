class MergeSort:

    def sort(self, array):
        return self.algorithm(array)

    def algorithm(self, array):
        left = []
        right = []
        n = len(array)
        if n < 2:
            return array
        mid = n/2
        left <- self.divide_array(array, 0, mid)
        right <- self.divide_array(array, mid+1, n)
        self.algorithm(left)
        self.algorithm(right)
        self.merge(left, right, array)

    def merge(self, array, left, right):
        nl = len(left)
        nr = len(right)
        i = 0
        j = 0
        k = 0
        while i < nl and j < nr:
            if left[i] <= right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        while i < nl:
            array[k] = left[i]
            i = i + 1
            k = k + 1

        while i < nr:
            array[k] = right[i]
            j = j + 1
            k = k + 1

    def divide_array(self, array, start, end):
        half = []
        i = 0
        for j in range(start, end):
            half[i] = array[j]
            i = i + 1
        return half

sorter = MergeSort()
print sorter.sort([1,3,2,4,9,5,2])

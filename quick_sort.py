class QuickSort:

    def sort(self, array):
        return self.algorithm(array, 0, len(array)-1)

    def algorithm(self, array, start, end):
        if start < end:
            pIndex = self.partition(array, start, end)
            self.algorithm(array, start, pIndex-1)
            self.algorithm(array, start, pIndex+1)
        return array

    def partition(self, array, start, end):
        pivot = array[end]
        pIndex = start
        for i in range(start, end-1):
            if array[i] <= pivot:
                self.swap(array, i, pIndex)
                pIndex += 1
        self.swap(array, pIndex, end)
        return pIndex

    def swap(self, array, i, j):
        tmp = array[j]
        array[j] = array[i]
        array[i] = tmp

sorter = QuickSort()
print sorter.sort([1,2,4,3])

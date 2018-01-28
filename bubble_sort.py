class BubbleSort:

    def sort(self, array):
        return self.algorithm(array)

    def algorithm(self, array):
        for i in range(0, len(array)-1):
            for j in range(0, len(array)-1-i):
                if array[j] > array[j+1]:
                    self.swap(array,j)
        return array

    def swap(self, array, j):
        tmp = array[j]
        array[j] = array[j+1]
        array[j+1] = tmp

sorter = BubbleSort()
print sorter.sort([1,2,4,3])

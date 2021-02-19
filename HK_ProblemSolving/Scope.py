class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximum_difference=0

    def computeDifference(self):
        j = 0
        while j < len(self.__elements) - 1:
            i = 1
            while i < len(self.__elements):
                data = abs(int(self.__elements[j]) - int(self.__elements[i]))
                if self.maximum_difference < data:
                    self.maximum_difference = data
                i = i + 1
            j = j + 1


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximum_difference)

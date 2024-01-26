class perform(object):
    def __init__(self, list1, list2) -> None:
        self.list1 = list1
        for i in range(len(list2)//2):
            temp = list2[i]
            list2[i] = list2[len(list2) - i - 1]
            list2[len(list2) - i - 1] = temp
        self.list2 = list2

    def add(self, list1, list2):
        try:
            if len(list1) != len(list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x + y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def sub(self, list1, list2):
        try:
            if len(list1) != len(list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x - y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def mul(self, list1, list2):
        try:
            if len(list1) != len(list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x * y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def div(self, list1, list2):
        try:
            if len(list1) != len(list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x / y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def mod(self, list1, list2):
        try:
            if len(list1) != len(list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x % y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def pow(self, list1, list2):
        try:
            if len(list1) != len(list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x ** y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def floordiv(self, list1, list2):
        try:
            if len(list1) != len(list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x // y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def and_(self, list1, list2):
        try:
            if len(list1) != len(list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x and y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def or_(self, list1, list2):
        try:
            if len(list1) != len(list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x or y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

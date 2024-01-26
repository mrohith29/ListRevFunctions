class perform(object):
    def __init__(self, list1, list2) -> None:
        self.list1 = list1
        self.list2 = list2
        try:
            if len(list1) != len(list2):
                raise ValueError("Length of lists are not equal")
            else:
               for i in range(len(self.list2)//2):
                    temp = self.list2[i]
                    self.list2[i] = self.list2[len(self.list2) - i - 1]
                    self.list2[len(self.list2) - i - 1] = temp
        except ValueError as e:
            print(e)        

    def add(self):
        try:
            if len(self.list1) != len(self.list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x + y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def sub(self):
        try:
            if len(self.list1) != len(self.list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x - y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def mul(self):
        try:
            if len(self.list1) != len(self.list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x * y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def div(self):
        try:
            if len(self.list1) != len(self.list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x / y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def mod(self):
        try:
            if len(self.list1) != len(self.list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x % y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def pow(self):
        try:
            if len(self.list1) != len(self.list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x ** y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def floordiv(self):
        try:
            if len(self.list1) != len(self.list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x // y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def and_(self):
        try:
            if len(self.list1) != len(self.list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x and y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

    def or_(self):
        try:
            if len(self.list1) != len(self.list2):
                raise ValueError("Length of lists are not equal")
            else:
                return [x or y for x, y in zip(self.list1, self.list2)]
        except ValueError as e:
            print(e)

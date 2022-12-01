class Exception:

    @staticmethod
    def only_int1():
        try:
            a = int(input("Enter a number: "))
        except ValueError:
            print("It must be an integer number. Try again")
            return Exception.only_int1()
        return a

    @staticmethod
    def only_int():
        try:
            a = int(input("Enter a starting year of the worker: "))
        except ValueError:
            print("It must be an integer number. Try again")
            return Exception.only_int()
        if len(str(a)) != 4:
            print("Year must be wrong. Try again")
            return Exception.only_int()
        else:
            return a

    @staticmethod
    def only_str():
        a = input("Enter a worker's department: ").title()
        if all([char.isalpha() for char in a]):
            return a
        else:
            print("Only letters are allowed")
            return Exception.only_str()

    @staticmethod
    def more_than_single_str():
        a = input("Enter name and surname of the worker: ").title()
        if all(x.isalpha() for x in a.split()):
            return a
        else:
            print("You should enter only words. Try again!")
            return Exception.more_than_single_str()


class Worker:
    __WORKERS_LST = []

    def __self__(self, full_name=None, department=None, starting_year=None):
        self.full_name = full_name
        self.department = department
        self.starting_year = starting_year

    def run_program(self):
        print("Enter a number of workers to be added below")
        n = Exception.only_int1()
        for w in range(n):
            self.__type_data()
        print(self.workers_lst)
        ask = input("Print 'y' to sort workers by year or print other symbol to exit: ")
        if ask == "y":
            self.__workers_sorted_by_st_year()

    @property
    def workers_lst(self):
        return self.__WORKERS_LST

    @workers_lst.setter
    def workers_lst(self, arg):
        self.__WORKERS_LST.append(arg)

    def __type_data(self):
        self.full_name = Exception.more_than_single_str()
        self.department = Exception.only_str()
        self.starting_year = Exception.only_int()
        worker = [self.full_name, {"Department": self.department, "starting_year": self.starting_year}]
        self.workers_lst = worker

    def __workers_sorted_by_st_year(self):
        print("Sort workers by starting year")
        year = Exception.only_int()
        sorted_lst = []
        for i in self.__WORKERS_LST:
            if i[1]["starting_year"] == year:
                sorted_lst.append(i[0])
        if len(sorted_lst) != 0:
            print("Workers sorted by year " + str(year) + " below: ")
            for i in sorted_lst:
                print(i)
        else:
            print("There are no workers who started ", year)


w = Worker()
w.run_program()

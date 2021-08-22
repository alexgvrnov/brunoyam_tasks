class StringVar:

    def __init__(self, s):
        self.__string = s

    def set(self, s_new):
        self.__string = s_new

    def get(self):
        return self.__string


string = StringVar(str(input('Please input string :')))

print('You have entered :', string.get())

string.set('Hello World')

print('String has been changed to: ', string.get())

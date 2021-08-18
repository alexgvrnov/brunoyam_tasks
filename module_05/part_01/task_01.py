class StringVar:

    def __init__(self, s):
        self.s = s

    def set(self, s_new):
        self.s = s_new

    def get(self):
        return self.s


string = StringVar(str(input('Please input string :')))

print('You have entered :', string.get())

string.set('Hello World')

print('String has been changed to: ', string.get())

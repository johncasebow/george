
class Calculator:

    def readInt(self, prompt):
        return int(input(prompt))

    def add(self, arg1, arg2):
        return arg1 + arg2

if __name__ == '__main__':
    cal = Calculator()
    first = cal.readInt("Enter a number ")
    second = cal.readInt("Enter another number ")
    print(cal.add(first, second))

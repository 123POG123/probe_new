class Read():
    def __init__(self, example, name, first):
        self.w = example
        self.e = name
        self.d = first

    def ff(self, name):
        return name + int(2)

    # def __str__(self, name):
    #     return self.e + "hello Mary"


a = Read(12, 12, 12)
w = a.ff

print(str(a))
print(w)

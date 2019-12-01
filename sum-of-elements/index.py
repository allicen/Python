class Buffer:
    def __init__(self):
        self.a = []
        self.b = []

    def add(self, *a):
        self.b += a
        while len(self.b) >= 5:
            if len(self.b) >= 5:
                summ = 0
                for i in range(5):
                    summ += self.b[i]
                print(summ)
                for i in range(5):
                    self.b.pop(0)
            else:
                break

    def get_current_part(self):
        return self.b
class HanoiTower:
    def __init__(self, n, source, target, auxiliary):
        self.n = n
        self.source = source
        self.target = target
        self.auxiliary = auxiliary
        self.move_stack = []

    def move_disk(self, from_tower, to_tower):
        print(f"Перемістіть диск з {from_tower} на {to_tower}")

    def hanoi_recursive(self, n, source, target, auxiliary):
        if n > 0:
            self.hanoi_recursive(n-1, source, auxiliary, target)
            self.move_disk(source, target)
            self.hanoi_recursive(n-1, auxiliary, target, source)

    def hanoi_iterative(self):
        while True:
            while self.n > 0:
                self.move_stack.append((self.n, self.source, self.target, self.auxiliary))
                self.n -= 1
                self.target, self.auxiliary = self.auxiliary, self.target

            if not self.move_stack:
                break

            n, source, target, auxiliary = self.move_stack.pop()
            self.move_disk(source, target)
            self.n = n - 1
            self.source, self.target, self.auxiliary = auxiliary, source, target

    def solve_recursive(self):
        self.hanoi_recursive(self.n, self.source, self.target, self.auxiliary)

    def solve_iterative(self):
        self.hanoi_iterative()


n = int(input("Введіть кількість дисків: "))
solver = HanoiTower(n, 'Вежа 1', 'Вежа 3', 'Вежа 2')

print("Рекурсивний підхід:")
solver.solve_recursive()

print("\nІтеративний підхід з використанням стеку:")
solver = HanoiTower(n, 'Вежа 1', 'Вежа 3', 'Вежа 2')
solver.solve_iterative()

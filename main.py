class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
            print(f"Рядок '{item}' додано до стеку.")
        else:
            print("Стек повний. Неможливо додати рядок.")

    def pop(self):
        if self.stack:
            item = self.stack.pop()
            print(f"Рядок '{item}' виштовхнуто зі стеку.")
            return item
        else:
            print("Стек порожній. Неможливо виштовхнути рядок.")
            return None

    def count(self):
        count = len(self.stack)
        print(f"Кількість рядків у стеку: {count}")
        return count




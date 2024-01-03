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

    def is_empty(self):
        if not self.stack:
            print("Стек порожній.")
            return True
        else:
            print("Стек не порожній.")
            return False

    def is_full(self):
        if len(self.stack) == self.max_size:
            print("Стек повний.")
            return True
        else:
            print("Стек не повний.")
            return False

    def clear(self):
        self.stack = []
        print("Стек очищено.")

    def peek(self):
        if self.stack:
            item = self.stack[-1]
            print(f"Значення верхнього рядка у стеку: '{item}'")
            return item
        else:
            print("Стек порожній. Неможливо отримати значення.")

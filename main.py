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



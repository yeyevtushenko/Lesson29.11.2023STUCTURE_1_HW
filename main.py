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

def main():
    max_size = int(input("Введіть максимальний розмір стеку: "))
    stack = Stack(max_size)

    while True:
        print("\nМеню:")
        print("1. Розмістити рядок у стек")
        print("2. Виштовхнути рядок зі стеку")
        print("3. Підрахунок кількості рядків у стеку")
        print("4. Перевірка, чи порожній стек")
        print("5. Перевірка, чи повний стек")
        print("6. Очищення стеку")
        print("7. Отримати значення без виштовхнення верхнього рядка зі стеку")
        print("0. Вийти з програми")

        choice = input("Виберіть опцію (1-8): ")

        if choice == '1':
            item = input("Введіть рядок для розміщення у стеку: ")
            stack.push(item)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.count()
        elif choice == '4':
            stack.is_empty()
        elif choice == '5':
            stack.is_full()
        elif choice == '6':
            stack.clear()
        elif choice == '7':
            stack.peek()
        elif choice == '0':
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

class HanoiTower:
    def __init__(self, n):
        self.n = n
        self.source = "Вежа 1"
        self.target = "Вежа 3"
        self.auxiliary = "Вежа 2"
        self.moves_stack = []

    def move_disk(self, from_tower, to_tower):
        print(f"Перемістіть диск з {from_tower} на {to_tower}")




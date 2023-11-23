class VacuumCleaner:
    def __init__(self, room_size):
        self.room = [[0] * room_size for _ in range(room_size)]
        self.x = 0
        self.y = 0

    def place_obstacle(self, x, y):
        self.room[x][y] = 1

    def move_up(self):
        if self.x > 0:
            self.x -= 1

    def move_down(self, room_size):
        if self.x < room_size - 1:
            self.x += 1

    def move_left(self):
        if self.y > 0:
            self.y -= 1

    def move_right(self, room_size):
        if self.y < room_size - 1:
            self.y += 1

    def clean_position(self):
        self.room[self.x][self.y] = 0

    def print_room(self):
        for row in self.room:
            print(row)
        print()

room_size = 5
vacuum = VacuumCleaner(room_size)

vacuum.place_obstacle(2, 3)
vacuum.place_obstacle(4, 1)

vacuum.move_right(room_size)
vacuum.clean_position()
vacuum.print_room()

vacuum.move_down(room_size)
vacuum.move_down(room_size)
vacuum.clean_position()
vacuum.print_room()

vacuum.move_left()
vacuum.clean_position()
vacuum.print_room()

vacuum.move_up()
vacuum.clean_position()
vacuum.print_room()

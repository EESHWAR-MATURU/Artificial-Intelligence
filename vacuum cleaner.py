class VacuumCleaner:
    def __init__(self, room_a_status, room_b_status, initial_location):
        self.room_a = "dirty" if room_a_status == 1 else "clean"
        self.room_b = "dirty" if room_b_status == 1 else "clean"
        self.location = "a" if initial_location == 0 else "b"

    def clean(self, room):
        print(f"Cleaning {room}")
        if room == "a":
            self.room_a = "clean"
        elif room == "b":
            self.room_b = "clean"

    def move(self, to_room):
        print(f"Moving to {to_room}")
        self.location = to_room

    def is_dirty(self, room):
        if room == "a":
            return self.room_a == "dirty"
        elif room == "b":
            return self.room_b == "dirty"

    def clean_all_rooms(self):
        while self.is_dirty("a") or self.is_dirty("b"):
            current_room = self.location

            if self.is_dirty(current_room):
                self.clean(current_room)

            if current_room == "a":
                self.move("b")
            else:
                self.move("a")

        print("All rooms are clean now.")


room_a_status = int(
    input("Enter status of room A (0 for clean, 1 for dirty): "))
room_b_status = int(
    input("Enter status of room B (0 for clean, 1 for dirty): "))
initial_location = int(
    input("Enter initial location (0 for room A, 1 for room B): "))

vacuum_cleaner = VacuumCleaner(room_a_status, room_b_status, initial_location)

vacuum_cleaner.clean_all_rooms()

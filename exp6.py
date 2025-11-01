

def vacuumCleaner():
    rooms = {}
    n = int(input("Enter number of rooms: "))
    for i in range(n):
        state = input(f"Enter state of room {i+1} (Clean/Dirty): ").lower()
        rooms[f"Room{i+1}"] = state

    print("\nInitial room states:", rooms)
    for room, state in rooms.items():
        if state == "dirty":
            print(f"Cleaning {room}...")
            rooms[room] = "clean"
    print("All rooms cleaned!\nFinal states:", rooms)

vacuumCleaner()

def time(dist, speed):
    if speed < 1 or speed > 200:
        print("Error")
        return None

    time_taken = (dist / speed) * (18 / 5)
    return time_taken

speed = int(input("Enter the speed of the train: "))
result = time(400, speed)

if result is not None:
    print(result)

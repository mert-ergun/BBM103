def Tower(disk, source, destination, auxiliary):
    if disk == 1:
        print("Move disk 1 from source {} to destination {}".format(source, destination))
        return

    Tower(disk - 1, source, auxiliary, destination)
    print("Move disk {} from source {} to destination {} ".format(disk, source, destination))
    Tower(disk - 1, auxiliary, destination, source)


Tower(3, 'A', 'B', 'C')

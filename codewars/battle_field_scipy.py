import numpy as np
from scipy.ndimage import find_objects, label


def validate_battlefield(field):
    field = np.array(field)
    return sorted(ship.size if min(ship.shape) == 1 else 0 for ship in (field[pos] for pos in find_objects(label(field, np.ones((3, 3)))[0]))) == [
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        3,
        3,
        4,
    ]


def validate_battlefield0(field):
    field = np.array(field)
    np_ones = np.ones((3, 3))
    labels = label(field, np_ones)[0]
    objects_pos = find_objects(labels)

    print("field:")
    print(field)
    print()
    print(labels)
    # [print(object) for object in objects_pos]

    ships_founded = [ship.size if min(ship.shape) == 1 else 0 for ship in (field[pos] for pos in objects_pos)]
    print(f"{ships_founded=}")

    ships_founded1 = []
    ships_founded2 = []
    print("pos:")
    for pos in objects_pos:
        print(pos)
        count = 0
        # ship_s = sum([sum(ship) for ship in (field[pos])])

        # print("\t ship_S ", ship_s)
        print(f"\t lenPOS  {len(field[pos])} lenCell:?")

        for ship in field[pos]:
            print("\t ship ", ship)
            print(f"\t\t shape: {ship.shape} size: {ship.size} len(ship) {len(ship)}")

            # value = ship.size if min(ship.shape) == 1 else 0
            count += sum(ship)

        if min(len(field[pos]), len(field[pos][0])) == 1:
            ships_founded1.append(sum(field[pos]).sum())

        else:
            ships_founded1.append(0)
        ships_founded2.append(sum(sum(ship) for ship in field[pos]))
    ships_founded3 = [sum(sum(ship) for ship in field[pos]) for pos in objects_pos]
    ships_founded4 = [
        # (sum(sum(ship)), ship.sum(), ship.size, ship.shape, min(ship.shape))
        sum(sum(ship)) if min(ship.shape) == 1 else 0  # ship.size
        for ship in (field[pos] for pos in objects_pos)
    ]

    ships_founded0 = [ship.size if min(ship.shape) == 1 else 0 for ship in (field[pos] for pos in objects_pos)]

    print(f"{ships_founded1=} ok")
    print(f"{ships_founded2=}")
    print(f"{ships_founded3=}")
    print(f"{ships_founded4=} ok")
    print("ships_founded4:")
    for result in ships_founded4:
        print(result)
    print(f"{ships_founded0=} ok")

    return sorted(ships_founded) == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]


field = [
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
]
# assert validate_battlefield(field) == True

field = [
    [1, 1, 1, 0],
    [
        0,
        0,
        0,
        0,
    ],
    [
        0,
        1,
        0,
        1,
    ],
    [
        1,
        0,
        0,
        1,
    ],
]
validate_battlefield(field)
assert validate_battlefield(field) is False

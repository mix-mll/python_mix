# one loop
from collections import OrderedDict
import numpy as np


class BattleField:
    def __init__(self, val_type=3) -> None:
        self.ships_size = OrderedDict({
            4: {"qty": 1, "name": "battleship", "count": 0, "pos": []},
            3: {"qty": 2, "name": "cruisers", "count": 0, "pos": []},
            2: {"qty": 3, "name": "destroyers", "count": 0, "pos": []},
            1: {"qty": 4, "name": "submarines", "count": 0, "pos": []},
        })
        self.iterations = {"active": 0, "pasive": 0}
        # self.validate = self.validate_np if use_np else self.validate_list
        val_types = {
            1: self.validate_np,
            2: self.validate_list,
            3: self.validate_v2,
        }
        self.validate = val_types[val_type]



    def pad_with_zeros(self, field):
        pad = [0] * (len(field) + 2)
        return [pad] + [[0] + line + [0] for line in field] + [pad]

    def find_ships(self, field):
        for i, j in np.ndindex(field.shape):
            if field[i][j] != 1:
                self.iterations["pasive"] += 1
                continue

            for ship_size, ship_data in self.ships_size.items():
                if not self.check_cell(field, ship_size, ship_data, i, j, is_horizontal=False):
                    self.check_cell(field, ship_size, ship_data, i, j, is_horizontal=True)

    def check_cell(self, field, ship_size, ship_data, i, j, is_horizontal):
        self.iterations["active"] += 1
        delta_j, delta_i = [ship_size, 1] if is_horizontal else [1, ship_size]

        ship = field[i : i + delta_i, j: j + delta_j]
        perimeter = field[i - 1 : i + delta_i + 1, j - 1 : j + delta_j + 1]

        match = int(ship_size == ship.sum() == perimeter.sum())
        ship_data["count"] += match

        # update values
        ship -= match
        if match: ship_data["pos"].append([i, j, is_horizontal])
        return match

    def validate_np(self, field):
        self.field = np.array(self.pad_with_zeros(field))
        self.find_ships(self.field)
        result = all(ship_data["qty"] == ship_data["count"]for _, ship_data in self.ships_size.items())
        #print(f"{self.iterations=}")
        return result
    
    def find_ship_type(self, ship_size):
        if self.ships_size[ship_size]["qty"] == 0:
            return True
        # find horizontal
        self.find_ships_and_clean_field(ship_size, is_horizontal=True)

        # transpose
        self.field  = [list(x) for x in zip(*self.field )]
        self.find_ships_and_clean_field(ship_size, is_horizontal=False)

        # transpose_back
        self.field  = [list(x) for x in zip(*self.field )]

        return self.ships_size[ship_size]["qty"] == self.ships_size[ship_size]["count"]

    def find_ships_and_clean_field(self, ship_size, is_horizontal):
        for i in range(1,  len(self.field) - 1):
            j = 1
            while j < len(self.field[i]) - ship_size:
            #for j in range(1, len(self.field[i]) - ship_size):
                if self.field[i][j] == 0:
                    j += 1
                    self.iterations["pasive"] += 1
                    continue
                self.iterations["active"] += 1
                ship = self.field[i][j: j + ship_size]
                ship_sum =  sum(ship)
                perimeter_sum = sum(
                        self.field[i-1][j-1: j + ship_size + 1] +
                        self.field[i+0][j-1: j + ship_size + 1] +
                        self.field[i+1][j-1: j + ship_size + 1]
                    )
                match = int(ship_size == ship_sum == perimeter_sum)
                self.ships_size[ship_size]["count"] += match
            
                if match:
                    self.ships_size[ship_size]["pos"].append([i, j, is_horizontal]) # i, j, isHorizontal maybe substrct 1 becouse of the padding
                    # clear ship so is easier to find smaller ships
                    # -1 will cover to double assingments                    
                    for k in range(j, j + ship_size):
                        self.field[i][k] -= 1
                j += (1 + ship_size * match)
       
    def validate_list(self, field):
        self.field = self.pad_with_zeros(field)
        results = [self.find_ship_type(ship_size) for ship_size in  self.ships_size]
        #print(f"{self.iterations=}")
        return  all(results)

    def validate_v2(self, field):
        n, m = len(field), len(field[0])

        def cell(i, j):
            if i < 0 or j < 0 or i >= n or j >= m: return 0
            return field[i][j]
       
        def find(i, j):
            #   example
            #
            #   0 1 H  
            #   C V C
            #
            # check corners (C) in the next line to be free
            corners = cell(i + 1, j - 1) + cell(i + 1, j + 1)
            next_horizontal_cell = cell(i, j + 1)
            next_vertical_cell = cell(i + 1, j)
            if corners:
                return 0
 
            # it can be in only one direction
            if next_horizontal_cell and next_vertical_cell:
                return 0

            # mark field
            field[i][j] = 2

            # if horizontal
            if next_horizontal_cell:
                return find(i, j + 1) + 1

            # if vertical
            if next_vertical_cell:
                return find(i + 1, j) + 1

            # size 1
            return 1

        for i in range(len(field)):
            for j in range(len(field[0])):       
                if field[i][j] != 1:
                    continue
                ship_size = find(i, j)
                if ship_size < 1 or ship_size > 4: 
                    continue
                self.ships_size[ship_size]["count"] += 1

        return all(ship_data["qty"] == ship_data["count"]for _, ship_data in self.ships_size.items())
   
    def test_validate(val_type):
        print(f"test_validate {val_type=}")

        field = [
            [1, 1,],
            [0, 0,],
   
        ]
        assert False == BattleField(val_type).validate(field)
        field = [
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        ]
        battle_field =  BattleField(val_type)
        for i in range (1, 5):
            assert battle_field.ships_size[i]["count"] == 0
        result = battle_field.validate(field)
        assert battle_field.ships_size[4]["count"] == 2
        assert battle_field.ships_size[3]["count"] == 3
        assert battle_field.ships_size[2]["count"] == 3
        assert battle_field.ships_size[1]["count"] == 5
        assert False == result

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
        assert True == BattleField(val_type).validate(field)

        field = [
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        assert False == BattleField(val_type).validate(field)

        field = [
            [1, 0,],
            [0, 1,],
        ]
        assert False == BattleField(val_type).validate(field)

def validate_battlefield(field):
    return BattleField().validate(field)


BattleField.test_validate(val_type=1)
BattleField.test_validate(val_type=2)
BattleField.test_validate(val_type=3)

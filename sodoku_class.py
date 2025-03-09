import json 

from enum import Enum

class difficulty(Enum):
    EASY = 'test_easy.txt'
    MEDIUM = 'test_med.txt'
    HARD = 'test_hrd.txt'


class sodoku():
    def __init__(self, diff: difficulty):
        self.game_grid, self.solution = self._set_game(diff)
        self.grids = {
                'grid1':((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)),
                'grid2':((3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)),
                'grid3':((6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)),
                'grid4':((0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)),
                'grid5':((3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)),
                'grid6':((6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)),
                'grid7':((0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)),
                'grid8':((3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)),
                'grid9':((6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)),
                }
        self.vaild_values = (1,2,3,4,5,6,7,8,9)
    
    def _set_game(self, diff: difficulty):

        game_data_path = self._get_test_game(diff)

        with open(game_data_path) as f:
            data = json.load(f)

        return  data['newboard']['grids'][0]['value'], data['newboard']['grids'][0]['solution']

    def _get_test_game(self,diff: difficulty) -> str:
        match diff:
            case difficulty.EASY:
                return diff.value
            case difficulty.MEDIUM:
                return diff.value
            case difficulty.HARD:
                return diff.value
            case _:
                raise ValueError('Difficulty must be of class difficulty')

    def check_solution(self, guess:str) -> bool:
        return all(x == y for x, y in zip(guess,self.solution))

    def get_row(self,indx:int) -> list[int]:
        return self.game_grid[indx]

    def get_column(self,indx:int) -> list[int]:
        return_list = list()

        for row in self.game_grid:
            return_list.append(row[indx])

        return return_list

    def _get_sub_grid_values(self,grid_label:str) -> list[int]:
        pos_to_check = self.grids[grid_label]
        return_list = list()

        for i in pos_to_check:
            return_list.append(game_grid[i[1]][i[0]])
        
        return return_list
    
    def get_sub_grid(self, x, y) -> list[int]:
        for key, value in self.grids.items():
            if (x,y) in value:
                return_txt = key

        return get_sub_grid_values(game_board, return_txt)

    def print_game_grid(self):
        print('    0  1  2  3  4  5  6  7  8 ')
        print('------------------------------')
        for i in range(9):
            print(f'{i}| {self.game_grid[i]}')
            print('------------------------------')






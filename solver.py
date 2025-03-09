import json

grids = {
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

val_values = (1,2,3,4,5,6,7,8,9)

def get_game(pth:str) ->list|list:
    with open(pth, 'r') as f:
        data = json.load(f)


    game_grid = data['newboard']['grids'][0]['value']
    solution = data['newboard']['grids'][0]['solution']

    return game_grid,solution

def check_solution(guess:str, solution:str) -> bool:
    return all(x == y for x, y in zip(guess,solution))

def check_row(row:list[int], value:int) -> bool:
    if value in row:
        return True
    return False

def get_column(game_board:list, column) -> list:
    return_list = list()

    for row in game_board:
        return_list.append(row[column])

    return return_list

def get_sub_grid_values(game_board:list[list[int]], grid:str) -> list:
    pos_to_check = grids[grid]
    return_list = list()

    for i in pos_to_check:
        return_list.append(game_board[i[1]][i[0]])
    
    return return_list


def get_sub_grid(game_board:list[list[int]], x,y) -> list:

    for key, value in grids.items():
        if (x,y) in value:
            return_txt = key

    return get_sub_grid_values(game_board, return_txt)

def check_if_value_vaild(game_board:list[list[int]],x:int,y:int,guess:int) -> bool:
    row = game_board[y]
    column = get_column(game_board,x)
    grid = get_sub_grid(game_board, x,y)


    if guess in row:
        return False
    elif guess in column:
        return False
    elif guess in grid:
        return False
    else:
        return True

def get_guess_dict(game_board:list[list[int]]) -> dict:
    pos_list = list()

    for i in range(0,9):
        for i2 in range(0,9):
            pos_list.append((i2,i))

    pos_dict = dict()
    for i in pos_list:
        if game_board[i[1]][i[0]] == 0:
            pos_dict[i]= game_board[i[1]][i[0]]  

    return pos_dict

def update_game_grid(game_board:list[list[int]], x, y, value):
    if check_if_value_vaild(game_board,x,y,value) == True:
        game_board[y][x] = value
    
def guess_values(gam):
    guess_dict = get_guess_dict(gam)

    for k, v in guess_dict.items():
        vaild_list = list()
        for val in val_values:
            if check_if_value_vaild(gam, k[0],k[1], val) == True:
                vaild_list.append(val)

            
        if len(vaild_list) == 1:
            print(f'Updateding x{k[0]}, y{k[1]} to {vaild_list[0]}')
            update_game_grid(gam, k[0],k[1], vaild_list[0])

        else:
            guess_dict[k] = vaild_list

    for k,v in guess_dict.items():
        print(f'{k}: {v}')


def main():
    gam , sol = get_game('test1.txt')

    for i in gam:
        print(i)
    print('---------------------------')
    guess_values(gam)
    print('---------------------------')
    for i in gam:
        print(i)

    guess_values(gam)
    print('---------------------------')
    for i in gam:
        print(i)

    guess_values(gam)
    print('---------------------------')    
    for i in gam:
        print(i)

    guess_values(gam)
    print('---------------------------')    
    for i in gam:
        print(i)

    print(f'did it work: {check_solution(gam, sol)}')




if __name__ == "__main__":
    main()
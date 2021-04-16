maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]
visited = []
exits = []

def is_bad_cell(x, y):
    return y < 0 or x < 0 or x >= len(maze[0]) or y >= len(maze) or maze[y][x] == "#"

def try_go(x, y):
    if is_bad_cell(x, y):
        return

    if (x, y) in visited:
        return
    
    visited.append((x, y))
        
    if maze[y][x].isalpha() and maze[y][x] not in exits:
        exits.append(maze[y][x])

    try_go(x, y+1)
    try_go(x, y-1)
    try_go(x+1, y)
    try_go(x-1, y)

x, y = map(int, input("Введите координаты x, y: ").split())
try_go(x, y)

if is_bad_cell(x, y):
    print("Неверные координаты")
else:
    if (len(exits) == 0):
        print("Выходов нет")
    else:
        for exit in exits:
            print(exit, end=' ')
        print()

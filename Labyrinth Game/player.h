#ifndef PLAYER_H
#define PLAYER_H

typedef struct {    /*stores position of given char*/
    int row;
    int col;
} Position;

typedef struct {    /*stores position and direction faced char of enemy*/
    Position pos;
    char dir_facing; /*< > ^ V*/
} Enemy;

void find_position(char **map, int rows, int cols, Position* player, Enemy* enemy, Position* goal_pos);
int move_player(char **map, int rows, int cols, Position* player, Enemy* enemy, char* key, int* treasure, int* goal, int* got_player);
int check_win(int* treasure, int* goal);
int check_lose(int* got_player);

#endif

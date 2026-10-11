#ifndef ENEMY_H
#define ENEMY_H

int is_free(char **map, int rows, int cols, int row, int col);
char get_direction_enemy(char facing, char direction);
int can_fwd(char** map, int rows, int cols, Enemy* enemy);
int can_lft(char** map, int rows, int cols, Enemy* enemy);
int can_rgt(char** map, int rows, int cols, Enemy* enemy);
void move_1_step(char next_dir, Enemy* enemy);
void move_enemy(char **map, int rows, int cols, Enemy* enemy, int *treasure, int* got_player);

#endif
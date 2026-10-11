#include <stdio.h>
#include <stdlib.h>
#include "terminal.h"
#include "player.h"
#include "enemy.h"
#include "map.h"

int is_free(char **map, int rows, int cols, int row, int col) { /*checks if enemy can move (if the path is empty)*/
    int free;
    free = 0;
    if ((row >= 0 && row < rows) && (col >= 0 && col < cols)) { /*if enemy is within borders*/
        
        if ((map[row][col] != 'W' && (map[row][col]) != 'T') &&  (map[row][col] != 'G')) {  
            /*checks if position row col is not a W or T or G*/
            free = 1;   /*free to move*/
        }
    }
    
    else {
        free = 0;
    }
            
    return free;
}

void move_enemy(char **map, int rows, int cols, Enemy* enemy, int *treasure, int* got_player) { 
    /*check forward, left & right before calling function to move enemy by 1 step*/
    int forward, left, right, random, old_row, old_col;
    char current_direction, new_dir;
    old_row = enemy->pos.row;
    old_col = enemy->pos.col;
    forward = 0;
    left = 0;
    right = 0;
    random = 0;
    current_direction = enemy->dir_facing;
    new_dir = enemy->dir_facing;
    forward = can_fwd(map, rows, cols, enemy);
    left = can_lft(map, rows, cols, enemy);
    right = can_rgt(map, rows, cols, enemy);

    if (forward == 1 && left == 0 && right == 0) {  /*case 1*/
        new_dir = get_direction_enemy(current_direction, 'F');
        
        
    }
        else if (forward == 1 && left == 1 && right == 0) { /*case 2*/
            random = randomUCP(0, 1);   /*forward = 0, left = 1*/

            if (random == 0) {  /*Go forward*/
                new_dir = get_direction_enemy(current_direction, 'F');
            }
                else if (random == 1) {  /*Go left*/
                    new_dir = get_direction_enemy(current_direction, 'L');
            }
        }

        else if (forward == 1 && left == 0 && right == 1) { /*case 3*/
            random = randomUCP(0, 1);   /*forward = 0, right = 1*/

            if (random == 0) {  /*Go forward*/
                new_dir = get_direction_enemy(current_direction, 'F');
            }
                else if (random == 1) {  /*Go right*/
                    new_dir = get_direction_enemy(current_direction, 'R');
            }
        }        

        else if (forward == 1 && left == 1 && right == 1) { /*case 4*/
            random = randomUCP(0, 2);   /*forward = 0, left = 1, right = 2*/

            if (random == 0) {  /*Go forward*/
                new_dir = get_direction_enemy(current_direction, 'F');
            }
                else if (random == 1) {  /*Go left*/
                    new_dir = get_direction_enemy(current_direction, 'L');
            }
                else if (random == 2) {  /*Go right*/
                    new_dir = get_direction_enemy(current_direction, 'R');
            }
        }

        else if (forward == 0 && left == 1 && right == 0) {  /*case 5*/
            new_dir = get_direction_enemy(current_direction, 'L');
            
        }

        else if (forward == 0 && left == 0 && right == 1) {  /*case 6*/
            new_dir = get_direction_enemy(current_direction, 'R');
            
        }

        else if (forward == 0 && left == 1 && right == 1) {  /*case 7*/
            random = randomUCP(0, 1);   /*left = 0, right = 1*/

            if (random == 0) {  /*Go left*/
                new_dir = get_direction_enemy(current_direction, 'L');
            }
                else if (random == 1) {  /*Go right*/
                    new_dir = get_direction_enemy(current_direction, 'R');
            }
        }

        else if (forward == 0 && left == 0 && right == 0) {  /*case 1*/
            new_dir = get_direction_enemy(current_direction, 'B');
        
    }


    move_1_step(new_dir, enemy);    /*gives the next position of enemy*/
    
    if (map[enemy->pos.row][enemy->pos.col] == 'P') {
        *got_player = 1;
        enemy->dir_facing = new_dir;
        map[old_row][old_col] = ' ';
        map[enemy->pos.row][enemy->pos.col] = enemy->dir_facing;
        return;
    }
    else {
        enemy->dir_facing = new_dir;
        map[old_row][old_col] = ' ';
        map[enemy->pos.row][enemy->pos.col] = enemy->dir_facing;
    }
    
    
    
}
char get_direction_enemy(char facing, char direction) {
    /*facing is current enemy char*/
    /*direction = F(forward), B(backward), L(left), R(right)*/
    /*new_direction is the char which the enemy will take to face a particular direction*/
    char new_direction; 

    /*For facing = <*/
    if (facing == '<' && direction == 'F') {
        new_direction = '<';
    }
        else if (facing == '<' && direction == 'B') {
        new_direction = '>';
    }
        else if (facing == '<' && direction == 'L') {
        new_direction = 'v';
    }
        else if (facing == '<' && direction == 'R') {
        new_direction = '^';
    }
    /*For facing = >*/
        else if (facing == '>' && direction == 'F') {
        new_direction = '>';
    }
        else if (facing == '>' && direction == 'B') {
        new_direction = '<';
    }
        else if (facing == '>' && direction == 'L') {
        new_direction = '^';
    }
        else if (facing == '>' && direction == 'R') {
        new_direction = 'v';
    }
    /*For facing = ^*/
        else if (facing == '^' && direction == 'F') {
        new_direction = '^';
    }
        else if (facing == '^' && direction == 'B') {
        new_direction = 'v';
    }
        else if (facing == '^' && direction == 'L') {
        new_direction = '<';
    }
        else if (facing == '^' && direction == 'R') {
        new_direction = '>';
    }
    /*For facing = v*/
        else if (facing == 'v' && direction == 'F') {
        new_direction = 'v';
    }
        else if (facing == 'v' && direction == 'B') {
        new_direction = '^';
    }
        else if (facing == 'v' && direction == 'L') {
        new_direction = '>';
    }
        else if (facing == 'v' && direction == 'R') {
        new_direction = '<';
    }
    return new_direction;
}

int can_fwd(char** map, int rows, int cols, Enemy* enemy){  /*checks if enemy can go forward*/
    int forward, chk_row, chk_col, free, row, col;
    char dir_fwd, current_dir;
    forward = 0;
    free = 0;
    chk_row = 0;
    chk_col = 0;
    row = enemy->pos.row;
    col = enemy->pos.col;
    current_dir = enemy->dir_facing;

    dir_fwd = get_direction_enemy(current_dir, 'F');
    if (dir_fwd == '<') {
        chk_row = row;
        chk_col = col - 1;
    }
        else if (dir_fwd == '>') {
            chk_row = row;
            chk_col = col + 1;
        }

        else if (dir_fwd == '^') {
            chk_row = row-1;
            chk_col = col;
        }

        else if (dir_fwd == 'v') {
            chk_row = row+1;
            chk_col = col;
        }
    
    free = is_free(map, rows, cols, chk_row, chk_col);
    if (free == 1) {
        forward = 1; /*if forward = 1 then it is possible for enemy to move forward, else enemy cannot */
    }
    else {
        forward = 0;
    }
    return forward;
}

int can_lft(char** map, int rows, int cols, Enemy* enemy){  /*checks if enemy can go left*/
    int left, chk_row, chk_col, free, row, col;
    char dir_lft, current_dir;
    left = 0;
    free = 0;
    chk_row = 0;
    chk_col = 0;
    row = enemy->pos.row;
    col = enemy->pos.col;
    current_dir = enemy->dir_facing;
    dir_lft = get_direction_enemy(current_dir, 'L');

    if (dir_lft == '<') {
        chk_row = row;
        chk_col = col - 1;
    }
        else if (dir_lft == '>') {
            chk_row = row;
            chk_col = col + 1;
        }

        else if (dir_lft == '^') {
            chk_row = row-1;
            chk_col = col;
        }

        else if (dir_lft == 'v') {
            chk_row = row+1;
            chk_col = col;
        }
    
    free = is_free(map, rows, cols, chk_row, chk_col);
    /*takes left position(chk_row & chk_col) to check if enemy can move left*/
    if (free == 1) {
        left = 1; /*if left = 1 then it is possible for enemy to move left, else enemy cannot */
    }
    else {
        left = 0;
    }
    return left;
}

int can_rgt(char** map, int rows, int cols, Enemy* enemy){  /*checks if enemy can go right*/
    int right, chk_row, chk_col, free, row, col;
    char dir_rgt, current_dir;
    right = 0;
    free = 0;
    chk_row = 0;
    chk_col = 0;
    row = enemy->pos.row;
    col = enemy->pos.col;
    current_dir = enemy->dir_facing;
    dir_rgt = get_direction_enemy(current_dir, 'R');

    if (dir_rgt == '<') {
        chk_row = row;
        chk_col = col - 1;
    }
        else if (dir_rgt == '>') {
            chk_row = row;
            chk_col = col + 1;
        }

        else if (dir_rgt == '^') {
            chk_row = row-1;
            chk_col = col;
        }

        else if (dir_rgt == 'v') {
            chk_row = row+1;
            chk_col = col;
        }
    
    free = is_free(map, rows, cols, chk_row, chk_col);
    if (free == 1) {
        right = 1; /*if right = 1 then it is possible for enemy to move right, else enemy cannot */
    }
    else {
        right = 0;
    }
    return right;
}

void move_1_step(char next_dir, Enemy* enemy) { /*moves enemy by 1 step*/
/*next_dir is the direction of the next enemy movement*/
int row, col, next_row, next_col;
row = enemy->pos.row;   /*current position of enemy*/
col = enemy->pos.col;
next_row = row;
next_col = col;
    if (next_dir == '<') {
            next_row = row;
            next_col = col - 1;
        }
            else if (next_dir == '>') {
                next_row = row;
                next_col = col + 1;
            }

            else if (next_dir == '^') {
                next_row = row-1;
                next_col = col;
            }

            else if (next_dir == 'v') {
                next_row = row+1;
                next_col = col;
            }

    /*by allocating next row & col to enemy pos struct, the movement of enemy is confirmed*/
    enemy->pos.row = next_row;
    enemy->pos.col = next_col;   /*provides the coordinate for next movement*/
}

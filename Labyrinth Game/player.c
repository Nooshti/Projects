#include <stdio.h>
#include <stdlib.h>
#include "map.h"
#include "terminal.h"
#include "player.h"
#include "undo.h"


void find_position(char **map, int rows, int cols, Position* player, Enemy* enemy, Position* goal_pos) {
    /*find initial position of player, enemy and goal*/
    int i, j, found_p, found_e, found_g;
    found_p = 0;    /*0 = not found player, 1 = found player*/
    found_e = 0;    /*0 = not found enemy, 1 = found enemy*/
    found_g = 0;    /*0 = not found goal, 1 = found goal*/

    for (i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            if (map[i][j] == 'P' && found_p == 0) {
                player->row = i;
                player->col = j;
                found_p = 1;
            }
                else if (map[i][j] == '<' && found_e == 0) {
                    enemy->pos.row = i;
                    enemy->pos.col = j;
                    enemy->dir_facing = '<';
                    found_e = 1;
                }

                else if (map[i][j] == 'G' && found_g == 0) {
                    goal_pos->row = i;
                    goal_pos->col = j;
                    found_g = 1;
                    
                }
        }
    }
}

int move_player(char **map, int rows, int cols, Position* player, Enemy* enemy, char* key, int* treasure, int* goal,int *got_player) {
    /*move player*/
    int i, j, found, new_row, new_col, valid_move;
    new_row = player->row;
    new_col = player->col;
    valid_move = 0;
    switch (*key) {
        case 'w':   /*move up*/
            found = 0; /*0 - not found location of player*/
            for (i = 0; i < rows && found == 0; i++) {
                for(j = 0; j < cols && found == 0; j++) {
                    new_row = i-1;
                    new_col = j;
                    if (map[i][j] == 'P') {
                        found = 1; /*found Player*/
                        if (new_row >= 0 && map[new_row][new_col] != 'W') {/*checks if player is going out of bounds or going through walls*/
                            if (map[new_row][new_col] == 'T') {
                                *treasure = 1;  /*player grabs the treasure*/
                                map[i][new_col] = ' ';
                                map[new_row][new_col] = 'P';  /*if player grabs the treasure then player moves in its location */
                                player->row = new_row; /*update player position*/
                                player->col = new_col;
                                valid_move = 1;
                            }
                                else if (map[new_row][new_col] == 'G' && *treasure == 1) {
                                    *goal = 1;  /*player reaches the goal*/
                                    map[i][new_col] = ' ';
                                    map[new_row][new_col] = 'P';  /*player reaches goal*/
                                    player->row = new_row; /*update player position*/
                                    player->col = new_col;
                                    valid_move = 1;
                                    
                                }
                                else if (map[new_row][new_col] == 'G' && *treasure == 0) {
                                    map[i][new_col] = 'P';
                                    map[new_row][new_col] = 'G';  /*player cannot win without grabbing treasure*/
                                    
                                }
                                else if (new_row == enemy->pos.row && new_col == enemy->pos.col) {
                           
                                    map[i][j] = ' ';
                                    map[new_row][new_col] = enemy->dir_facing; /*player touches enemy*/
                                    player->row = new_row;
                                    player->col = new_col;
                                    *got_player = 1;
                                    valid_move = 1;
                                }
                                else if ((map[new_row][new_col] == 'W') || (new_row < 0 && new_row > rows) || (new_col < 0 && new_col > cols)) {
                           
                                    valid_move = 0;
                                }
                            else {
                                map[i][new_col] = ' ';
                                map[new_row][new_col] = 'P';  /*can move if the next step is empty space*/
                                player->row = new_row; /*update player position*/
                                player->col = new_col;
                                valid_move = 1;
                            }
                        
                        }
                    }
                }
            }
            break;
        
        case 's':   /*move down*/
            found = 0;
            for (i = 0; i < rows && found == 0; i++) {
                for(j = 0; j < cols && found == 0; j++) {
                    new_row = i+1;
                    new_col = j;
                    if (map[i][j] == 'P') {
                        found = 1;
                        if ((i + 1 < rows) && map[new_row][new_col] != 'W') {
                            /*checks if player is going out of bounds or going through walls*/
                            if (map[new_row][new_col] == 'T') {
                                *treasure = 1;
                                map[i][new_col] = ' ';
                                map[new_row][new_col] = 'P';  
                                /*if player grabs the treasure then player moves in its location */
                                player->row = new_row; /*update player position*/
                                player->col = new_col;
                                valid_move = 1;
                            }
                                else if (map[new_row][new_col] == 'G' && *treasure == 1) {
                                    *goal = 1;  /*player reaches the goal*/
                                    map[i][new_col] = ' ';
                                    map[new_row][new_col] = 'P';  /*player reaches goal*/
                                    player->row = new_row; /*update player position*/
                                    player->col = new_col;
                                    valid_move = 1;
                                    
                                }
                                else if (map[new_row][new_col] == 'G' && *treasure == 0) {
                                    map[i][new_col] = 'P';
                                    map[new_row][new_col] = 'G';  /*player cannot win without grabbing treasure*/
                                    
                            }
                                else if (new_row == enemy->pos.row && new_col == enemy->pos.col) {
                                    map[i][new_col] = ' ';
                                    map[new_row][new_col] = enemy->dir_facing; /*player touches enemy*/
                                    player->row = new_row;
                                    player->col = new_col;
                                    *got_player = 1;
                                    valid_move = 1;
                                }

                                else if ((map[new_row][new_col] == 'W') || (new_row < 0 && new_row > rows) || (new_col < 0 && new_col > cols)) {
                           
                                    valid_move = 0;
                                }
                                
                            else{
                                map[i][new_col] = ' ';
                                map[new_row][new_col] = 'P';  /*can move if the next step is empty space*/
                                player->row = new_row; /*update player position*/
                                player->col = new_col;
                                valid_move = 1;
                            }
                            
                            
                        }
                        
                    }
                }
            }
            break;

        case 'a':   /*move left*/
            found = 0;
            for (i = 0; i < rows && found == 0; i++) {
                for(j = 0; j < cols && found == 0; j++) {
                    new_row = i;
                    new_col = j-1;
                    if (map[i][j] == 'P') {
                        found = 1;
                        if (j - 1 >= 0 && map[i][new_col] != 'W') {/*checks if player is going out of bounds or going through walls*/
                            if (map[i][new_col] == 'T') {
                                *treasure = 1;
                                map[i][j] = ' ';
                                map[i][new_col] = 'P';  /*if player grabs the treasure then player moves in its location */
                                player->row = i; /*update player position*/
                                player->col = new_col;
                                valid_move = 1;
                                
                                }
                                else if (map[i][new_col] == 'G' && *treasure == 1) {
                                    *goal = 1;  /*player reaches the goal*/
                                    map[i][j] = ' ';
                                    map[i][new_col] = 'P';  /*player reaches goal*/
                                    player->row = i; /*update player position*/
                                    player->col = new_col;
                                    valid_move = 1;
                                    
                                }
                                else if (map[i][new_col] == 'G' && *treasure == 0) {
                                    map[i][j] = 'P';
                                    map[i][new_col] = 'G';  /*player cannot win without grabbing treasure*/
                                    
                                }
                                else if (new_row == enemy->pos.row && new_col == enemy->pos.col) {
                                    
                                    map[i][new_col] = ' ';
                                    map[new_row][new_col] = enemy->dir_facing; /*player touches enemy*/
                                    player->row = new_row;
                                    player->col = new_col;
                                    *got_player = 1;
                                    valid_move = 1;
                                }

                                else if ((map[new_row][new_col] == 'W') || (new_row < 0 && new_row > rows) || (new_col < 0 && new_col > cols)) {
                           
                                    valid_move = 0;
                                }
                            else {
                                map[i][j] = ' ';
                                map[i][new_col] = 'P';  /*can move if the next step is empty space*/
                                player->row = i; /*update player position*/
                                player->col = new_col;
                                valid_move = 1;
                            }

                            
                        }
                    }
                }
            }
            break;

        case 'd':   /*move right*/
            found = 0;
            for(i = 0; i < rows && found == 0; i++) {
                for(j = 0; j < cols && found == 0; j++) {/*checks if player is going out of bounds or going through walls*/
                    new_row = i;
                    new_col = j+1;
                    if (map[i][j] == 'P') {
                        found = 1;
                        if (j + 1 < cols && map[i][new_col] != 'W') {
                            if (map[i][new_col] == 'T') {
                                *treasure = 1;
                                map[i][j] = ' ';
                                map[i][new_col] = 'P';  /*if player grabs the treasure then player moves in its location */
                                player->row = i; /*update player position*/
                                player->col = new_col;
                                valid_move = 1;
                            }
                                else if (map[i][new_col] == 'G' && *treasure == 1) {
                                    *goal = 1;  /*player reaches the goal*/
                                    map[i][j] = ' ';
                                    map[i][new_col] = 'P'; /*player reaches goal*/
                                    player->row = i; /*update player position*/
                                    player->col = new_col;
                                     valid_move = 1;
                                 
                                }
                                else if (map[i][new_col] == 'G' && *treasure == 0) {
                                    map[i][j] = 'P';
                                    map[i][new_col] = 'G'; /*player cannot win without grabbing treasure*/
                                    
                                }
                                
                                else if (new_row == enemy->pos.row && new_col == enemy->pos.col) {
                                    
                                    map[i][new_col] = ' ';
                                    map[new_row][new_col] = enemy->dir_facing; /*player touches enemy*/
                                    player->row = new_row;
                                    player->col = new_col;
                                    valid_move = 1;
                                    *got_player = 1;
                                }
                                
                                else if ((map[new_row][new_col] == 'W') || (new_row < 0 && new_row > rows) || (new_col < 0 && new_col > cols)) {
                           
                                    valid_move = 0;
                                }
                                
                            else {
                                map[i][j] = ' ';
                                map[i][new_col] = 'P';  /*can move if the next step is empty space*/
                                player->row = i; /*update player position*/
                                player->col = new_col;
                                valid_move = 1;
                            }
                            
                        }
                        
                    }
                }
            }
            break;
        
    }
    return valid_move;
}

int check_win(int* treasure, int* goal) {
    /*checks if player got treasure and goal*/
    int result;
    result = 0;
    if ((*treasure == 1) && (*goal == 1)) {
        result = 1;
    }
    else {
        result = 0;
    }
    return result;
}

int check_lose(int* got_player) {
    /*checks if enemy got player*/
    int result;
    result = 0;
    if (*got_player == 1) {
        result = 1;
    }
    else {
        result = 0;
    }
    return result;
}






    


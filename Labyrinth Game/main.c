#include <stdio.h>
#include <stdlib.h>
#include "map.h"
#include"terminal.h"
#include "player.h"
#include "enemy.h"
#include "undo.h"

int main(int argc, char** argv) { 
    int rows, cols, run, end, treasure, message_win, message_lose, goal, got_player, valid_move;
    char key;
    char** map;
    Position player = {0, 0};    /*initialise position of player*/
    Enemy enemy = {{0, 0}, '<'};    /*initialise position of enemy*/
    Position goal_pos;  /*initialise position of goal*/
    Undo_list u_list;   /*initialise linked list*/
    valid_move = 0;
    message_win = 0;    /*initialise message_win*/
    message_lose = 0;   /*initialise message_lose*/
    treasure = 0; /*initialise treasure*/
    goal = 0; /*initialise goal*/
    got_player = 0; /*initialise got_player*/   /*if got_player is 0, the enemy did not catch player yet, 1 = player caught*/
    end = 0; /*end ends the program if used */
    run = 0; /*determines if game keeps running*/

    create_undo_list(&u_list);  /*initialise undo linked list*/
    initRandom();   /*initialise random*/
    if (argc != 2) {
        printf("Usage: ./labyrinth <map_file>\n");
        return end; /*if there is no 2 arguments in terminal, program stops*/
    }

    
    map = load_map(argv[1], &rows, &cols); /*load map*/
    if (map == NULL) {  /*if map contains nothing then error message is printed and program ends*/
        printf("Error in loading map\n");
        return end;
    }

    find_position(map, rows, cols, &player, &enemy, &goal_pos);    
    /*finds initial position of player, enemy and goal in map*/
    disableBuffer(); /*disables the display letters when typed*/
    
    while (run == 0) {  /*the game keeps running as long as run == 0*/
        print_map(map, rows, cols, &treasure); /*print map*/
        scanf("%c", &key);  /*take letter entered*/
        if (key == 'w' || key == 's' || key == 'a' || key == 'd') {
            /*move player if letter entered matches the above letters*/
            save_snapshot(&u_list, map, rows, cols, &treasure, &player, &enemy);    /*takes a snapshot of game*/
            valid_move = move_player(map, rows, cols, &player, &enemy, &key, &treasure, &goal, &got_player);

            if (valid_move == 0) {  
                /*remove invalid movement (walking into walls or outside map border) from undo list*/
                current_state *remove_invalid_movement;
                remove_invalid_movement = pop_snapshot_first(&u_list);
                free_copy(remove_invalid_movement->map, rows);
                free(remove_invalid_movement);
            }
            
            
            message_win = check_win(&treasure, &goal);
            if (message_win == 1) {
                run = 1;
            }

            if (run == 0) {
                if (treasure == 0  && goal == 0 && got_player == 0 && valid_move == 1) { 
                    /*Player has not looted treasure and has not reached goal*/
                    move_enemy(map, rows, cols, &enemy, &treasure, &got_player);
                    if (run == 0){
                        message_lose = check_lose(&got_player);
                        if (message_lose == 1) {
                            run = 1;
                        }
                    }
                    
                    
                    if (run == 0) {
                        move_enemy(map, rows, cols, &enemy, &treasure, &got_player);
                        
                        message_lose = check_lose(&got_player);
                        
                        if (message_lose == 1) {
                            run = 1;
                        
                        }
                    
                    }
                }
            
                else if (treasure == 1 && goal == 0 && got_player == 0 && valid_move == 1) {   /*Player has looted treasure, thus making enemy furious*/
                    move_enemy(map, rows, cols, &enemy, &treasure, &got_player);
                    if (run == 0) {
                        message_lose = check_lose(&got_player);
                    }
                    if (message_lose == 1) {
                        run = 1;
                    }
                    if (run == 0){
                        move_enemy(map, rows, cols, &enemy, &treasure, &got_player);
                        message_lose = check_lose(&got_player);
                        if (message_lose == 1) {
                            run = 1;
                        }
                    }
                

                    if (run == 0){
                        move_enemy(map, rows, cols, &enemy, &treasure, &got_player);
                        message_lose = check_lose(&got_player);
                        if (message_lose == 1) {
                            run = 1;
                        }
                    }
                
            }
            }
            
        }

            else if (key == 'u') {
                undo_game(&u_list, &map, rows, cols, &treasure, &player, &enemy);
            }
        else {
            printf("invalid key\n");    
            /*if letter entered does not match the above letters then print invalid key*/
            
        }
}
    
    print_map(map, rows, cols, &treasure); /*print map*/
    enableBuffer(); /*enables the display letters when typed*/
    if (message_win == 1) {
        printf("You win!\n");
    }
        else if (message_lose == 1) {
            printf("You lose!\n");
    }
    free_undo_list(u_list.head, rows);  /*free linked list used to implement undo feature*/
    
    free_map(map, rows);    /*free map*/
    
   
    return end;


}

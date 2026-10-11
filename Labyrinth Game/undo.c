#include <stdio.h>
#include <stdlib.h>
#include "undo.h"
#include "player.h"
#include "map.h"

/*create and initialise the undo linked list*/
void create_undo_list(Undo_list *u_list){
    u_list->head = NULL;
}

void insert_snapshot_first(Undo_list *u_list, current_state *state){
    /*inserts snapshot into undo list*/
    UndoNode* new_node;
    new_node = malloc(sizeof(UndoNode));

    if (new_node != NULL) {
        new_node->data = state;
        new_node->next = u_list->head;
        u_list->head = new_node;
        }

}  

void* pop_snapshot_first(Undo_list *u_list){
    /*takes snapshot out of undo list*/
    void *result;
    UndoNode *remove_node;
    result = NULL;

    remove_node = u_list->head;
    if (remove_node == NULL){
        result = NULL;
    }
    else{
        result = remove_node->data;
        u_list->head = remove_node->next;
        free(remove_node);
    }
    return result;
}

void free_undo_list(UndoNode *head, int rows) {
    /*free linked list*/
    UndoNode *current_node;
    UndoNode *next_node;
    current_node = head;
    while (current_node != NULL) {
        next_node = current_node->next;
        free_copy(current_node->data->map, rows);
        free(current_node->data);
        free(current_node);
        current_node = next_node;
    }
}


void save_snapshot(Undo_list *u_list, char** map, int rows, int cols, int* treasure, Position* player, Enemy* enemy){
    
    current_state *state;
    state = malloc(sizeof(current_state));

    /*copy all positions of player and enemy and the possible looting of treasure*/
    state->map = copy_map(map, rows, cols);
    state->player = *player;
    state->has_treasure = *treasure;
    state->en = *enemy; 
    insert_snapshot_first(u_list, state);
    
}

void undo_game(Undo_list *u_list, char*** map, int rows, int cols, int* treasure, Position* player, Enemy* enemy){
    /*uses pop_snapshot_first to undo*/
    current_state *state;
    state = pop_snapshot_first(u_list);
    if (state == NULL){
        return;
    }
    
    free_map(*map, rows);   /*free current map*/

    /*shows the previous game state by updating*/
    *map = state->map;
    *player = state->player;
    *treasure = state->has_treasure;
    *enemy = state->en;
    free(state);    /*frees state*/
}
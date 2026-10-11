#ifndef UNDO_H
#define UNDO_H
#include "player.h"

typedef struct{ /*captures full snapshot of current game state*/
    char **map;
    Position player;
    int has_treasure;
    Enemy en;
}   current_state;

typedef struct UndoNode {
    current_state *data;
    struct UndoNode *next;
}   UndoNode;

typedef struct Undo_list {
    UndoNode *head;
} Undo_list;


void create_undo_list(Undo_list *u_list);
void insert_snapshot_first(Undo_list *u_list, current_state *state);
void* pop_snapshot_first(Undo_list *u_list);
void save_snapshot(Undo_list *u_list, char** map, int rows, int cols, int* treasure, Position* player, Enemy* enemy);
void undo_game(Undo_list *u_list, char*** map, int rows, int cols, int* treasure, Position* player, Enemy* enemy);
void free_undo_list(UndoNode *head, int rows);
#endif
#ifndef MAP_H
#define MAP_H

char** load_map(char* filename, int* rows, int* cols);
void print_map(char** map, int rows, int cols, int *treasure);
char ** copy_map(char** org, int rows, int cols);
void free_map(char** map, int rows);
void free_copy(char** copy, int rows);

#endif
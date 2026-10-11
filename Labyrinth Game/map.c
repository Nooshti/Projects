#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "map.h"
#include "terminal.h"

char** load_map(char* filename, int* rows, int* cols) { 
    /*loads map from txt file to malloc'ed 2d array. 
    if successful, the numbers are changed into player, walls, enemy and etc*/
    
    char** map;
    int i, j, a;
    int num;
    int success;
    FILE* f;
    success = 1;
    

    f = fopen(filename, "r"); /*Open file*/
    if (f == NULL) {    /*if file is empty, display error message*/
            perror("No file was found\n");
            map = NULL;
            success = 0;   /*return nothing*/
    }
    
        else if ((f != NULL) && (fscanf(f,"%d %d", rows, cols) != 2)) {
            map = NULL;
            success = 0;
            }
        
    if (success == 1) {
        map = (char**)malloc((*rows) * sizeof(char*));  /*allocate memory*/
        success = 1;
        if (map == NULL) {
            printf("Error: malloc failed for map rows\n");
            free(map); /*####EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE*/
            success = 0;
        }
    } 

    

    if (success == 1) {
        for (i = 0; i < *rows; i++) { /*allocate memory to each column of each row*/
            map[i] = (char*)malloc((*cols) * sizeof(char));
            if (map[i] == NULL) {   /*if memory is not allocated successfully to map[i], free map and close file*/
                success = 0;
                for (a = 0; a < *rows; a++) {    /*####EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE*/
                    free(map[a]);
                }
                free(map);
                map = NULL;
                success = 0;
        }
    }
    if (success == 1)  {
        for (i = 0; i < *rows; i++) {     /*store contents of filename inside of map*/
            for (j = 0; j < *cols; j++) {
                fscanf(f, "%d", &num);
                if (num == 0) {map[i][j] = ' ';}    /*Path*/
                if (num == 1) {map[i][j] = 'W';}    /*walls*/
                if (num == 2) {map[i][j] = 'G';}    /*Goal*/
                if (num == 3) {map[i][j] = 'T';}    /*Treasure*/
                if (num == 4) {map[i][j] = 'P';}    /*Player*/
                if (num == 5) {map[i][j] = '<';}    /*Enemy*/
                /*convert the numbers inside filename to char and change their foreground and background color*/
            }
        }
    }

    
    }
    if (f != NULL) {
    fclose(f);
    }
    return map;
    }
    


void print_map(char** map, int rows, int cols, int *treasure) {
    /*prints map with all changes(enemy/player movement)*/
    int i, j, k;
    int success;
    success = 1;
    
    system("clear");    /*clears screen before printing map*/
    
    if (map == NULL) {
        success = 0;
        printf("Error opening file\n");
    }

        else if (success == 1) {
            for (k = 0; k < (cols + 2); k++){ /*top border*/
                printf("*");
            }
            printf("\n");


        
            for (i = 0; i < rows; i++) {
                printf("*"); /*side border*/
                for(j = 0; j < cols; j++) {
                    
                    if (map[i][j] == 'W') {setBackground("white"); printf(" ");}
                        else if (map[i][j] == ' ') {setBackground("black"); printf(" ");}
                    
                    else {
                        if (map[i][j] == 'P') {setForeground("blue");}
                            else if (map[i][j] == '<') {setForeground("red");}
                                if ((map[i][j] == '<') && *treasure == 1) {
                                    setBackground("red");
                                    
                                }
                            else if (map[i][j] == '>') {setForeground("red");}
                                if ((map[i][j] == '>') && *treasure == 1) {
                                    setBackground("red");
                                }
                            else if (map[i][j] == '^') {setForeground("red");}
                                if ((map[i][j] == '^') && *treasure == 1) {
                                    setBackground("red");
                                }
                            else if (map[i][j] == 'v') {setForeground("red");}
                                if ((map[i][j] == 'v') && *treasure == 1) {
                                    setBackground("red");
                                }
                            else if (map[i][j] == 'G') {setBackground("green");}
                                
                            else if (map[i][j] == 'T') {setBackground("yellow");}
                        printf("%c", map[i][j]);
                    }
                    setForeground("reset");
                    setBackground("reset");
                }
                printf("*\n");  /*side border*/
            }
            
            
            for (k = 0; k < (cols + 2); k++){ /*bottom border*/
                printf("*");
            }
            printf("\n");
            printf("Press 'w' to move UP\n");
            printf("Press 's' to move DOWN\n");
            printf("Press 'a' to move LEFT\n");
            printf("Press 'd' to move RIGHT\n");
            printf("Press 'u' to move UNDO\n");
            newSleep(0.5);
            
        }
}

void free_map(char** map, int rows) {   /*free malloc'ed 2D array containing map*/
    int i, success;
    success = 1;
    if (map == NULL) {
        success = 0;
        perror("Error opening file\n");
    }

    if (success == 1) {
        for (i = 0; i < rows; i++) {
            free(map[i]);
        }
        free(map);
    }
}

char** copy_map(char** org, int rows, int cols) {   /*used for snapshot of game state*/
    /*org is the original 2D array of the map
    Function to create copy of map*/
    int i, j, a, success;
    char** copy;
    success = 1;

    copy = (char**)malloc(rows * sizeof(char*));
    success = 1;
    if (copy == NULL) {
            printf("Error: malloc failed for map rows\n");
            success = 0;
        }

    if (success == 1) {
        for (i = 0; i < rows; i++) {
            copy[i] = (char*)malloc(cols * sizeof(char));
            if (copy[i] == NULL) {   
                /*if memory is not allocated successfully to copy[i], free copy and close file*/
                    success = 0;
                    for (a = 0; a < rows; a++) {
                        free(copy[a]);
                    }
                    free(copy);
                    copy = NULL;
                    success = 0;
            }
        }
    }

    if (success == 1) {
        for (i = 0; i < rows; i++) {
            for (j = 0; j < cols; j++) {
                copy[i][j] = org[i][j];
            }
        }

    }

    return copy;
}

void free_copy(char** copy, int rows) { /*free malloc'ed 2D array containing copy of map*/
    int i, success;
    success = 1;
    if (copy == NULL) {
        success = 0;
        perror("Error opening file\n");
    }

    if (success == 1) {
        for (i = 0; i < rows; i++) {
            free(copy[i]);
        }
        free(copy);
    }
}
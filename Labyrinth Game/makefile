CC = gcc
CFLAGS = -Wall -ansi -pedantic
OBJ = main.o map.o terminal.o player.o enemy.o undo.o
EXEC = labyrinth

$(EXEC) : $(OBJ)
		$(CC) $(OBJ) -o $(EXEC)

main.o : main.c map.h terminal.h player.h enemy.h undo.h
		$(CC) -c main.c $(CFLAGS) main.c -c 

map.o : map.c map.h terminal.h
		$(CC) -c map.c $(CFLAGS) map.c -c 

terminal.o : terminal.c terminal.h
		$(CC) -c terminal.c $(CFLAGS) terminal.c -c 

player.o : player.c player.h undo.h
		$(CC) -c player.c $(CFLAGS) player.c -c 

enemy.o: enemy.c enemy.h terminal.h player.h map.h
		$(CC) -c enemy.c $(CFLAGS) enemy.c -c 

undo.o: undo.c undo.h player.h map.h
		$(CC) -c undo.c $(CFLAGS) undo.c -c 

clean:
	rm -f $(EXEC) $(OBJ)


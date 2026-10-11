#define _DEFAULT_SOURCE 
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"terminal.h"
#include <time.h>
#include<termios.h>

/*Contains functions which affect the display of the labyrinth game*/

void setForeground(char * color)    /*changes color of letters*/
{
    if(strcmp(color, "black") == 0)
    {
        printf("\033[30m");
    }
    else if(strcmp(color, "red") == 0)
    {
        printf("\033[31m");
    }
    else if(strcmp(color, "green") == 0)
    {
        printf("\033[32m");
    }
    else if(strcmp(color, "yellow") == 0)
    {
        printf("\033[33m");
    }
    else if(strcmp(color, "blue") == 0)
    {
        printf("\033[34m");
    }
    else if(strcmp(color, "magenta") == 0)
    {
        printf("\033[35m");
    }
    else if(strcmp(color, "cyan") == 0)
    {
        printf("\033[36m");
    }
    else if(strcmp(color, "white") == 0)
    {
        printf("\033[37m");
    }
    else if(strcmp(color, "reset") == 0)
    {
        printf("\033[39m");
    }
}

void setBackground(char * color)    /*changes background color of letters*/
{
    if(strcmp(color, "black") == 0)
    {
        printf("\033[40m");
    }
    else if(strcmp(color, "red") == 0)
    {
        printf("\033[41m");
    }
    else if(strcmp(color, "green") == 0)
    {
        printf("\033[42m");
    }
    else if(strcmp(color, "yellow") == 0)
    {
        printf("\033[43m");
    }
    else if(strcmp(color, "blue") == 0)
    {
        printf("\033[44m");
    }
    else if(strcmp(color, "magenta") == 0)
    {
        printf("\033[45m");
    }
    else if(strcmp(color, "cyan") == 0)
    {
        printf("\033[46m");
    }
    else if(strcmp(color, "white") == 0)
    {
        printf("\033[47m");
    }
    else if(strcmp(color, "reset") == 0)
    {
        printf("\033[49m");
    }
}

void newSleep(float sec) /*delays display by desired number of seconds*/
{
	struct timespec ts;
	ts.tv_sec = (int) sec;
	ts.tv_nsec = (sec - ((int) sec)) * 1000000000;
	nanosleep(&ts,NULL);
}

void disableBuffer()    /*enables to press a char without press Enter*/
{
    struct termios mode;

    tcgetattr(0, &mode);
    mode.c_lflag &= ~(ECHO | ICANON);
    tcsetattr(0, TCSANOW, &mode);
}

void enableBuffer() /*resets to normal*/
{
    struct termios mode;

    tcgetattr(0, &mode);
    mode.c_lflag |= (ECHO | ICANON);
    tcsetattr(0, TCSANOW, &mode);
}

/*call this function just ONCE at the beginning of your program before using the random number generator */
void initRandom()
{
    srand(time(NULL));
}

/* Will return random integer between *low* and *high* inclusive.
   If the low is larger than the high, it will return -1 instead.
   In theory, it still works with negative *low* and *high* (as long as low is not larger than high).
   Please ensure you call initRandom function once before starting using this function. */
int randomUCP(int low, int high)
{
    int number = -1;

    if(low <= high)
    {
        number = (rand() % (high-low+1)) + low;
    }

    return number;
}
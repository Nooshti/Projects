#ifndef TERMINAL_H
#define TERMINAL_H

void setForeground(char * color);
void setBackground(char * color);

void newSleep(float sec);

void disableBuffer();
void enableBuffer();

void initRandom();
int randomUCP(int low, int high);

#endif
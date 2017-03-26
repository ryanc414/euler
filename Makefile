CC = gcc
CFLAGS = -Wall -O3

all: src/problems/P1.o
	$(CC) -o bin/P1 src/problems/P1.o

clean:
	rm -f bin/*
	rm -f src/problems/*.o


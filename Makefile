CC = gcc
CFLAGS = -Wall -g -Og -L lib -I src/c_utils -I src/problems
LDLIBS = -lutils -lm
SRC = $(wildcard src/problems/*.c src/problems/*.h)
LIBSRC = $(wildcard src/c_utils/*.c src/c_utils/*.h)
PYSRC = $(wildcard src/problems/P*.py)
BIN = $(SRC:src/problems/%.c=bin/%)
PY = $(PYSRC:src/problems/%.py=bin/%)

.PHONY: all clean tests problems

all: problems tests

problems: lib/libutils.so $(BIN) $(PY)

tests: test/testutils test/testproblems problems

clean:
	rm -f bin/* lib/* test/*

bin/%: src/problems/%.c src/problems/%.h src/problems/problems.h lib/libutils.so
	$(CC) $(CFLAGS) $< -o $@ $(LDLIBS)

bin/%: src/problems/%.py
	ln -sf ../$< $@

lib/libutils.so: $(LIBSRC)
	$(CC) $(CFLAGS) -shared -fPIC -I src/c_utils src/c_utils/*.c -o lib/libutils.so

test/testutils: src/test/testutils.c $(LIBSRC) lib/libutils.so
	$(CC) $(CFLAGS) $< -o $@ $(LDLIBS)

test/testproblems: src/test/testproblems.py
	ln -sf ../$< $@


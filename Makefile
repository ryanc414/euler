CC = gcc
CFLAGS = -Wall -g -Og -L lib -I src/c_utils -I src/problems
SRC = $(wildcard src/problems/*.c src/problems/*.h)
LIBSRC = $(wildcard src/c_utils/*.c src/c_utils/*.h)
BIN = $(SRC:src/problems/%.c=bin/%)
LDLIBS = -lutils -lm
PYSRC = $(wildcard src/problems/P*.py)
PY = $(PYSRC:src/problems/%.py=bin/%)

.PHONY: all clean
all: lib/libutils.so $(BIN) $(PY)

bin/%: src/problems/%.c src/problems/%.h src/problems/problems.h lib/libutils.so
	$(CC) $(CFLAGS) $< -o $@ $(LDLIBS)

bin/%: src/problems/%.py
	ln -sf ../$< $@

lib/libutils.so: $(LIBSRC)
	$(CC) $(CFLAGS) -shared -fPIC -I src/c_utils src/c_utils/*.c -o lib/libutils.so

bin/testutils: src/test/testutils.c $(LIBSRC) lib/libutils.so
	$(CC) $(CFLAGS) $< -o $@ $(LDLIBS)

clean:
	rm -f bin/* lib/*


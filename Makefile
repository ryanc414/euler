CC = gcc
CFLAGS = -Wall -O3 -L lib -I src/c_utils -I src/problems
SRC = $(wildcard src/problems/*.c)
LIBSRC = $(wildcard src/c_utils/*.c)
BIN = $(SRC:src/problems/%.c=bin/%)
LDLIBS = -lutil -lm
PYSRC = $(wildcard src/problems/P*.py)
PY = $(PYSRC:src/problems/%.py=bin/%)

.PHONY: all clean
all: lib/libutil.so $(BIN) $(PY)

bin/%: src/problems/%.c src/problems/%.h src/problems/problems.h lib/libutil.so
	$(CC) $(CFLAGS) $< -o $@ $(LDLIBS)

bin/%: src/problems/%.py
	ln -sf ../$< $@

lib/libutil.so: $(LIBSRC)
	$(CC) $(CFLAGS) -shared -fPIC -I src/c_utils src/c_utils/*.c -o lib/libutil.so

clean:
	rm -f bin/* lib/*


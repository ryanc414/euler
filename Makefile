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

tests: test/test_c_utils test/test_py_utils test/test_problems problems

clean:
	rm -f bin/* lib/* test/*

bin/%: src/problems/%.c src/problems/%.h src/problems/problems.h lib/libutils.so
	$(CC) $(CFLAGS) $< -o $@ $(LDLIBS)

bin/%: src/problems/%.py
	ln -sf ../$< $@

bin/%: src/problems/%.hs
	ghc --make -dynamic $< -o $@

lib/libutils.so: $(LIBSRC)
	$(CC) $(CFLAGS) -shared -fPIC -I src/c_utils src/c_utils/*.c -o lib/libutils.so

test/test_c_utils: src/test/test_c_utils.c $(LIBSRC) lib/libutils.so
	$(CC) $(CFLAGS) $< -o $@ $(LDLIBS)

test/test_py_utils: src/test/test_py_utils.py $(PYUTILS)
	ln -sf ../$< $@

test/test_problems: src/test/test_problems.py
	ln -sf ../$< $@


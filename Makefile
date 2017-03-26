CC = gcc
CFLAGS = -Wall -O3 -L lib
SRC = $(wildcard src/problems/*.c)
LIBSRC = $(wildcard src/c_utils/*.c)
BIN = $(SRC:src/problems/%.c=bin/%)
LDLIBS = -lutil -lm
PYSRC = $(wildcard src/problems/P*.py)
PY = $(PYSRC:src/problems/%.py=bin/%)

.PHONY: all clean libutil
all: libutil $(BIN) $(PY)

$(BIN): bin/% : src/problems/% | bin
	mv $^ $@

$(PY): bin/% : src/problems/%.py | bin
	ln -sf ../$< $@

libutil: $(LIBSRC) 
	$(CC) $(CFLAGS) -shared -fPIC -I src/c_utils src/c_utils/*.c -o lib/libutil.so

clean:
	rm -f bin/* lib/*


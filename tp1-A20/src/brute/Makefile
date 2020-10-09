EXEC=closests_points.out											# Executable to create

############ 	Variables	 	 ############

SRC=$(wildcard *.cpp)
OBJECTS=$(SRC:.cpp=.o)

############ Compilation options ############

CC = g++
CFLAGS=-Wall -std=c++11 -pedantic -g

############ Makefile commands   ############

.PHONY: clean mrproper all remote

all: $(EXEC)

$(EXEC): $(OBJECTS)
	@echo $(OBJECTS)
	$(CC) -o $@ $^ $(LDFLAGS)


%.o: %.cpp
	@echo $(OBJECTS)
	$(CC) -o $@ -c $< $(CFLAGS)

clean:
	find . -name '*.o' -delete

mrproper: clean
	rm -rf $(EXEC)

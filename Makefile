######################################################
### Chess engine by Jeffrey Qian
### Makefile for compiling C++ code for the engine 
### v0.0.1
#####################################################

### **************************************************
# Build config
CXX       	:= g++
CXX_FLAGS 	:= -Wall -Wextra -std=c++17 -ggdb

BIN     	:= bin
SRC     	:= src
INCLUDE 	:= src
LIB     	:= lib
LIBRARIES   := 
EXECUTABLE  := Cypher

SOURCES 	:= $(shell find $(SRC) -name '*.cpp')

### **************************************************
# Targets
all: build run

all_clean: build flush run


build: clean $(BIN)/$(EXECUTABLE)

$(BIN)/$(EXECUTABLE): $(SRC)/*.cpp
	@echo "🚧 Building..."
	$(CXX) $(CXX_FLAGS) -I $(INCLUDE) -L $(LIB) $(SOURCES) -o $@ $(LIBRARIES)

flush:
	clear

run: 
	@echo "🚀 Executing..."
	./$(BIN)/$(EXECUTABLE)


clean:
	@echo "🧹 Cleaning..."
	-rm $(BIN)/*



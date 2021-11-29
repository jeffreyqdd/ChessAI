#pragma once
#include "types.h"
#include <iostream>
using namespace std;

// Gets on/off status of a bit in a bitboard.
#define GET_BIT(bitboard, square)       (bitboard &   (ONE_BB << (square)) )

// Sets a bit in a bitboard to on status. Returns.
#define SET_BIT(bitboard, square)       (bitboard |   (ONE_BB << (square)) )

// Sets a bit in a bitboard to off status. Reference.
#define SET_REF_BIT(bitboard, square)   (bitboard |=  (ONE_BB << (square)) )

// Sets a bit in a bitboard to off status. Returns.
#define POP_BIT(bitboard, square)       (bitboard &  ~(ONE_BB << (square)) )

// Sets a bit in a bitboard to off status. Reference.
#define POP_REF_BIT(bitboard, square)   (bitboard &= ~(ONE_BB << (square)) )

// Pretty print bitboard.
#define PRETTY_PRINT(bb)                                            \
    for (int rank = 0; rank < RANK_NUM; rank++) {                   \
        cout << RANK_NUM - rank << "  ";                            \
        for (int file = 0; file < FILE_NUM; file++) {               \
            int squareIdx = rank * RANK_NUM + file;                 \
            cout << (GET_BIT(bb, squareIdx) ? 'X' : '.') << ' '; \
        }                                                           \
        cout << '\n';                                               \
    }                                                               \
    cout << "\n   a b c d e f g h\n\n";                             \
    cout << "   bitboard = " << bb << "\n\n";                       


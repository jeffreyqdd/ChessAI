#include "bitboard.h"
#include <iostream>
using namespace std;
using namespace cypher;

/*************************************\
=======================================
Bit manipulation
=======================================
\*************************************/
u64 cypher::get_bit(const u64& bitboard, const int& square) {
    return bitboard & (ONE_BB << square);
}

void cypher::set_bit(u64& bitboard, const int& square) {
    bitboard |= (ONE_BB << square);
}

void cypher::pop_bit(u64& bitboard, const int& square) {
    bitboard &= ~(ONE_BB << square);
}

/*************************************\
=======================================
Attacks
=======================================
\*************************************/

u64 cypher::maskPawnAttacks(int square, cypher::Colors side) {
    // attacks bitboard
    u64 attacks = EMPTY_BB;

    // piece bitboard
    u64 bitboard = EMPTY_BB;

    //set piece on board
    set_bit(bitboard, square);
    printBitboard(bitboard);

    if (side == cypher::WHITE) {
        attacks |= bitboard >> 7;
        attacks |= bitboard >> 9;
    } else {
        attacks |= bitboard << 7;
        attacks |= bitboard << 9;
    }

    return attacks;
}

/*************************************\
=======================================
Input & Output
=======================================
\*************************************/
void cypher::printBitboard(u64 bb) {
    // loop over rank
    for (int rank = 0; rank < RANK_NUM; rank++) {
        //print rank
        cout << RANK_NUM - rank << "  ";
        
        // loop over file
        for (int file = 0; file < FILE_NUM; file++) {
            //convert to square index
            int squareIdx = rank * RANK_NUM + file;

            //print bit state (1 or 0)
            cout << (get_bit(bb, squareIdx) ? true : false) << ' ';
        }
        cout << '\n';
    }

    //print files
    cout << "\n   a b c d e f g h\n\n";

    //print numerical number for bitboard
    cout << "   bitboard = " << bb << "\n\n";
}

#include "../tools/tools.h"
#include "../tools/types.h"
#include "bitboard.h"
using namespace std;

namespace cypher {
    Bitboard pawnAttacks[64][2] = {};
    Bitboard getPawnMask(int square, Colors side) {
        // attacks bitboard
        Bitboard attacks = EMPTY_BB;

        // piece bitboard
        Bitboard bitboard = EMPTY_BB;

        //set piece on board
        SET_REF_BIT(bitboard, square);

        if (side == cypher::WHITE) {
            if ((bitboard >> 7) & ~A_FILE) attacks |= bitboard >> 7;
            if ((bitboard >> 9) & ~H_FILE) attacks |= bitboard >> 9;
        } else {
            if ((bitboard << 7) & ~H_FILE) attacks |= bitboard << 7;
            if ((bitboard << 9) & ~A_FILE) attacks |= bitboard << 9;
        }

        return attacks;
    }
    void initPawnAttacks() {
        for (int square = 0; square < 64; square++) {
            pawnAttacks[square][WHITE] = getPawnMask(square, WHITE);
            pawnAttacks[square][BLACK] = getPawnMask(square, BLACK);
        }
    }


    Bitboard knightAttacks[64] = {};
    Bitboard getKnightMask(int square) {
        // attacks bitboard
        Bitboard attacks = EMPTY_BB;

        // piece bitboard
        Bitboard bitboard = EMPTY_BB;

        //set piece on board
        SET_REF_BIT(bitboard, square);

        // right side
        if(bitboard & ~H_FILE) attacks |= bitboard << 17;
        if(bitboard & ~H_FILE) attacks |= bitboard >> 15;
        
        if(bitboard & ~GH_FILE) attacks |= bitboard << 10;
        if(bitboard & ~GH_FILE) attacks |= bitboard >> 6;

        // left side
        if(bitboard & ~A_FILE) attacks |= bitboard >> 17;
        if(bitboard & ~A_FILE) attacks |= bitboard << 15;
        
        if(bitboard & ~AB_FILE) attacks |= bitboard >> 10;
        if(bitboard & ~AB_FILE) attacks |= bitboard << 6;
    
        return attacks;
    }

    void initKnightAttacks() {
        for (int square = 0; square < 64; square++) {
            knightAttacks[square] = getKnightMask(square);
        }
    }
}

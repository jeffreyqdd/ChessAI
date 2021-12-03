#include "../tools/tools.h"
#include "../tools/types.h"
#include "bitboard.h"
using namespace std;

namespace cypher {
    bool HAS_INIT_CYPHER_BITBOARD = false;

    Bitboard pawnAttackMask[64][2]  = {};
    Bitboard knightAttackMask[64]   = {};
    Bitboard kingAttackMask[64]     = {};

    Bitboard pawnMoveMask[64][2]    = {};
    Bitboard knightMoveMask[64]     = {};
    Bitboard kingMoveMask[64]       = {};


    Bitboard getPawnAttackMask(int square, Colors side) {
        // attacks bitboard
        Bitboard attacks = EMPTY_BB;

        // piece bitboard
        Bitboard bitboard = EMPTY_BB;

        //set piece on bitboard
        SET_REF_BIT(bitboard, square);

        if (side == WHITE) {
            if ((bitboard >> 7) & ~A_FILE) attacks |= bitboard >> 7;
            if ((bitboard >> 9) & ~H_FILE) attacks |= bitboard >> 9;
        } else {
            if ((bitboard << 7) & ~H_FILE) attacks |= bitboard << 7;
            if ((bitboard << 9) & ~A_FILE) attacks |= bitboard << 9;
        }

        return attacks;
    }
    Bitboard getPawnMoveMask(int square, Colors side) {
        // move bitboard
        Bitboard moves = EMPTY_BB;

        // slider bitboard 
        Bitboard bitboard = SET_BIT(EMPTY_BB, square);
    

        if (side == WHITE) {
            if (bitboard & RANK_2) moves |= bitboard >> 16;
            moves |= bitboard >> 8;
        } else {
            if (bitboard & RANK_7) moves |= bitboard << 16;
            moves |= bitboard << 8;

        }
        return moves;
    }

    void initPawnAttackMask() {
        for (int square = 0; square < 64; square++) {
            pawnAttackMask[square][WHITE] = getPawnAttackMask(square, WHITE);
            pawnAttackMask[square][BLACK] = getPawnAttackMask(square, BLACK);
        }
    }
    void initPawnMoveMask() {
        for (int square = 0; square < 64; square++) {
            pawnMoveMask[square][WHITE] = getPawnMoveMask(square, WHITE);
            pawnMoveMask[square][BLACK] = getPawnMoveMask(square, BLACK);
        }
    }

    Bitboard getKnightAttackMask(int square) {
        // attacks bitboard
        Bitboard attacks = EMPTY_BB;

        // piece bitboard
        Bitboard bitboard = EMPTY_BB;

        //set piece on bitboard
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
    Bitboard getKnightMoveMask(int square) {
        return getKnightAttackMask(square);
    }
    void initKnightAttackMask() {
        for (int square = 0; square < 64; square++) {
            knightAttackMask[square] = getKnightAttackMask(square);
        }
    }
    void initKnightMoveMask() {
        for (int square = 0; square < 64; square++) {
            knightMoveMask[square] = getKnightMoveMask(square);
        }
    }


    Bitboard getKingAttackMask(int square) {
        //attacks bitboard
        Bitboard attacks = EMPTY_BB;

        //piece bitboard
        Bitboard bitboard = EMPTY_BB;

        //set piece on bitboard
        SET_REF_BIT(bitboard, square);

        if(bitboard & ~A_FILE) attacks |= bitboard << 7;
        if(bitboard & ~A_FILE) attacks |= bitboard >> 9;
        if(bitboard & ~A_FILE) attacks |= bitboard >> 1;
        
        if(bitboard & ~H_FILE) attacks |= bitboard >> 7;
        if(bitboard & ~H_FILE) attacks |= bitboard << 9;
        if(bitboard & ~H_FILE) attacks |= bitboard << 1;
        attacks |= bitboard << 8;
        attacks |= bitboard >> 8;

        return attacks;
    }
    Bitboard getKingMoveMask(int square) {
        return getKingAttackMask(square);
    }
    void initKingAttackMask(){
        for (int square = 0; square < 64; square++) {
            kingAttackMask[square] = getKingAttackMask(square);
        }
    }
    void initKingMoveMask() {
        for (int square = 0; square < 64; square ++) {
            kingMoveMask[square] = getKingMoveMask(square);
        }
    }


    void initAllMasks() {
        initPawnAttackMask();
        initPawnMoveMask();

        initKnightAttackMask();
        initKnightMoveMask();
        
        initKingAttackMask();
        HAS_INIT_CYPHER_BITBOARD = true;
    }
}

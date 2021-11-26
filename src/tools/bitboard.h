#pragma once
#include <cstdint>
using namespace std;

namespace cypher {
    /*************************************\
    =======================================
    typedefs, enums, and defines
    =======================================
    \*************************************/
    
    // define popular bitboards
    #define EMPTY_BB 0ULL
    #define ONE_BB 1ULL

    // define board constants
    #define RANK_NUM 8
    #define FILE_NUM 8

    // define datatype for bitboards
    typedef uint64_t u64;
    
    //enum board squares
    enum Square {
        a8, b8, c8, d8, e8, f8, g8, h8,
        a7, b7, c7, d7, e7, f7, g7, h7,
        a6, b6, c6, d6, e6, f6, g6, h6,
        a5, b5, c5, d5, e5, f5, g5, h5,
        a4, b4, c4, d4, e4, f4, g4, h4,
        a3, b3, c3, d3, e3, f3, g3, h3,
        a2, b2, c2, d2, e2, f2, g2, h2,
        a1, b1, c1, d1, e1, f1, g1, h1
    };

    //enum colors
    enum Colors {
        WHITE,
        BLACK
    };

    /*
    "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
    "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
    "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
    "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
    "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
    "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
    "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
    "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
    */

    /*************************************\
    =======================================
    Bit manipulation
    =======================================
    \*************************************/
    
    /*      NOT A FILE
        8  0 1 1 1 1 1 1 1 
        7  0 1 1 1 1 1 1 1 
        6  0 1 1 1 1 1 1 1 
        5  0 1 1 1 1 1 1 1 
        4  0 1 1 1 1 1 1 1 
        3  0 1 1 1 1 1 1 1 
        2  0 1 1 1 1 1 1 1 
        1  0 1 1 1 1 1 1 1 

           a b c d e f g h 
    */
    const u64 NOT_A_FILE = 18374403900871474942ULL;
    const u64 NOT_H_FILE = 9187201950435737471ULL;

    /**
     * Gets on/off status of a bit in a bitboard.
     * @param bitboard bitboard of interest
     * @param square square-th bit to check
     * @return bitboard with only the square-th bit kept on if it was on before
     */ 
    u64 get_bit(const u64& bitboard, const int& square);

    /**
     * Sets a bit in a bitboard to on status.
     * @param bitboard bitboard of interest
     * @param square square-th bit to set on
     */ 
    void set_bit(u64& bitboard, const int& square);

    /**
     * Sets a bit in a bitboard to off status.
     * @param bitboard bitboard of interest
     * @param square square-th bit to set off
     */ 
    void pop_bit(u64& bitboard, const int& square);

    /*************************************\
    =======================================
    Attacks
    =======================================
    \*************************************/

    //pawn attacks table [side][square]
    extern u64 pawnAttacks[2][64];

    /**
     * Generate bitmasks for pawn attacks.
     * @param square square the pawn is on
     * @param side color of the pawn
     */ 
    u64 maskPawnAttacks(int square, Colors side);

    /*************************************\
    =======================================
    Input & Output
    =======================================
    \*************************************/
    /**
     * Pretty print bitboard.
     * @param bb input bitboard
     */ 
    void printBitboard(u64 bb);


}




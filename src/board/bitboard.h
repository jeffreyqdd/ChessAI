#pragma once
#include "../tools/types.h"
#include "../tools/tools.h"
using namespace std;

namespace cypher {
    /************************************************************\
    * lookup values and tables
    \************************************************************/ 
    const Bitboard A_FILE = 72340172838076673ULL;
    const Bitboard B_FILE = 144680345676153346ULL;
    const Bitboard C_FILE = 289360691352306692ULL;
    const Bitboard D_FILE = 578721382704613384ULL;
    const Bitboard E_FILE = 1157442765409226768ULL;
    const Bitboard F_FILE = 2314885530818453536ULL;
    const Bitboard G_FILE = 4629771061636907072ULL;
    const Bitboard H_FILE = 9259542123273814144ULL;
    const Bitboard AB_FILE = (A_FILE | B_FILE);
    const Bitboard GH_FILE = (G_FILE | H_FILE);

    //en passant squares will need to be generated live
    extern Bitboard pawnAttacks[64][2];
    Bitboard getPawnMask(int square, Colors side);
    void initPawnAttacks();

    extern Bitboard knightAttacks[64];
    Bitboard getKnightMask(int square);
    void initKnightAttacks();


}

//     extern u64 pawnAttacks[64][2];
//     /**
//      * Generate bitmasks for pawn attacks.
//      * @param square square the pawn is on
//      * @param side color of the pawn
//      */ 
//     u64 maskPawnAttacks(int square, Colors side);
//     /**
//      * Precompute bitmasks for pawn attacks.
//      */ 
//     void initPawnAttacks();
//     /*************************************\
//     =======================================
//     Input & Output
//     =======================================
//     \*************************************/
//     /**
//      * Pretty print bitboard.
//      * @param bb input bitboard
//      */ 
//     void printBitboard(u64 bb);
//     /*************************************\
//     =======================================
//     Driver
//     =======================================
//     \*************************************/
//     /**
//      * Runs the necessary functions to populate all values.
//      */ 
//     void cypherInit();
// }




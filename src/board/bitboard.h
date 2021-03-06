#pragma once
#include "../tools/types.h"
#include "../tools/tools.h"
using namespace std;

namespace cypher {
    /************************************************************\
    * Bitboard section
    \************************************************************/
    extern bool HAS_INIT_CYPHER_BITBOARD;

    /************************************************************\
    * PRECOMPUTING LOOKUP VALUES AND TABLES
    * 
    * I define 
    *   1) attacks          - all possible capture squares
    *   2) moves            - all possible non capture squares
    *   3) sliding piece    - rooks, bishops, and queen
    \************************************************************/ 
 
    /* Note that bitshifts work in this setup as follows
    
        x << n; // plus (+) n bits
        x >> n; // minus (-) n bits

        NW             N            NE

                -9    -8    -7
                    \  |  /
        W       -1 <-  0 -> +1      E
                    /  |  \
                +7    +8    +9

        SW             S            SE
     
    */

    //%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    // PRECOMPUTED FILE BITBOARDS
    //%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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

    //%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    // PRECOMPUTED RANK BITBOARDS
    //%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    const Bitboard RANK_1 = 18374686479671623680ULL;
    const Bitboard RANK_2 = 71776119061217280ULL;
    const Bitboard RANK_3 = 280375465082880ULL;
    const Bitboard RANK_4 = 1095216660480ULL;
    const Bitboard RANK_5 = 4278190080ULL;
    const Bitboard RANK_6 = 16711680ULL;
    const Bitboard RANK_7 = 65280ULL;
    const Bitboard RANK_8 = 255ULL;

    //%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    // NON SLIDING PIECE ATTACK AND MOVE LOOKUP
    //%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    extern Bitboard pawnAttackMask[64][2];
    extern Bitboard pawnMoveMask[64][2];

    extern Bitboard knightAttackMask[64];
    extern Bitboard knightMoveMask[64];

    extern Bitboard kingAttackMask[64];
    extern Bitboard kingMoveMask[64];

    Bitboard getPawnAttackMask(int square, Colors side);
    Bitboard getPawnMoveMask(int square, Colors side);
    void initPawnAttackMask();
    void initPawnMoveMask();

    Bitboard getKnightAttackMask(int square);
    Bitboard getKnightMoveMask(int square);
    void initKnightAttackMask();
    void initKnightMoveMask();

    Bitboard getKingAttackMask(int square);
    Bitboard getKingMoveMask(int square);
    void initKingAttackMask();
    void initKingMoveMask();




    void initAllMasks();



    //sliding-piece 


    class Board {
        private:
        Bitboard PAWNS[2];
        Bitboard KNIGHTS[2];
        Bitboard BISHOPS[2];
        Bitboard QUEEN[2];
        Bitboard KING[2];
       
        public:
        Board();
        Board(string fen);

    };
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




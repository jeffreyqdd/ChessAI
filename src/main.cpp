#include <chrono>
#include <assert.h>
#include "tools/tools.h"
#include "board/bitboard.h"

using namespace std;

int main() {     
    cypher::initAllMasks();
    for (int i = 0; i < 64; i++) {
        assert(cypher::knightMoveMask[i] == cypher::knightAttackMask[i]);
        assert(cypher::kingMoveMask[i] == cypher::kingAttackMask[i]);
    }
    // assert (cypher::knightMoveMask == cypher::knightAttackMask);
    // for(int i = 0; i < 64; i++) {
    //     PRETTY_PRINT(cypher::pawnMoveMask[i][cypher::WHITE]);
    // }

    // for (int i = 0; i < 8; i++) {
    //     Bitboard bitboard = EMPTY_BB;

    //     for (int rank = 0; rank < RANK_NUM; rank ++) { 
    //         for (int file = 0; file < FILE_NUM; file ++) {
    //             int square = rank * RANK_NUM + file;
    //             if (rank == i) SET_REF_BIT(bitboard, square);
    //         }
    //     }

    // PRETTY_PRINT(4629771061636907072ULL);

    // }


    // for (int i = 0; i < 64; i++) {
        // PRETTY_PRINT(cypher::kingAttackMask[i]);
    // }
    // PRETTY_PRINT(1157442765409226768ULL)


    
    // cypher::cypherInit();
    // cypher::u64 pawn = EMPTY_BB;
    
    // set_bit(pawn, cypher::e4);

    // cypher::printBitboard(~(cypher::A_FILE | cypher::B_FILE));
    //cypher::printBitboard(cypher::pawnAttacks[cypher::e4][cypher::BLACK] );
    

    // for (int i = 0; i < 8; i++) {
    //     cypher::u64 bitboard = EMPTY_BB;
    //     for (int rank = 0; rank < RANK_NUM; rank++) {
    //         for(int file = 0; file < FILE_NUM; file++) {
    //             int square = rank * RANK_NUM + file;
    //             if (file == i) cypher::set_bit(bitboard, square);
    //         }
    //     }
    //     cypher::printBitboard(bitboard);        
    // }



    return 0;
}

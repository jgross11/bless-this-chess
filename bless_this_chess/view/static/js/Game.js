Game = () => {
    let obj = {};
    obj = {
        players: 2,                     // number of players
        dimensions: {                   // board dimensions
            width: 8,
            height: 8,
        },
        playerTurn: 1,                  // player whose turn it is
        board: [                        // representation of board
            [-2,-3,-4,-5,-6,-4,-3,-2],  // positive values are white
            [-1,-1,-1,-1,-1,-1,-1,-1],  // negative values are black
            [ 0, 0, 0, 0, 0, 0, 0, 0],  // values are indices in pieces array (below)
            [ 0, 0, 0, 0, 0, 0, 0, 0],  // zero is empty space
            [ 0, 0, 0, 0, 0, 0, 0, 0],  // yes this isn't extendable to n players
            [ 0, 0, 0, 0, 0, 0, 0, 0],  // value could be nk, where k is index and n is player #
            [ 1, 1, 1, 1, 1, 1, 1, 1],
            [ 2, 3, 4, 5, 6, 4, 3, 2]
        ],
        primaryTileColor: "white",      // tile colors
        secondaryTileColor: "black",
        winRules: {},                   // collection of rules for this game
        drawRules: {},                  // good luck
        pieces: [
            {}, // :)                   // empty square representation
            {                           // currently pieces are just names (used for sprite fetching)
                name: "pawn",           // and "moves" array
                moves: [{
                    type: 0,             // 0 = offset (one time movement), 1 = pattern (row movement)
                    dx: 0, 
                    dy: 1
                }],
            },
            {
                name: "rook",
                moves: [
                    {
                        type: 1,
                        dx: 1,
                        dy: 0,
                    },
                    {
                        type: 1,
                        dx: -1,
                        dy: 0
                    },
                    {
                        type: 1,
                        dx: 0,
                        dy: 1,
                    },
                    {
                        type: 1,
                        dx: 0,
                        dy: -1
                    }
                ],
            },
            {
                name: "knight",
                moves: [
                    {
                        type: 0,
                        dx: 1, 
                        dy: 2
                    },
                    {
                        type: 0,
                        dx: 1, 
                        dy: -2
                    },
                    {
                        type: 0,
                        dx: -1, 
                        dy: 2
                    },
                    {
                        type: 0,
                        dx: -1, 
                        dy: -2
                    },
                    {
                        type: 0,
                        dx: 2, 
                        dy: 1
                    },
                    {
                        type: 0,
                        dx: -2, 
                        dy: 1
                    },
                    {
                        type: 0,
                        dx: 2, 
                        dy: -1
                    },
                    {
                        type: 0,
                        dx: -2, 
                        dy: -1
                    }
                ],
            },
            {
                name: "bishop",
                moves: [
                    {
                        type: 1,
                        dx: 1,
                        dy: 1
                    },
                    {
                        type: 1,
                        dx: -1,
                        dy: 1
                    },
                    {
                        type: 1,
                        dx: 1,
                        dy: -1
                    },
                    {
                        type: 1,
                        dx: -1,
                        dy: -1
                    }
                ],
            },
            {
                name: "queen",
                moves: [
                    {
                        type: 1,
                        dx: 1,
                        dy: 1
                    },
                    {
                        type: 1,
                        dx: -1,
                        dy: 1
                    },
                    {
                        type: 1,
                        dx: 1,
                        dy: -1
                    },
                    {
                        type: 1,
                        dx: -1,
                        dy: -1
                    },
                    {
                        type: 1,
                        dx: 1,
                        dy: 0,
                    },
                    {
                        type: 1,
                        dx: -1,
                        dy: 0
                    },
                    {
                        type: 1,
                        dx: 0,
                        dy: 1,
                    },
                    {
                        type: 1,
                        dx: 0,
                        dy: -1
                    }
                ],
            },
            {
                name: "king",
                moves: [
                    {
                        type: 0,
                        dx: 1,
                        dy: 0
                    },
                    {
                        type: 0,
                        dx: 1,
                        dy: 1
                    },
                    {
                        type: 0,
                        dx: 0,
                        dy: 1
                    },
                    {
                        type: 0,
                        dx: -1,
                        dy: 1
                    },
                    {
                        type: 0,
                        dx: -1,
                        dy: 0
                    },
                    {
                        type: 0,
                        dx: -1,
                        dy: -1
                    },
                    {
                        type: 0,
                        dx: 0,
                        dy: -1
                    },
                    {
                        type: 0,
                        dx: 1,
                        dy: -1
                    }
                ],
            },
        ],

        // determine if x and y are within bounds of (assumed filled rectangular) board
        // this can very easily be modified to accomodate a board of any size / swiss-cheesiness 
        // by populating the square border of the actual shape of the board with a special value
        // to indicate a tile pieces can't move to
        coordsInBoard(x,y){ 
            return 0 <= x && x < this.dimensions.width && 0 <= y && y < this.dimensions.height
        },

        isValidMove(pieceX, pieceY, newX, newY){

            // don't process silly move requests
            if(!this.coordsInBoard(pieceX, pieceY) || !this.coordsInBoard(newX, newY)) return false;

            // get type of piece at this position
            let pieceIndex = this.board[pieceY][pieceX];

            // can't move an empty tile
            if(pieceIndex === 0) return false;

            // get the piece information
            let piece = this.pieces[Math.abs(pieceIndex)];

            // for each move of this piece
            for(let move of piece.moves){

                // add dx, dy to determine new tile position for this move
                let newPieceX = pieceX + move.dx;
                let newPieceY = pieceY + move.dy;

                // go to next move if this move isn't on board
                if(!this.coordsInBoard(newPieceX, newPieceY)) continue;
                
                // get info on piece that (may) occupy the desired tile
                let pieceOnCheckedTile = this.board[newPieceY][newPieceX];

                // if a one-off move (pawn, king, knight)
                if(move.type === 0){
                    if(newPieceX === newX && newPieceY === newY && !this.piecesOnSameTeam(pieceIndex, pieceOnCheckedTile)) 
                        return true;
                }

                // if a rule-like move (bishop, queen, rook)
                else if(move.type === 1){
                    let multiplier = 1;
                    do {
                        pieceOnCheckedTile = this.board[newPieceY][newPieceX];
                        // will have to change when considering friendly capture gamemodes
                        if(newPieceX === newX && newPieceY === newY && !this.piecesOnSameTeam(pieceIndex, pieceOnCheckedTile)) return true;
                        else if(pieceOnCheckedTile != 0) break; // very sneaky :)

                        // calculate next tile along formulaic path 
                        multiplier++;
                        newPieceX = pieceX + (move.dx * multiplier);
                        newPieceY = pieceY + (move.dy * multiplier);
                    } while(this.coordsInBoard(newPieceX, newPieceY));
                }
            }
            // if you get here, the piece cannot move to the targeted tile
            // all above "return true" will have to instead set a flag to indicate if 
            // move should be simulated or not, as checking if a piece's moveset allows
            // it to move to a tile doesn't mean moving to that tile is valid within 
            // the scope of the game (i.e. move a piece that was pinned to a king in regular rules)

            // simulate move
            // if game over rules hold
            return false;
        },

        // will have to modify to account for > 2 player games
        // as this relies on player 1 pieces being positive and player 2 pieces being negative
        piecesOnSameTeam(piece1, piece2){
            return (piece1 > 0 && piece2 > 0) || (piece1 < 0 && piece2 < 0);
        }
    }

    return obj;
};

console.log("Loaded game!");
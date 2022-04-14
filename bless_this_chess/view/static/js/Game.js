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
        coordsInBoard(x,y){ 
            return 0 <= x && x < this.dimensions.width && 0 <= y && y < this.dimensions.height
        },

        isValidMove(pieceX, pieceY, newX, newY){
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

                // if a one-off move (pawn, king, knight)
                if(move.type == 0) {
                    if(newPieceX == newX && newPieceY == newY){
                        return true;
                    }
                }
                // if a rule-like move (bishop, queen, rook)
                else if(move.type == 1){
                    let multiplier = 1;

                    // move along the formulaic path described by this move rule until you're off the board
                    // checking if the path lands on the selected tile
                    while(this.coordsInBoard(newPieceX, newPieceY)){
                        if(newPieceX == newX && newPieceY == newY)
                            return true;
                        else {
                            multiplier++;
                            newPieceX = pieceX + (move.dx * multiplier);
                            newPieceY = pieceY + (move.dy * multiplier);
                        }
                    }
                }
            }
            // if you get here, the piece cannot move to the targeted tile

            // simulate move
            // if game over rules hold
            return false;
        }
    }
    return obj;
};

console.log("Loaded game!");
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
                moves: [],
            },
            {
                name: "rook",
                moves: [],
            },
            {
                name: "knight",
                moves: [],
            },
            {
                name: "bishop",
                moves: [],
            },
            {
                name: "queen",
                moves: [],
            },
            {
                name: "king",
                moves: [],
            },
        ],

    }
    return obj;
};

console.log("Loaded game!");
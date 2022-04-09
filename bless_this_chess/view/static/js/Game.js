Game = () => {
    let obj = {};
    obj = {
        players: 2,
        dimensions: {
            width: 8,
            height: 8,
        },
        playerTurn: 1,
        board: [
            [-2,-3,-4,-5,-6,-4,-3,-2],
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 1, 1, 1, 1, 1, 1, 1, 1],
            [ 2, 3, 4, 5, 6, 4, 3, 2]
        ],
        primaryTileColor: "white",
        secondaryTileColor: "black",
        winRules: {},
        drawRules: {},
        pieces: [
            {}, // :)
            {
                name: "pawn",
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
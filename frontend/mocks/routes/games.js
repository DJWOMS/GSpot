// Use this file only as a guide for first steps using routes. Delete it when you have added your own route files.
// For a detailed explanation regarding each routes property, visit:
// https://mocks-server.org/docs/usage/routes

const GAMES = [
    {
        id: 1,
        title: 'Test game',
        description: 'Lorem ipsum...',
        price: 100,
    },
    {
        id: 2,
        title: 'TestGame2',
        description: 'Lorem impsum...2',
        price: 200,
    },
]

module.exports = [
    {
        id: 'get-list-games', // route id
        url: '/api/games/list', // url in express format
        method: 'GET', // HTTP method
        variants: [
            {
                id: 'success', // variant id
                type: 'json', // variant handler id
                options: {
                    status: 200, // status to send
                    body: GAMES, // body to send
                },
            },
            {
                id: 'error', // variant id
                type: 'json', // variant handler id
                options: {
                    status: 400, // status to send
                    // body to send
                    body: {
                        message: 'Error',
                    },
                },
            },
        ],
    },
    {
        id: 'get-game-by-id',
        url: '/api/games/:id',
        method: 'GET',
        variants: [
            {
                id: 'success',
                type: 'json',
                options: {
                    status: 200,
                    body: GAMES[0],
                },
            },
            {
                id: 'not-found',
                type: 'json',
                options: {
                    status: 404,
                    body: {
                        message: 'Not Found',
                    },
                },
            },
        ],
    },
]

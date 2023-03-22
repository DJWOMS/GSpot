const GAMES = [
    {
        id: '8d7d3d19-8c68-4225-8e63-10acb3a34a90',
        title: 'Test game 1',
        releaseDate: '2023-03-19',
        genres: [
            {
                id: '8d7d3d19-8c68-4225-8e63-frff25f424r',
                name: 'Приключения',
            },
            {
                id: '8d7d3d19-8c68-4225-8e63-542624fr42f',
                name: 'Экшн',
            },
        ],
        platforms: [
            {
                id: '8d7d3d19-43cv-4225-8e63-frff25f424r',
                name: 'Windows',
                icon: 'win',
            },
        ],
        price: 100,
        discount: 5,
        is_bought: false,
        is_favorite: false,
    },
    {
        id: '8d7d3d19-8c68-4225-34df-10acb3a34a90',
        title: 'Test game 2',
        releaseDate: '2023-02-10',
        genres: [
            {
                id: '8d7d3d19-8c68-4225-8e63-45vvfv65324',
                name: 'MMO',
            },
        ],
        platforms: [
            {
                id: '8d7d3d19-54gg-4225-8e63-frff25f424r',
                name: 'Linux',
                icon: 'linux',
            },
        ],
        price: 100,
        discount: 5,
        is_bought: false,
        is_favorite: false,
    },
    {
        id: '8d7d3d19-8c68-4225-34fs-10acb3a34a90',
        title: 'Test game 3',
        releaseDate: '2023-03-10',
        genres: [
            {
                id: '8d7d3d19-8c68-4225-8e63-45vvfv65324',
                name: 'MMO',
            },
        ],
        platforms: [
            {
                id: '8d7d3d19-54gg-4225-8e63-frff25f424r',
                name: 'Windows',
                icon: 'win',
            },
        ],
        price: 100,
        discount: 5,
        is_bought: false,
        is_favorite: false,
    },
]

const GAME_DETAIL = {
    id: '8d7d3d19-8c68-4225-8e63-10acb3a34a90',
    title: 'Test game 1',
    releaseDate: '2023-03-19',
    genres: [
        {
            id: '8d7d3d19-8c68-4225-8e63-frff25f424r',
            name: 'Приключения',
        },
        {
            id: '8d7d3d19-8c68-4225-8e63-542624fr42f',
            name: 'Экшн',
        },
    ],
    platforms: [
        {
            id: '8d7d3d19-43cv-4225-8e63-frff25f424r',
            name: 'Windows',
            icon: 'win',
        },
    ],
    price: 100,
    discount: 5,
    is_bought: false,
    is_favorite: false,
    name: 'Game1',
    release_date: '2023-03-19',
    description: '1',
    about: '1',
    age: null,
    adult: '',
    status: 'M',
    type: 'G',
    developersUuid: '7e8a503e-bf96-11ed-afa1-0242ac120002',
    publishersUuid: '7e8a503e-bf96-11ed-afa1-0242ac120002',
    dlcs: [
        {
            id: '73db9198-2523-4f02-ad4e-43f5a8606f76',
            name: 'Dlc1',
            description: 'dlc1',
            developersUuid: '7e8a503e-bf96-11ed-afa1-0242ac120002',
            publishersUuid: '7e8a503e-bf96-11ed-afa1-0242ac120002',
            langs: [
                {
                    id: 4,
                    language_name: 'Russian',
                    interface: true,
                    subtitles: true,
                    voice: true,
                },
            ],
        },
    ],
    langs: [
        {
            id: 2,
            language_name: 'English',
            interface: true,
            subtitles: true,
            voice: true,
        },
    ],
    systemRequirements: [
        {
            id: 'f45a2256-970d-4df8-a255-ac55a7834500',
            operatingSystem: 'W',
            deviceProcessor: '12',
            deviceMemory: '12',
            deviceStorage: '12',
            deviceGraphics: '12',
            typeRequirements: 'M',
        },
    ],
}

module.exports = [
    {
        id: 'get-list-games', // route id
        url: '/api/games/', // url in express format
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
                    body: GAME_DETAIL,
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

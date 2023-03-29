const BESTGAMES = [
  {
    title: 'Elden Ring',
    link: '/',
    coverImg: 'https://picsum.photos/240/240',
    price: 60.0,
    platforms: ['win', 'ps', 'xbox'],
  },
  {
    title: 'World of Warcraft',
    link: '/',
    coverImg: 'https://picsum.photos/240/240',
    price: 39.99,
    sale: 19.99,
    platforms: ['ap', 'win'],
  },
  {
    title: 'Half Life 2',
    link: '/',
    coverImg: 'https://picsum.photos/240/240',
    price: 28.0,
    sale: 15.0,
    platforms: ['xbox', 'ap', 'win'],
  },
  {
    title: 'Resident Evil 2',
    link: '/',
    coverImg: 'https://picsum.photos/240/240',
    price: 58.49,
    platforms: ['xbox'],
  },
  {
    title: "Sid Meier's Civilization VI ",
    link: '/',
    coverImg: 'https://picsum.photos/240/240',
    price: 49.99,
    platforms: ['xbox', 'ap'],
  },
]

module.exports = [
  {
    id: 'best-games',
    url: '/api/best-games',
    method: 'GET',
    variants: [
      {
        id: 'success',
        type: 'json',
        options: {
          status: 200,
          body: BESTGAMES,
        },
      },
      {
        id: 'error',
        type: 'json',
        options: {
          status: 400,
          body: {
            message: 'Error',
          },
        },
      },
    ],
  },
]

const BESTGAMES = [
  {
    title: 'Elden Ring',
    link: '/',
    coverImg: '',
    price: 60.0,
    available: ['win', 'ps', 'xbox'],
  },
  {
    title: 'World of Warcraft',
    link: '/',
    coverImg: '',
    price: 39.99,
    sale: 19.99,
    available: ['ap', 'win'],
  },
  {
    title: 'Half Life 2',
    link: '/',
    coverImg: '',
    price: 28.0,
    sale: 15.0,
    available: ['xbox', 'ap', 'win'],
  },
  {
    title: 'Resident Evil 2',
    link: '/',
    coverImg: '',
    price: 58.49,
    available: ['xbox'],
  },
  {
    title: "Sid Meier's Civilization VI ",
    link: '/',
    coverImg: '',
    price: 49.99,
    available: ['xbox', 'ap'],
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

const LatestGameMockState = [
  { title: 'Desperados III Digital De', link: '/', coverImg: '', price: 49.0, badge: 'New', platform: ['ps', 'xbox', 'ap'] },
  { title: 'Red Dead Redemptio', link: '/', coverImg: '', price: 19.99, sale: 12.0, badge: 'Pre-order', platform: ['ap', 'win'] },
  { title: 'Dandara: Trials of Fear Editi', link: '/', coverImg: '', price: 18.0, sale: 12.0, badge: 'New', platform: ['xbox', 'ap'] },
  { title: 'Druidstone: The Secret of t', link: '/', coverImg: '', price: 58.49, sale: 20.0, platform: ['xbox'] },
  { title: "Baldur's Gate II: Enhanced ", link: '/', coverImg: '', price: 38.99, platform: ['xbox', 'ap'] },
  { title: "Baldur's Gate: Enhanced", link: '/', coverImg: '', price: 9.99, platform: ['xbox', 'ps'] },
  { title: 'SteamWorld Quest: Hand ', link: '/', coverImg: '', price: 12.49, badge: 'Pre-order', platform: ['xbox', 'win'] },
]

module.exports = [
  {
    id: 'latest-games',
    url: '/api/latest-games',
    method: 'GET',
    variants: [
      {
        id: 'success',
        type: 'json',
        options: {
          status: 200,
          body: LatestGameMockState,
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

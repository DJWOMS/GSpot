const NEWS = [
  {
    id: '8d7d3d19-8c68-4225-ht56-10acb3a34a90',
    category: {
      id: '8d7d3d19-8c68-4225-ht56-10acb3a34a90',
      name: 'Игровые',
    },
    name: 'Тестовая новость 1',
    date: '2023-01-01',
    image: 'https://picsum.photos/240/240',
  },
  {
    id: '8d7d3d19-463g-4225-ht56-10acb3a34a90',
    category: {
      id: '8d7d3d19-2dft-4225-ht56-10acb3a34a90',
      name: 'Интервью',
    },
    name: 'Тестовая новость 2',
    date: '2023-01-05',
    image: 'https://picsum.photos/240/240',
  },
]

module.exports = [
  {
    id: 'get-list-news',
    url: '/api/news/',
    method: 'GET',
    variants: [
      {
        id: 'success',
        type: 'json',
        options: {
          status: 200,
          body: NEWS,
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
  {
    id: 'get-news-by-id',
    url: '/api/news/:id',
    method: 'GET',
    variants: [
      {
        id: 'success',
        type: 'json',
        options: {
          status: 200,
          body: NEWS[0],
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

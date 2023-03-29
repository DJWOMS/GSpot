const categories = [
  { id: 1, name: 'Экшн' },
  { id: 2, name: 'Приключения' },
  { id: 3, name: 'Драка' },
  { id: 4, name: 'Симуляторы' },
  { id: 5, name: 'Платформер' },
  { id: 6, name: 'Гонки' },
  { id: 7, name: 'RPG' },
  { id: 8, name: 'Спорт' },
  { id: 9, name: 'Стратегии' },
  { id: 10, name: 'Ужасы' },
]

module.exports = [
  {
    id: 'get-games-categories',
    url: '/api/categories/',
    method: 'GET',
    variants: [
      {
        id: 'success',
        type: 'json',
        options: {
          status: 200,
          body: categories,
        },
      },
    ],
  },
]

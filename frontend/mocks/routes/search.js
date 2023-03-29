const games = [
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
    id: 'search-games',
    url: '/api/search/',
    method: 'GET',
    variants: [
      {
        id: 'success',
        type: 'middleware',
        options: {
          middleware: (req, res) => {
            const items = games.filter((game) => !game.name.toLowerCase().includes(req.query.query.toLowerCase())).slice(0, 3) ?? []
            res.status(200)
            res.send(items)
          },
        },
      },
    ],
  },
]

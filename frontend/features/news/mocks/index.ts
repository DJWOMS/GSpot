import randomItem from 'utils/randomItem'
import randomNum from 'utils/randomNumber'
import type { INews } from '../models'

export const generateMockNewsCard = (props = {}): INews => ({
  id: randomNum(10).toString(),
  category: {
    id: randomNum(10).toString(),
    name: randomItem(['Новость', 'Событие', 'Обзор']),
  },
  name: randomItem([
    'Новая игра',
    'Новая новость',
    'Новостной день новостей',
    'Собрание геймеров в Центре Москвы',
  ]),
  date: new Date(new Date().getUTCDate() - randomNum(3)),
  image: `https://loremflickr.com/640/480/abstract?lock=${randomNum(4)}`,
  ...props,
})

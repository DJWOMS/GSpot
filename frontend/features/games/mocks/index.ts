import { faker } from '@faker-js/faker'
import { GameCardInterface } from 'features/games'

const generateMockGameCard = (props = {}): GameCardInterface => ({
  title: faker.word.adjective(),
  link: '/',
  coverImg: faker.image.abstract(),
  price: faker.datatype.number(1000),
  sale: faker.datatype.number(500),
  currency: 'RUB',
  ...props,
})

export { generateMockGameCard }

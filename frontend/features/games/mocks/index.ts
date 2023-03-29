import { faker } from '@faker-js/faker'
import { GameCardInterface, GameCardSimpleInterface } from 'features/games'

const generateMockGameCardSimple = (props = {}): GameCardSimpleInterface => ({
  title: faker.word.adjective(),
  link: faker.internet.url(),
  ...props,
})

const generateMockGameCard = (props = {}): GameCardInterface => ({
  coverImg: faker.image.abstract(),
  price: faker.datatype.number(1000),
  sale: faker.datatype.number(500),
  currency: 'RUB',
  ...generateMockGameCardSimple(props),
})

export { generateMockGameCard, generateMockGameCardSimple }

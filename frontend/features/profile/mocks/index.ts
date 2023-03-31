import { faker } from '@faker-js/faker'
import { GameCardInterface } from 'features/games'

const generateMockGameCard = (props = {}): GameCardInterface => ({
  title: faker.name.fullName(),
  link: '#',
  coverImg: faker.image.abstract(),
  price: faker.datatype.number(10),
  sale: faker.datatype.number(50),
  currency: 'RUB',
})

export { generateMockGameCard }

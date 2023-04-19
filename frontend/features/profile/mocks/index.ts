import { faker } from '@faker-js/faker'
import { GameCardInterface, generateMockGameCard } from 'features/games'
import { PurchaseCardInterface, CheckoutGameCardInterface } from '../types'

export const generateMockPurchaseCard = (props = {}): PurchaseCardInterface => ({
  id: faker.datatype.number({ min: 0, max: 100 }),
  title: faker.word.adjective(),
  price: faker.datatype.number(),
  status: 'confirmed',
  coverImg: faker.image.abstract(240, 340),
  platform: {
    type: 'win',
  },
  date: 'Aug 22, 2021',
  currency: 'rub',
  link: faker.internet.url(),
})

export const generateMockCheckoutGameCard = (props = {}): CheckoutGameCardInterface => ({
  id: faker.datatype.number(),
  title: faker.word.adjective(),
  coverImg: faker.image.abstract(240, 240),
  platform: {
    type: 'win',
  },
  link: faker.internet.url(),
  price: faker.datatype.number(),
  currency: 'rub',
  ...props,
})

export const generateMockFavoriteGameCard = (props = {}): GameCardInterface => ({
  ...generateMockGameCard(props),
})

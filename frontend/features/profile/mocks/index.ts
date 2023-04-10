import { faker } from '@faker-js/faker'
import { CheckoutGameCardInterface } from '../types'

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

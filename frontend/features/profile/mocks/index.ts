import { faker } from '@faker-js/faker'
import { PurchaseCardInterface } from '../types'

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
  ...props,
})

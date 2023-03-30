import { faker } from '@faker-js/faker'
import { INews } from 'features/news'

const generateMockNewsCard = (props = {}): INews => ({
  id: faker.datatype.uuid(),
  category: {
    id: faker.datatype.uuid(),
    name: faker.word.adjective(),
  },
  name: faker.word.adjective(),
  date: faker.datatype.datetime(),
  image: faker.image.abstract(),
  ...props,
})

export { generateMockNewsCard }

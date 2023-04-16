import { faker } from '@faker-js/faker'
import { ContactsFormInterface } from '../types'

export const generateMockContactsForm = (props = {}): ContactsFormInterface => ({
  name: faker.word.adjective(),
  email: faker.internet.email(),
  subject: faker.lorem.text(),
  message: faker.lorem.text(),
  ...props,
})

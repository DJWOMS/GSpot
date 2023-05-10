import { faker } from '@faker-js/faker'
import type {
  GameCardInterface,
  GameCardSimpleInterface,
  GameDetailsInterface,
  GameListInterface,
} from '../types'

export const generateMockGameCardSimple = (props = {}): GameCardSimpleInterface => ({
  title: faker.word.adjective(),
  link: faker.internet.url(),
  ...props,
})

export const generateMockGameList = (props = {}): GameListInterface => ({
  coverImg: faker.image.imageUrl(240, 340, 'pc-games', true),
  price: faker.datatype.number(1000),
  sale: faker.datatype.number(500),
  currency: 'RUB',
  ...generateMockGameCardSimple(props),
})

export const generateMockGameCard = (props = {}): GameCardInterface => ({
  badge: 'New',
  platforms: [{ type: 'ap' }, { type: 'win' }],
  ...generateMockGameList(props),
})

export const generateRequirement = (props = {}) => ({
  operatingSystem: faker.word.adjective(),
  deviceProcessor: faker.lorem.paragraph(),
  deviceMemory: faker.lorem.paragraph(),
  deviceStorage: faker.lorem.paragraph(),
  deviceGraphics: faker.lorem.paragraph(),
  typeRequirements: faker.lorem.paragraph(),
  ...props,
})

export const generateMockGameDetails = (props = {}): GameDetailsInterface => ({
  description: faker.lorem.paragraphs(5),
  languages: [
    {
      languageName: 'English',
      interfaces: true,
      subtitles: false,
      voice: false,
    },
  ],
  requirements: [
    generateRequirement({ operatingSystem: 'Windows', typeRequirements: 'Minimal' }),
    generateRequirement({ operatingSystem: 'Linux', typeRequirements: 'Minimal' }),
    generateRequirement({ operatingSystem: 'Apple', typeRequirements: 'Minimal' }),
  ],
  age: 'adult',
  ...generateMockGameCard(props),
})

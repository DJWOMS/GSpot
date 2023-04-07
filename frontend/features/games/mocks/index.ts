import { faker } from '@faker-js/faker'
import { GameCardInterface, GameCardSimpleInterface, GameDetailsInterface, GameListInterface } from 'features/games'

const generateMockGameCardSimple = (props = {}): GameCardSimpleInterface => ({
  title: faker.word.adjective(),
  link: faker.internet.url(),
  ...props,
})

const generateMockGameList = (props = {}): GameListInterface => ({
  coverImg: faker.image.abstract(),
  price: faker.datatype.number(1000),
  sale: faker.datatype.number(500),
  currency: 'RUB',
  ...generateMockGameCardSimple(props),
})
const generateMockGameCard = (props = {}): GameCardInterface => ({
  ...generateMockGameList(props),
})

const generateRequirement = (props = {}) => ({
  operatingSystem: faker.word.adjective(),
  deviceProcessor: faker.lorem.paragraph(),
  deviceMemory: faker.lorem.paragraph(),
  deviceStorage: faker.lorem.paragraph(),
  deviceGraphics: faker.lorem.paragraph(),
  typeRequirements: faker.lorem.paragraph(),
  ...props,
})
const generateMockGameDetails = (props = {}): GameDetailsInterface => ({
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
  ...generateMockGameCard(props),
})

export { generateMockGameCard, generateMockGameCardSimple, generateMockGameDetails, generateMockGameList }

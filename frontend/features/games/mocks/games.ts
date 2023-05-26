import randomItem from 'utils/randomItem'
import randomNum from 'utils/randomNumber'
import type {
  GameCardInterface,
  GameCardSimpleInterface,
  GameDetailsInterface,
  GameListInterface,
} from '../types'

export const generateMockGameCardSimple = (props = {}): GameCardSimpleInterface => ({
  title: 'little',
  link: '/details/id',
  ...props,
})

export const generateMockGameList = (props = {}): GameListInterface => ({
  coverImg: `https://loremflickr.com/240/340/pc-games?lock=${randomNum(5)}`,
  price: randomNum(3),
  sale: randomNum(3),
  currency: 'RUB',
  ...generateMockGameCardSimple(props),
})

export const generateMockGameCard = (props = {}): GameCardInterface => ({
  badge: 'New',
  platforms: [{ type: 'ap' }, { type: 'win' }],
  ...generateMockGameList(props),
})

export const generateRequirement = (props = {}) => ({
  operatingSystem: randomItem(['Windows', 'Linux', 'MacOS']),
  deviceProcessor: randomItem(['Intel', 'AMD']),
  deviceMemory: randomItem(['4GB', '8GB', '12GB', '16GB']),
  deviceStorage: randomItem(['8GB', '10GB', '12GB', '14GB', '16GB', '20GB', '40GB', '60GB']),
  deviceGraphics: randomItem(['NVIDIA 1080', 'NVIDIA Titan X', 'AMD Radeon 5215']),
  typeRequirements: randomItem(['Minimal', 'Recommend']),
  ...props,
})

export const generateMockGameDetails = (props = {}): GameDetailsInterface => ({
  description: 'Some description for game',
  languages: [
    {
      languageName: 'English',
      interfaces: true,
      subtitles: true,
      voice: false,
    },
    {
      languageName: 'Russian',
      interfaces: true,
      subtitles: false,
      voice: false,
    },
    {
      languageName: 'German',
      interfaces: true,
      subtitles: false,
      voice: true,
    },
    {
      languageName: 'Spanish',
      interfaces: true,
      subtitles: true,
      voice: false,
    },
    {
      languageName: 'Italian',
      interfaces: true,
      subtitles: false,
      voice: false,
    },
    {
      languageName: 'Chinese',
      interfaces: true,
      subtitles: false,
      voice: true,
    },
    {
      languageName: 'Belarusian',
      interfaces: true,
      subtitles: false,
      voice: false,
    },
    {
      languageName: 'Turkey',
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

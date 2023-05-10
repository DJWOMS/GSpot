import { faker } from '@faker-js/faker'
import type {
  FilterGenreInterface,
  FilterSubgenreType,
  FilterPlatformInterface,
  FilterPriceType,
  FilterSortByInterface,
} from '../types'

/**
 * SortBy mocks
 */
export const generateMockFilterSortBy = (props = {}): FilterSortByInterface => ({
  id: faker.datatype.number({ min: 0, max: 10 }),
  name: faker.word.adjective(),
  ...props,
})

/**
 * Prices mocks
 */
export const generateMockFilterPrice = (): FilterPriceType => [
  faker.datatype.number({ min: 1000, max: 5000 }),
  faker.datatype.number({ min: 10000, max: 50000 }),
]

/**
 * Platforms mocks
 */
export const generateMockFilterPlatform = (props = {}): FilterPlatformInterface => ({
  id: faker.datatype.number({ min: 0, max: 10 }),
  name: faker.word.adjective(),
  ...props,
})

/**
 * Genres mocks
 */
export const generateMockFilterSubgenre = (props = {}): FilterSubgenreType => ({
  id: faker.datatype.number({ min: 0, max: 10 }),
  name: faker.word.adjective(),
  ...props,
})

export const generateMockFilterGenre = (props = {}): FilterGenreInterface => ({
  ...generateMockFilterSubgenre(),
  subgenres: [...new Array(3)].map(() => generateMockFilterSubgenre()),
  ...props,
})

import randomItem from 'utils/randomItem'
import randomNum from 'utils/randomNumber'
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
  id: randomNum(3),
  name: randomItem(['Price', 'Date', 'Hot']),
  ...props,
})

/**
 * Prices mocks
 */
export const generateMockFilterPrice = (): FilterPriceType => [randomNum(4), randomNum(5)]

/**
 * Platforms mocks
 */
export const generateMockFilterPlatform = (props = {}): FilterPlatformInterface => ({
  id: randomNum(3),
  name: randomItem(['Requirements', 'RAM', 'ROM', 'CPU', 'Video card']),
  ...props,
})

/**
 * Genres mocks
 */
export const generateMockFilterSubgenre = (props = {}): FilterSubgenreType => ({
  id: randomNum(3),
  name: randomItem(['RPG', 'Action', 'MMO', 'Horror', 'Adventure']),
  ...props,
})

export const generateMockFilterGenre = (props = {}): FilterGenreInterface => ({
  ...generateMockFilterSubgenre(),
  subgenres: [...new Array(3)].map(() => generateMockFilterSubgenre()),
  ...props,
})

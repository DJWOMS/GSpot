/**
 * SortBy interface
 */
export interface FilterSortByInterface {
  id: number
  name: string
}

/**
 * Prices type
 */
export type FilterPriceType = number[]

/**
 * Platforms interface
 */
export interface FilterPlatformInterface {
  id: number
  name: string
}

/**
 * Genres interfaces & types
 */
interface FilterBaseGenreInterface {
  id: number
  name: string
}

export type FilterSubgenreType = FilterBaseGenreInterface

export interface FilterGenreInterface extends FilterBaseGenreInterface {
  subgenres: FilterSubgenreType[]
}

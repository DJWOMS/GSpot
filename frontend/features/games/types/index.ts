export interface GameCardSimpleInterface {
  title: string
  link: string
}

export interface GameCardInterface extends GameCardSimpleInterface {
  coverImg: string
  price: number
  sale?: number
  badge?: 'New' | 'Pre-order'
  platform?: Array<PlatformType>
  currency?: 'RUB' | 'USD' | 'EUR'
}
export type GameDetailsInterface = GameCardInterface

export interface PlatformType {
  type: 'ps' | 'xbox' | 'win' | 'ap'
}

export interface RequirementListType {
  [key: string]: string
}

export interface RequirementType {
  title: string
  list: RequirementListType
}

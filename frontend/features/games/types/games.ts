export interface GameCardSimpleInterface {
  title: string
  link: string
}

export interface GameListInterface extends GameCardSimpleInterface {
  coverImg: string
  price: number
  sale?: number
  currency?: 'RUB' | 'USD' | 'EUR'
}

export interface GameCardInterface extends GameListInterface {
  badge?: 'New' | 'Pre-order'
  platforms: PlatformType[]
}

export interface GameDetailsInterface extends GameCardInterface {
  description: string
  languages: LanguageInterface[]
  requirements: RequirementInterface[]
  age: string
}

export interface LanguageInterface {
  languageName: string
  interfaces: boolean
  subtitles: boolean
  voice: boolean
}

export interface RequirementInterface {
  operatingSystem: string
  deviceProcessor: string
  deviceMemory: string
  deviceStorage: string
  deviceGraphics: string
  typeRequirements: string
}

export interface PlatformType {
  type: 'ps' | 'xbox' | 'win' | 'ap'
}

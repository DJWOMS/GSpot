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

export interface GameDetailsInterface extends GameCardInterface {
  description: string
  languages: LanguageInterface[]
  requirements: RequirementInterface[]
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
export interface GamingCards {
  coverImg: string
  title: string
  price: number
  sale?: number
}

export interface PlatformType {
  type: 'ps' | 'xbox' | 'win' | 'ap'
}

import { UUID, DATE } from '@defaultTypes'

export interface IProductGenre {
  id: UUID
  name: string
}

export interface IProduct {
  id: UUID
  name: string
  releaseDate: DATE
  genres: IProductGenre[]
  systemRequirements: {
    id: UUID
    operatingSystem: string
  }[]
  price: number
  discount?: number
  isBought: boolean
  isFavorite: boolean
}

export interface IProductLang {
  id: UUID
  languageName: string
  interface: boolean
  subtitles: boolean
  voice: boolean
}

export interface IProductDlc {
  id: UUID
  name: string
  description: string
  developersUuid: UUID
  publishersUuid: UUID
  langs: IProductLang[]
}

export interface IProductSystemRequirement {
  id: UUID
  operatingSystem: string
  deviceProcessor: string
  deviceMemory: string
  deviceStorage: string
  deviceGraphics: string
  typeRequirements: string
}

export interface IProductDetail extends IProduct {
  description: string
  about: string
  age: number | null
  adult: string
  status: string
  type: string
  developersUuid: UUID
  publishersUuid: UUID
  dlcs: IProductDlc[]
  langs: IProductLang[]
  systemRequirements: IProductSystemRequirement[]
}

import { URL, UUID, DATE } from '@defaultTypes'

export interface IProductGenre {
    id: UUID
    name: string
}

export interface IProductPlatform {
    id: UUID
    name: string
    icon: URL
}

export interface IProduct {
    id: UUID
    name: string
    releaseDate: DATE
    genres: IProductGenre[]
    platforms: IProductPlatform[]
    price: number
    discount?: number
    is_bought: boolean
    is_favorite: boolean
}

export interface GameCardInterface {
    title: string
    link: string
    coverImg: string
    price: number
    sale?: number
    badge?: 'New' | 'Pre-order'
    avalible?: Array<PlatformType>
    currency?: 'RUB' | 'USD' | 'EUR'
}

export interface PlatformType {
    type: 'ps' | 'xbox' | 'win' | 'ap'
}

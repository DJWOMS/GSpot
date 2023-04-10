import { PlatformType } from 'features/games'

export interface CheckoutGameCardInterface {
  id: number
  title: string
  coverImg: string
  link: string
  platform: PlatformType
  price: number
  currency: string
}

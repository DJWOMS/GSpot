import { PlatformType } from 'features/games'

export interface PurchaseCardInterface {
  id: number
  coverImg: string
  title: string
  platform: PlatformType
  date: string
  price: number
  status: 'confirmed' | 'canceled' | 'not confirmed'
  link: string
  currency: string
}

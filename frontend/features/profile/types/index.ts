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

export interface CheckoutGameCardInterface {
  id: number
  title: string
  coverImg: string
  link: string
  platform: PlatformType
  price: number
  currency: string
}

export interface UserDataInterface {
  nickname: string
  email: string
  firstName: string
  lastName: string
}
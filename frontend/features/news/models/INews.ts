import { UUID } from '@defaultTypes'
import { INewsCategory } from './INewsCategory'

export interface INews {
  id: UUID
  category: INewsCategory
  name: string
  date: Date
  image: string
}

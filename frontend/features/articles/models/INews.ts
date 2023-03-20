import { UUID } from '@defaultTypes'

import INewsCategory from './INewsCategory'

export default interface INews {
    id: UUID
    category: INewsCategory
    name: string
    timestamp: number
    image: URL
}

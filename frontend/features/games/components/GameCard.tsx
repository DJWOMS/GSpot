import Card from 'components/Card'
import { FC } from 'react'

interface Props {
    badge?: string
    title: string
    link: string
    price: number
    sale?: number
}

const GameCard: FC<Props> = ({ badge, title, link, price, sale }) => {
    const rand = () => {
        return Math.floor(Math.random() * (1000 - 900 + 1) + 900)
    }

    return <Card title={title} link={link} price={price} coverImg={`https://picsum.photos/${rand()}`} badge={badge} sale={sale} />
}

export default GameCard

import Card from 'components/Card'
import { FC } from 'react'
import { GameCardInterface } from '../types'

const GameCard: FC<GameCardInterface> = ({ badge, title, link, price, sale, avalible }): JSX.Element => {
    const rand = () => {
        return Math.floor(Math.random() * (1000 - 900 + 1) + 900)
    }

    return <Card avalible={avalible} title={title} link={link} price={price} coverImg={`https://picsum.photos/${rand()}`} badge={badge} sale={sale} />
}

export { GameCard }

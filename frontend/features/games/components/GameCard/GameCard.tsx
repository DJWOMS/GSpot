import { FC } from 'react'
import Card from 'components/Card'
import { GameCardInterface } from 'features/games'

const GameCard: FC<GameCardInterface> = ({ badge, title, link, price, coverImg, sale, platform }) => {
  return <Card platform={platform} title={title} link={link} price={price} coverImg={coverImg} badge={badge} sale={sale} />
}

export { GameCard }

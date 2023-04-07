import { FC } from 'react'
import { GameCardInterface } from 'features/games/types'
import { ListGame } from './ListGame'
import s from './ListGames.module.scss'

interface ListGamesProps {
  children: GameCardInterface[]
}

export const ListGames: FC<ListGamesProps> = ({ children }) => {
  return (
    <div className={s.list}>
      {children.map((game, index) => (
        <ListGame key={index} {...game} />
      ))}
    </div>
  )
}

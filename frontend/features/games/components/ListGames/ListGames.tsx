import { FC } from 'react'
import type { GameListInterface } from '../../types'
import { ListGame } from './ListGame'
import s from './ListGames.module.css'

interface ListGamesProps {
  children: GameListInterface[]
}

const ListGames: FC<ListGamesProps> = ({ children }) => {
  return (
    <div className={s.list}>
      {children.map((game, index) => (
        <ListGame key={index} {...game} />
      ))}
    </div>
  )
}

export default ListGames

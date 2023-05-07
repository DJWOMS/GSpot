import { FC } from 'react'
import { GameListInterface } from 'features/games'
import { ListGame } from './ListGame'
import s from './ListGames.module.css'

interface ListGamesProps {
  children: GameListInterface[]
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

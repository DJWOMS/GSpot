import { FC } from 'react'
import { RandomGameInterface } from 'features/games'
import { RandomGame } from '../RandomGame/RandomGame'
import s from './RandomGamesList.module.scss'

type RandomGameListType = {
  children: RandomGameInterface[]
}

const RandomGamesList: FC<RandomGameListType> = ({ children }) => {
  return (
    <ul className={s.list}>
      {' '}
      {children.map((card, index) => (
        <RandomGame key={index} {...card} />
      ))}{' '}
    </ul>
  )
}

export { RandomGamesList }

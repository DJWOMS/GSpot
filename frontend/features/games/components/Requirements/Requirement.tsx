import { FC } from 'react'
import { RequirementType } from 'features/games/types'
import s from './Requirement.module.scss'

const Requirement: FC<RequirementType> = ({ title, list }) => {
  return (
    <div>
      <span className={s.title}>{title}:</span>
      <ul className={s.list}>
        {Object.entries(list).map(([key, value]) => (
          <li key={key}>
            <span>{key}:</span> {value}
          </li>
        ))}
      </ul>
    </div>
  )
}

export { Requirement }

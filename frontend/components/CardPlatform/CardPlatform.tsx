import { FC } from 'react'
import { PlatformType } from 'features/games'
import s from './CardPlatform.module.scss'
import cn from 'classnames'

const CardPlatform: FC<PlatformType> = ({ type }): JSX.Element => {
  return <div className={cn(s.platform, s[type])} />
}

export default CardPlatform

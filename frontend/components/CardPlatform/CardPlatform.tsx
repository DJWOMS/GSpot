import { FC } from 'react'
import cn from 'classnames'
import { PlatformType } from 'features/games'
import s from './CardPlatform.module.scss'

const CardPlatform: FC<PlatformType> = ({ type }): JSX.Element => {
  return <div className={cn(s.platform, s[type])} />
}

export default CardPlatform

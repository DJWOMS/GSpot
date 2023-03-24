import { FC } from 'react'
import s from './CardPlatform.module.scss'
import cn from 'classnames'
import { PlatformType } from 'features/games/types'

const CardPlatform: FC<PlatformType> = ({ type }): JSX.Element => {
  return <div className={cn(s.platform, s[type])} />
}

export default CardPlatform

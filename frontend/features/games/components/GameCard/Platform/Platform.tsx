import { FC } from 'react'
import cn from 'classnames'
import { PlatformType } from 'features/games'
import s from './Platform.module.scss'

const Platform: FC<PlatformType> = ({ type }): JSX.Element => {
  return <div className={cn(s.platform, s[type])} />
}

export { Platform }

import { FC } from 'react'
import s from './CardPlatform.module.scss'
import cn from 'classnames'

interface Props {
  type: 'ps' | 'xbox' | 'win' | 'ap'
}

const CardPlatform: FC<Props> = ({ type }) => {
  return <div className={cn(s.platform, s[type])} />
}

export default CardPlatform

'use client'

import { FC } from 'react'
import { IconHeart, IconTrash } from '@tabler/icons-react'
import cn from 'classnames'
import Image from 'next/image'
import Link from 'next/link'
import type { GameCardInterface } from '../../types'
import Platform from '../Platform'
import s from './GameCard.module.css'

interface GameCardProps extends GameCardInterface {
  onDelete?: () => void
}
const GameCard: FC<GameCardProps> = ({
  badge,
  title,
  link,
  price,
  coverImg,
  sale,
  platforms,
  currency,
  onDelete,
}) => {
  return (
    <div className={s.card}>
      <Link className={s.cardCover} href="/details/id">
        <Image src={coverImg} width={240} height={340} alt="" />
        {badge && <span className={cn(s.cardBadge, s.cardBadgeNew)}>{badge}</span>}
      </Link>

      <ul className={s.cardPlatforms}>
        {platforms.map((platform, id: number) => (
          <Platform key={id} {...platform} />
        ))}
      </ul>

      <div className={s.cardTitle}>
        <h3>
          <Link href={link}>{title}</Link>
        </h3>

        <span>
          {currency}
          {sale ? sale : price}
          {sale && (
            <s>
              {currency}
              {price}
            </s>
          )}
        </span>
      </div>

      <div className={s.cardActions}>
        <div className={cn(s.cardAction, s.cardActionBuy)}>Купить</div>
        <div className={cn(s.cardAction, s.cardActionFavorite)}>
          {onDelete ? <IconTrash onClick={onDelete} /> : <IconHeart />}
        </div>
      </div>
    </div>
  )
}

export default GameCard

'use client'

import { FC, useTransition } from 'react'
import { IconHeart } from '@tabler/icons-react'
import { IconTrash } from '@tabler/icons-react'
import cn from 'classnames'
import { GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'
import Image from 'next/image'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import s from './GameCard.module.scss'
import { Platform } from './Platform'

const GameCard: FC<GameCardInterface & { favorite?: boolean }> = ({ badge, title, link, price, coverImg, sale, platforms, currency, favorite }) => {
  const [isPending, startTransition] = useTransition()
  const router = useRouter()
  const onActionButtonClickHandler = async () => {
    if (favorite) {
      await fetchServerSide({
        method: 'DELETE',
        path: '/profile/favorites',
      })
    }
    startTransition(() => {
      router.refresh()
    })
  }
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
        <div className={cn(s.cardAction, s.cardActionFavorite)} onClick={onActionButtonClickHandler}>
          {favorite ? <IconTrash /> : <IconHeart />}
        </div>
      </div>
    </div>
  )
}

export { GameCard }

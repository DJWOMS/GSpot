import { FC } from 'react'
import { IconHeart } from '@tabler/icons-react'
import cn from 'classnames'
import { GameCardInterface } from 'features/games'
import Image from 'next/image'
import Link from 'next/link'
import s from './GameCard.module.scss'
import { Platform } from './Platform'

const GameCard: FC<GameCardInterface> = ({ badge, title, link, price, coverImg, sale, platform, currency }) => {
  return (
    <div className={s.card}>
      <Link className={s.cardCover} href="/#">
        <Image src={coverImg} width={400} height={600} alt="" />
        {badge && <span className={cn(s.cardBadge, s.cardBadgeNew)}>{badge}</span>}
      </Link>

      <ul className={s.cardPlatforms}>
        {platform?.map((i, id: number) => (
          <Platform key={id} type={i.type} />
        ))}
      </ul>

      <div className={s.cardTitleWrapper}>
        <h3 className={s.cardTitle}>
          <Link className={s.cardTitleLink} href={link}>
            {title}
          </Link>
        </h3>

        <div className={s.cardPrice}>
          {currency}
          {sale ? sale : price}
          {sale && (
            <s>
              {currency}
              {price}
            </s>
          )}
        </div>
      </div>

      <div className={s.cardActions}>
        <div className={cn(s.cardAction, s.cardActionBuy)}>Купить</div>

        <div className={cn(s.cardAction, s.cardActionFavorite)}>
          <IconHeart />
        </div>
      </div>
    </div>
  )
}

export { GameCard }

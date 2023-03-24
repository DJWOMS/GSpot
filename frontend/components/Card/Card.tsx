import Link from 'next/link'
import { IconHeart } from '@tabler/icons-react'
import s from './Card.module.scss'
import { FC } from 'react'
import cn from 'classnames'
import CardPlatform from '../CardPlatform'
import { GameCardInterface } from 'features/games'

const Card: FC<GameCardInterface> = ({ title, link, coverImg, price, sale, available, badge, currency = '$' }) => {
  return (
    <div className={s.card}>
      <Link className={s.cardCover} href="/#">
        <img src={coverImg} alt="" />
        {badge && <span className={cn(s.cardBadge, s.cardBadgeNew)}>{badge}</span>}
      </Link>

      <ul className={s.cardPlatforms}>
        {available?.map((i, id: number) => (
          <CardPlatform key={id} type={i.type} />
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

export default Card

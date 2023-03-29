import { FC } from 'react'
import { IconHeart } from '@tabler/icons-react'
import cn from 'classnames'
import CardPlatform from 'components/CardPlatform'
import { GameCardInterface } from 'features/games'
import Image from 'next/image'
import Link from 'next/link'
import s from '../Card/Card.module.scss'

const CardBig: FC<GameCardInterface> = ({ coverImg, badge, link, title, sale, price, platform, currency = '$' }) => {
  return (
    <div className={s.cardBig}>
      <Link className={s.cardCover} href="/#">
        <Image src={coverImg} alt="" width={400} height={600} />
        {badge && <span className={s.cardBadgeNew}>{badge}</span>}
      </Link>

      <div className={s.cardWrapper}>
        <h3 className={s.cardTitle}>
          <Link className={s.cardTitleLink} href={link}>
            {title}
          </Link>
        </h3>

        <ul className={s.cardPlatforms}>
          {platform?.map((i, id) => (
            <CardPlatform key={id} type={i.type} />
          ))}
        </ul>

        <div className={s.cardPrice}>
          {sale ? [currency, sale] : [currency, price]}
          {sale && <s>{[currency, price]}</s>}
        </div>

        <div className={s.cardActions}>
          <div className={cn(s.cardAction, s.cardActionBuy)}>Купить</div>

          <div className={cn(s.cardAction, s.cardActionFavorite)}>
            <IconHeart />
          </div>
        </div>
      </div>
    </div>
  )
}

export default CardBig

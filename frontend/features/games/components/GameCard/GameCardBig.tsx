import { FC } from 'react'
import { IconHeart } from '@tabler/icons-react'
import cn from 'classnames'
import Image from 'next/image'
import Link from 'next/link'
import type { GameCardInterface } from '../../types'
import Platform from '../Platform'
import s from './GameCard.module.css'

const GameCardBig: FC<GameCardInterface> = ({
  coverImg,
  link,
  title,
  sale,
  price,
  platforms,
  currency = '$',
}) => {
  return (
    <div className={cn(s.card, s.cardBig)}>
      <Link className={s.cardCover} href="/details/id">
        <Image src={coverImg} alt="" width={240} height={340} />
      </Link>

      <div className={s.cardWrap}>
        <div className={s.cardTitle}>
          <h3>
            <Link href={link}>{title}</Link>
          </h3>
        </div>

        <ul className={s.cardList}>
          <li>
            <span>Release date:</span> 30.11.2018
          </li>
          <li>
            <span>Genres:</span> Simulation, Action, Sci-fi
          </li>
        </ul>

        <ul className={s.cardPlatforms}>
          {platforms.map((platform, id) => (
            <Platform key={id} {...platform} />
          ))}
        </ul>

        <div className={s.cardPrice}>
          <span>{sale ? [currency, sale] : [currency, price]}</span>
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

export { GameCardBig }

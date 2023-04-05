import { FC } from 'react'
import { GameCardInterface } from 'features/games/types'
import Image from 'next/image'
import Link from 'next/link'
import s from './CheckoutGameCard.module.scss'

const CheckoutGameCard: FC<GameCardInterface> = ({ title, coverImg, price, link, currency, sale }, id) => {
  return (
    <div className="container">
      <div className={s.card}>
        <div className={s.cardCover} key={id}>
          <div className="justify-normal flex">
            <input className="mr-2" type="checkbox" />
            <Link href="/details/id">
              <Image src={coverImg} width={50} height={50} alt="" />
            </Link>
            <h3>
              <Link href={link}>{title}</Link>
            </h3>
          </div>

          <div>
            {currency}
            {sale ? sale : price}
            {sale && (
              <s className={s.cardSale}>
                {currency}
                {price}
              </s>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export { CheckoutGameCard }

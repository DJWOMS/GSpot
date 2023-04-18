import { FC } from 'react'
import { IconX } from '@tabler/icons-react'
import { CheckoutGameCardInterface } from 'features/profile'
import Image from 'next/image'
import Link from 'next/link'
import s from './CheckoutGameCard.module.scss'

const CheckoutGameCard: FC<CheckoutGameCardInterface> = ({ title, link, currency, price, coverImg }) => {
  return (
    <tr>
      <td>
        <div className={s.cardImg}>
          <Image src={coverImg} width={240} height={340} alt="img" />
        </div>
      </td>
      <td>
        <Link href={link}>{title}</Link>
      </td>
      <td>PC</td>
      <td>
        <span className={s.cardPrice}>
          {currency}
          {price}
        </span>
      </td>
      <td>
        <button className={s.cardDelete} type="button">
          <IconX />
        </button>
      </td>
    </tr>
  )
}

export { CheckoutGameCard }

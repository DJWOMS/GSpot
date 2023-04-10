import { FC } from 'react'
import { IconX } from '@tabler/icons-react'
import { GameCardInterface } from 'features/games'
import Image from 'next/image'
import Link from 'next/link'
import s from './Purchase.module.scss'

const Purchase: FC<GameCardInterface> = ({ title, link, coverImg, price, currency }) => {
  return (
    <tr className={s.purchase}>
      <td>
        <Link href={link}>8420</Link>
      </td>
      <td>
        <div className={s.purchaseImage}>
          <Image src={coverImg} width={240} height={340} alt="image" />
        </div>
      </td>
      <td>{title}</td>
      <td>XBOX</td>
      <td>Aug 22, 2021</td>
      <td>
        <span className={s.purchasePrice}>
          {currency}
          {price}
        </span>
      </td>
      <td>
        <span className={s.purchaseStatus}>Not confirmed</span>
      </td>
      <td>
        <button className={s.purchaseDelete}>
          <IconX strokeWidth={0.3} />
        </button>
      </td>
    </tr>
  )
}

export { Purchase }

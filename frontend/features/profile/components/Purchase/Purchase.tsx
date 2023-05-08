import { FC } from 'react'
import { IconX } from '@tabler/icons-react'
import { PurchaseCardInterface } from 'features/profile'
import Image from 'next/image'
import Link from 'next/link'
import s from './Purchase.module.css'

const Purchase: FC<PurchaseCardInterface> = ({ id, title, link, platform, date, coverImg, price, status, currency }) => {
  return (
    <tr className={s.purchase}>
      <td>
        <Link href={link}>{id}</Link>
      </td>
      <td>
        <div className={s.purchaseImage}>
          <Image src={coverImg} width={240} height={340} alt="image" />
        </div>
      </td>
      <td>{title}</td>
      <td>{platform.type}</td>
      <td>{date}</td>
      <td>
        <span className={s.purchasePrice}>
          {currency}
          {price}
        </span>
      </td>
      <td>
        <span className={s.purchaseStatus}>{status}</span>
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

import { FC } from 'react'
import { IconX } from '@tabler/icons-react'
import { GameCardInterface } from 'features/games'
import Link from 'next/link'
import s from './Purchase.module.scss'

const Purchase: FC<GameCardInterface> = ({ title, link, coverImg, price, sale, currency }) => {
  return (
    <tr className={s.wrapper}>
      <td>
        <Link href="#modal-info" className={s.openModal}>
          8420
        </Link>
      </td>
      <td>
        <div className={s.profileImg}>
          <img src={coverImg} alt="image" style={{ height: '120px' }} />
        </div>
      </td>
      <td>{title}</td>
      <td>XBOX</td>
      <td>Aug 22, 2021</td>
      <td>
        <span className={s.profilePrice}>${price}</span>
      </td>
      <td>
        <span className={s.profileStatus}>Not confirmed</span>
      </td>
      <td>
        <button className={s.profileDelete}>
          <IconX strokeWidth={0.3} />
        </button>
      </td>
    </tr>
  )
}

export { Purchase }

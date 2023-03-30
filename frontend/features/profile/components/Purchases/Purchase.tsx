import { IconX } from '@tabler/icons-react'
import Link from 'next/link'
import s from './Purchase.module.scss'

const ProfileItem = () => {
  const rand = () => {
    return Math.floor(Math.random() * (1000 - 900 + 1) + 900)
  }
  return (
    <tr className={s.wrapper}>
      <td>
        <Link href="#modal-info" className={s.openModal}>
          8451
        </Link>
      </td>
      <td>
        <div className={s.profileImg}>
          <img src={`https://picsum.photos/${rand()}`} alt="image" style={{ height: '120px' }} />
        </div>
      </td>
      <td>Desperados III Digital Deluxe Edition</td>
      <td>XBOX</td>
      <td>Aug 22, 2021</td>
      <td>
        <span className={s.profilePrice}>$49.00</span>
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

export default ProfileItem

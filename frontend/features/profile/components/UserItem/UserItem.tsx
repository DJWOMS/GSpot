import React, { FC } from 'react'
import { IconUser } from '@tabler/icons-react'
import Image from 'next/image'
import { UserPublicDataInterface } from '../../types'
import s from './UserItem.module.css'

const UserItem: FC<UserPublicDataInterface> = ({ username, avatar, is_active, country }) => {
  return (
    <div className={s.user}>
      <div className={s.userAvatar}>
        {avatar ? <Image src={avatar} alt={'avatar'} /> : <IconUser color="white" />}
      </div>
      <div className={s.userDescr}>
        <p className={s.userDescrName}>{username}</p>
        <div className={s.userStatuse}>
          Статус:
          {is_active ? <span> Активен</span> : <span>Заблокирован</span>}
        </div>
        <div className={s.userCountry}>
          Страна:
          {country}
        </div>
      </div>
    </div>
  )
}

export default UserItem

import { FC } from 'react'
import { IconUser, IconDoorExit } from '@tabler/icons-react'
import Section from 'components/Section'
import Link from 'next/link'
import s from './layout.module.css'

interface ProfileProps {
  children: React.ReactNode
}

const Profile: FC<ProfileProps> = ({ children }) => {
  return (
    <div>
      <Section title="Профиль" />

      <Section last>
        <div className={s.profile}>
          <div className={s.profileUser}>
            <div className={s.profileAvatar}>
              <IconUser color="white" />
            </div>

            <div className={s.profileMeta}>
              <h3>Джо Роджер</h3>
              <span>GSpot ID: 00319</span>
            </div>
          </div>

          <ul className={s.profileTabs}>
            <li className="nav-item">
              <Link className={s.active} href="/profile/purchases">
                Мои покупки
              </Link>
            </li>

            <li className="nav-item">
              <Link href="/profile/settings">Настройки</Link>
            </li>
          </ul>

          <button className={s.profileLogout} type="button">
            <IconDoorExit />
            <span>Выйти</span>
          </button>
        </div>

        {children}
      </Section>
    </div>
  )
}

export default Profile

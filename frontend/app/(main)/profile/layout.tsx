import { FC } from 'react'
import { IconUser, IconHome2, IconArrowNarrowRight, IconDoorExit } from '@tabler/icons-react'
import cn from 'classnames'
import Link from 'next/link'
import s from './layout.module.scss'

const Profile: FC<any> = ({ children }) => {
  return (
    <div>
      <section className={s.section}>
        <h2 className={s.sectionTitle}>Профиль</h2>
      </section>
      <section className={s.section}>
        <div className="container">
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
                <Link className="nav-link active" href="/profile/purchases">
                  Мои покупки
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" href="/profile/settings">
                  Настройки
                </Link>
              </li>
            </ul>

            <button className={s.profileLogout} type="button">
              <IconDoorExit />
              <span>Выйти</span>
            </button>
          </div>
        </div>
        {children}
      </section>
    </div>
  )
}

export default Profile

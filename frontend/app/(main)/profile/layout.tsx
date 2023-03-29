import { FC } from 'react'
import Link from 'next/link'

import s from './layout.module.scss'
import cn from 'classnames'
import { IconUser, IconHome2, IconArrowNarrowRight, IconDoorExit } from '@tabler/icons-react'

const Profile: FC<any> = ({ children }) => {
  return (
    <div>
      <section className={s.section}>
        <div className="container">
          <div className={s.sectionWrap}>
            <h2 className={s.sectionTitle}>Профиль</h2>
            <ul className={s.breadcrumb}>
              <li className={s.breadcrumbItem}>
                <IconHome2 color="#a782e9" />
                <Link href="#">Домой</Link>
              </li>
              <li className={cn(s.breadcrumbItem, s.breadcrumbItemActive)}>
                <IconArrowNarrowRight color="#a782e9" />
                Профиль
              </li>
            </ul>
          </div>
        </div>
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

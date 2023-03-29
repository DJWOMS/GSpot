import { FC } from 'react'
import Link from 'next/link'
import Image from 'next/image'

import s from './profile.module.scss'
import cn from 'classnames'

import UserSVG from 'assets/img/user.svg'
import HomeSVG from 'assets/img/home.svg'
import breadcrumbSVG from 'assets/img/breadcrumb.svg'

const Profile: FC<any> = ({ children }) => {
  return (
    <div>
      <section className={s.section}>
        <div className="container">
          <div className="row">
            <div className="col-12">
              <div className={s.section__wrap}>
                <h2 className={s.section__title}>Профиль</h2>
                <ul className={s.breadcrumb}>
                  <li className={s.breadcrumb__item}>
                    <Image src={HomeSVG} alt="Home" className={s.breadcrumb__item_img} />
                    <a href="#">Домой</a>
                  </li>
                  <li className={cn(s.breadcrumb__item, s.breadcrumb__item_active)}>
                    <Image src={breadcrumbSVG} alt="Home" className={s.breadcrumb__item_img} />
                    Профиль
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section className={s.section}>
        <div className="container">
          <div className="row">
            <div className="col-12">
              <div className={s.profile}>
                <div className={s.profile__user}>
                  <div className={s.profile__avatar}>
                    <Image src={UserSVG} alt="User" />
                  </div>
                  <div className={s.profile__meta}>
                    <h3>Джо Роджер</h3>
                    <span>GSpot ID: 00319</span>
                  </div>
                </div>

                <ul className={s.profile__tabs} id="profile__tabs" role="tablist">
                  <li className="nav-item">
                    <Link
                      className="nav-link active"
                      data-toggle="tab"
                      href="/profile/purchases"
                      role="tab"
                      aria-controls="tab-1"
                      aria-selected="true"
                    >
                      Мои покупки
                    </Link>
                  </li>
                  <li className="nav-item">
                    <Link className="nav-link" data-toggle="tab" href="/profile/settings" role="tab" aria-controls="tab-2" aria-selected="false">
                      Настройки
                    </Link>
                  </li>
                </ul>

                <button className={s.profile__logout} type="button">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                    <path
                      d="M304 336v40a40 40 0 01-40 40H104a40 40 0 01-40-40V136a40 40 0 0140-40h152c22.09 0 48 17.91 48 40v40M368 336l80-80-80-80M176 256h256"
                      fill="none"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="32"
                    />
                  </svg>
                  <span>Выйти</span>
                </button>
              </div>
            </div>
          </div>
        </div>
        <div className="container">
          <div className="tab-content">
            <div className="tab-pane fade show active" id="tab-1" role="tabpanel">
              <div className="row">{children}</div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default Profile

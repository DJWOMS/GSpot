'use client'

import { FC, useEffect, useState } from 'react'
import { IconHeart, IconSearch, IconShoppingCart } from '@tabler/icons-react'
import LogoPNG from 'assets/img/logo.png'
import cn from 'classnames'
import Image from 'next/image'
import Link from 'next/link'
import s from './Header.module.scss'

type HeaderLink = {
  href: string
  title: string
}
interface HeaderProps {
  links: HeaderLink[]
}

const Header: FC<HeaderProps> = ({ links }) => {
  const [hideHeader, setHideHeader] = useState(false)
  const [scrolling, setScrolling] = useState(false)
  const [previousTop, setPreviousTop] = useState(0)
  const [currentTop, setCurrentTop] = useState(0)
  const scrollDelta = 10
  const scrollOffset = 140

  useEffect(() => {
    const handleScroll = () => {
      if (!scrolling) {
        setScrolling(true)
        !window.requestAnimationFrame ? setTimeout(autoHideHeader, 250) : requestAnimationFrame(autoHideHeader)
      }
    }

    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [scrolling])

  useEffect(() => {
    if (previousTop - currentTop > scrollDelta) {
      setHideHeader(false)
    } else if (currentTop - previousTop > scrollDelta && currentTop > scrollOffset) {
      setHideHeader(true)
    }

    setPreviousTop(currentTop)
    setScrolling(false)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [currentTop])

  function autoHideHeader() {
    setCurrentTop(window.scrollY)
  }

  const [openHeader, setOpenHeader] = useState(false)
  const toggleOpen = () => setOpenHeader((state) => !state)

  useEffect(() => {
    window.onscroll = () => (openHeader ? window.scrollTo(window.scrollX, window.scrollY) : () => void 0)
  }, [openHeader])

  return (
    <header className={cn(s.header, { [s.headerHide]: hideHeader })}>
      <div className={s.wrapper}>
        <div className={s.content}>
          <button className={cn(s.menu, { [s.menuOpen]: openHeader })} onClick={toggleOpen}>
            <span></span>
            <span></span>
            <span></span>
          </button>

          <Link className={s.logo} href="/">
            <Image src={LogoPNG} alt="Logo" loading="eager" />
          </Link>

          <ul className={cn(s.nav, { [s.navOpen]: openHeader })}>
            {links.map(({ href, title }, index) => (
              <li className={s.navItem} onClick={() => setOpenHeader(false)} key={index}>
                <Link className={s.navLink} href={href}>
                  {title}
                </Link>
              </li>
            ))}
          </ul>

          <div className={s.actions}>
            <span />
            <a className={s.loginBtn} href="/signin">
              <span>Авторизация</span>
            </a>
          </div>
        </div>
      </div>

      <div className={s.wrapper}>
        <div className={s.content}>
          <form className={s.form}>
            <input className={s.input} type="text" placeholder="Я ищу..." />
            <select className={s.select}>
              <option value="0">Все категории</option>
              <option value="1">Экшн</option>
              <option value="3">Приключения</option>
              <option value="4">Драка</option>
              <option value="5">Симуляторы</option>
              <option value="6">Платформер</option>
              <option value="7">Гонки</option>
              <option value="8">RPG</option>
              <option value="9">Спорт</option>
              <option value="10">Стратегии</option>
              <option value="11">Ужасы</option>
            </select>
            <button className={s.searchBtn}>
              <IconSearch />
            </button>
          </form>

          <div className={s.actions}>
            <Link className={s.actionLink} href="/favorite">
              <IconHeart />
              <span>Favorites</span>
            </Link>

            <Link className={s.actionLink} href="/cart">
              <IconShoppingCart />
              <span>$00.00</span>
            </Link>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header

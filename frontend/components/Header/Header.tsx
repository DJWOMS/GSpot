'use client'

import { FC, useEffect, useState } from 'react'
import { IconHeart, IconShoppingCart } from '@tabler/icons-react'
import LogoPNG from 'assets/img/logo.png'
import cn from 'classnames'
import { Container } from 'components/Container'
import Image from 'next/image'
import Link from 'next/link'
import Search from '../Search/Search'
import s from './Header.module.scss'

type HeaderLink = {
  href: string
  title: string
}
interface HeaderProps {
  links: HeaderLink[]
}

const scrollDelta = 10
const scrollOffset = 140

const Header: FC<HeaderProps> = ({ links }) => {
  const [hideHeader, setHideHeader] = useState(false)
  const [, setScrolling] = useState(false)
  const [, setPreviousTop] = useState(0)
  const [currentTop, setCurrentTop] = useState(0)

  useEffect(() => {
    const handleScroll = () => {
      setScrolling((prev) => {
        if (!prev) {
          !window.requestAnimationFrame ? setTimeout(autoHideHeader, 250) : requestAnimationFrame(autoHideHeader)
          return true
        }
        return prev
      })
    }

    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  useEffect(() => {
    setPreviousTop((prev) => {
      if (prev - currentTop > scrollDelta) {
        setHideHeader(false)
      } else if (currentTop - prev > scrollDelta && currentTop > scrollOffset) {
        setHideHeader(true)
      }
      return currentTop
    })
    setScrolling(false)
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
        <Container>
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
              <a className={s.loginBtn} href="/contacts">
                <span>contacts</span>
              </a>
            </div>
          </div>
        </Container>
      </div>

      <div className={s.wrapper}>
        <Container>
          <div className={s.content}>
            <Search />

            <div className={s.actions}>
              <Link className={s.actionLink} href="/favorite">
                <IconHeart />
                <span>Favorites</span>
              </Link>

              <Link className={s.actionLink} href="/checkout">
                <IconShoppingCart />
                <span>$00.00</span>
              </Link>
            </div>
          </div>
        </Container>
      </div>
    </header>
  )
}

export default Header

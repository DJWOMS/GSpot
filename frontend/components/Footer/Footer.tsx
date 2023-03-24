import Link from 'next/link'
import Image from 'next/image'
import {
  IconTriangleSquareCircle,
  IconDeviceGamepad2,
  IconBuildingSkyscraper,
  IconBrandFacebook,
  IconBrandInstagram,
  IconBrandTwitter,
  IconBrandVk,
  IconBrandTwitch,
} from '@tabler/icons-react'
import s from './Footer.module.scss'
import LogoPNG from 'assets/img/logo.png'
import cn from 'classnames'

const Footer = () => {
  return (
    <footer className={s.footer}>
      <div className={s.container}>
        <div className={s.navList}>
          <div className={cn(s.nav, s.nav1)}>
            <div className={s.title}>
              <IconTriangleSquareCircle />
              <span>GSpot Info</span>
            </div>
            <nav className={s.list}>
              <a href="#About">О нас</a>
              <a href="#Catalog">Каталог</a>
              <a href="#News">Новости</a>
              <a href="#FAQ">Центр помощи</a>
              <a href="#Contacts">Контакты</a>
            </nav>
          </div>

          <div className={cn(s.nav, s.nav2)}>
            <div className={s.title}>
              <IconDeviceGamepad2 />
              <span>Game</span>
            </div>
            <nav className={cn(s.list, s.listDouble)}>
              <a href="#dota2">Dota 2</a>
              <a href="#pubg">Pubg</a>
              <a href="#COD">Call of Duty</a>
              <a href="#CS">CS:GO</a>
              <a href="#Mine">Minecraft</a>
            </nav>
            <nav className={cn(s.list, s.listDouble)}>
              <a href="#Portal2">Portal 2</a>
              <a href="#GOW">God Of War</a>
              <a href="#NFS">Need For Speed</a>
              <a href="#Metro">Metro Exodus</a>
              <a href="#Fortnite">Fortnite</a>
            </nav>
          </div>

          <div className={cn(s.nav, s.nav3)}>
            <div className={s.title}>
              <IconBuildingSkyscraper />
              <span>For partners</span>
            </div>

            <nav className={s.list}>
              <a href="#">Партнерская программа</a>
              <a href="#">Продажа</a>
              <a href="#">Условия и положени</a>
              <a href="#">Политика </a>
              <a href="#">Партнерство</a>
            </nav>

            <div className={s.contacts}>
              <Link className={s.footerLink} href="#">
                +3 301 234-52-48
              </Link>
              <Link className={s.footerLink} href="#">
                support@gmail.com
              </Link>
              <div className={s.social}>
                <a href="#">
                  <IconBrandFacebook />
                </a>
                <a href="#">
                  <IconBrandInstagram />
                </a>
                <a href="#">
                  <IconBrandTwitter />
                </a>
                <a href="#">
                  <IconBrandVk />
                </a>
                <a href="#">
                  <IconBrandTwitch />
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className={cn(s.container, s.wrapper)}>
        <Link className={s.logo} href="/">
          <Image src={LogoPNG} alt="Logo" loading="eager" />
        </Link>
        <span>
          © GSpot, 2020—2021
          <br /> Create by <a href="">GSpot Team</a>
        </span>
      </div>
    </footer>
  )
}

export default Footer

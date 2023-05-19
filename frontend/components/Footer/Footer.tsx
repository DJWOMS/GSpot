import {
  IconTriangleSquareCircle,
  IconDeviceGamepad2,
  IconBuildingSkyscraper,
  IconBrandFacebook,
  IconBrandInstagram,
  IconBrandTwitter,
  IconBrandVk,
  IconBrandTwitch,
  IconChevronRight,
} from '@tabler/icons-react'
import LogoPNG from 'assets/img/logo.png'
import cn from 'classnames'
import Container from 'components/Container'
import Image from 'next/image'
import Link from 'next/link'
import s from './Footer.module.css'

const Footer = () => {
  return (
    <footer className={s.footer}>
      <Container>
        <div className={s.navList}>
          <div className={cn(s.nav, s.nav1)}>
            <div className={s.title}>
              <IconTriangleSquareCircle />
              <span>GSpot Info</span>
            </div>
            <nav className={s.list}>
              <a href="#About">
                <IconChevronRight color="#a782e9" size={20} />О нас
              </a>
              <a href="#Catalog">
                <IconChevronRight color="#a782e9" size={20} />
                Каталог
              </a>
              <a href="#News">
                <IconChevronRight color="#a782e9" size={20} />
                Новости
              </a>
              <a href="#FAQ">
                <IconChevronRight color="#a782e9" size={20} />
                Центр помощи
              </a>
              <Link href="/contacts">
                <IconChevronRight color="#a782e9" size={20} />
                Контакты
              </Link>
            </nav>
          </div>

          <div className={cn(s.nav, s.nav2)}>
            <div className={s.title}>
              <IconDeviceGamepad2 />
              <span>Game</span>
            </div>
            <nav className={cn(s.list, s.listDouble)}>
              <a href="#dota2">
                <IconChevronRight color="#a782e9" size={20} />
                Dota 2
              </a>
              <a href="#pubg">
                <IconChevronRight color="#a782e9" size={20} />
                Pubg
              </a>
              <a href="#COD">
                <IconChevronRight color="#a782e9" size={20} />
                Call of Duty
              </a>
              <a href="#CS">
                <IconChevronRight color="#a782e9" size={20} />
                CS:GO
              </a>
              <a href="#Mine">
                <IconChevronRight color="#a782e9" size={20} />
                Minecraft
              </a>
            </nav>
            <nav className={cn(s.list, s.listDouble)}>
              <a href="#Portal2">
                <IconChevronRight color="#a782e9" size={20} />
                Portal 2
              </a>
              <a href="#GOW">
                <IconChevronRight color="#a782e9" size={20} />
                God Of War
              </a>
              <a href="#NFS">
                <IconChevronRight color="#a782e9" size={20} />
                Need For Speed
              </a>
              <a href="#Metro">
                <IconChevronRight color="#a782e9" size={20} />
                Metro Exodus
              </a>
              <a href="#Fortnite">
                <IconChevronRight color="#a782e9" size={20} />
                Fortnite
              </a>
            </nav>
          </div>

          <div className={cn(s.nav, s.nav3)}>
            <div className={s.title}>
              <IconBuildingSkyscraper />
              <span>For partners</span>
            </div>

            <nav className={s.list}>
              <a href="#">
                <IconChevronRight color="#a782e9" size={20} />
                Партнерская программа
              </a>
              <a href="#">
                <IconChevronRight color="#a782e9" size={20} />
                Продажа
              </a>
              <a href="#">
                <IconChevronRight color="#a782e9" size={20} />
                Условия и положения
              </a>
              <a href="#">
                <IconChevronRight color="#a782e9" size={20} />
                Политика{' '}
              </a>
              <a href="#">
                <IconChevronRight color="#a782e9" size={20} />
                Партнерство
              </a>
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

        <div className={s.wrapper}>
          <Link className={s.logo} href="/">
            <Image src={LogoPNG} width={496} height={161} alt="Logo" loading="eager" />
          </Link>
          <span>
            © GSpot, 2020—2021
            <br /> Create by <a href="">GSpot Team</a>
          </span>
        </div>
      </Container>
    </footer>
  )
}

export default Footer

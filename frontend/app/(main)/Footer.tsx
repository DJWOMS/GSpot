'use client'

import Link from 'next/link'
import Image from 'next/image'
import styled from 'styled-components'
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
import LogoPNG from '@/assets/img/logo.png'

const StyledFooter = styled.footer`
    position: relative;
    display: block;
    width: 100%;
    height: auto;
    border-top: 1px solid rgba(167, 130, 233, 0.06);
    padding-top: 60px;
    @media (min-width: 1200px) {
        padding-top: 90px;
    }
    @media (min-width: 768px) .footer {
        padding-top: 80px;
    }
    @media (min-width: 576px) .footer {
        padding-top: 70px;
    }
`
const Container = styled.div`
    @media (min-width: 576px) {
        max-width: 540px;
    }
    @media (min-width: 768px) {
        max-width: 720px;
    }
    @media (min-width: 992px) {
        max-width: 960px;
    }
    @media (min-width: 1200px) {
        max-width: 1140px;
    }
    @media (min-width: 1310px) {
        max-width: 1310px;
    }

    width: 100%;
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto;
    margin: auto;
`
const Navs = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;

    @media (min-width: 768px) {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-start;
        flex-wrap: wrap;
        padding: 0 1vw;
    }
`
const Nav = styled.div`
    @media (min-width: 1200px) {
        margin-bottom: 0;
    }
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    flex-wrap: wrap;
    margin-bottom: 40px;
    position: relative;
    width: 100%;
`
const Nav1 = styled(Nav)`
    @media (min-width: 768px) {
        width: calc(33.333333% - 15px);
    }
    @media (min-width: 1200px) {
        width: calc(20% - 20px);
    }
`
const Nav2 = styled(Nav)`
    @media (min-width: 768px) {
        width: calc(66.666666% - 15px);
    }
    @media (min-width: 1200px) {
        width: calc(40% - 20px);
    }
    @media (max-width: 768px) {
        flex-direction: column;
    }
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    flex-wrap: wrap;
`
const Nav3 = styled(Nav)`
    @media (max-width: 768px) {
        flex-direction: column;
    }

    @media (min-width: 768px) {
        width: 100%;
    }
    @media (min-width: 1200px) {
        width: calc(40% - 20px);
    }
`

const Title = styled.div`
    svg {
        position: relative;
        z-index: 2;
        stroke: #a782e9;
        // fill: #a782e9;
        width: 22px;
        height: auto;
        background-color: #1b222e;
    }
    span {
        position: relative;
        z-index: 2;
        display: block;
        background-color: #1b222e;
        padding: 0 10px;
        font-size: 16px;
        color: #fff;
        letter-spacing: 0.4px;
    }
    :before {
        content: '';
        position: absolute;
        display: block;
        left: 0;
        right: 0;
        top: 50%;
        height: 1px;
        background-color: rgba(167, 130, 233, 0.06);
        z-index: 1;
    }
    position: relative;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
`
const List = styled.nav`
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;

    a {
        font-size: 14px;
        color: #dbdada;
        line-height: 26px;
        position: relative;
        padding-left: 20px;
        letter-spacing: 0.4px;
        opacity: 0.8;
        :hover {
            opacity: 1;
        }
        :before {
            content: '';
            position: absolute;
            display: block;
            top: 0;
            bottom: 0;
            left: 0;
            width: 10px;
            background: url('/svg/arrow.svg') no-repeat left center;
            background-size: 10px auto;
            opacity: 0.5;
            transition: 0.5s;
        }
    }
`
const List_double = styled(List)`
    @media (max-width: 768px) {
        :last-child {
            margin-top: 0;
        }
    }
    @media (min-width: 768px) {
        width: 50%;
    }
`

const Contacts = styled.div`
    margin-top: 40px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;

    @media (min-width: 768px) {
        position: absolute;
        bottom: 0;
        right: 0;
        margin-top: 0;
        align-items: flex-end;
    }
`

const FooterLink = styled(Link)`
    font-size: 16px;
    line-height: 30px;
    color: #fff;

    :hover {
        color: #a782e9;
    }
`
const Social = styled.div`
    margin-top: 40px;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    a {
        margin-right: 20px;
        width: 20px;
        height: 24px;
        color: white;
    }
    a:last-child {
        margin-right: 0;
    }
    a:hover {
        color: #a782e9;
    }
`
const Wrap = styled(Container)`
    @media (min-width: 576px) {
        margin-top: 70px;
    }
    @media (min-width: 768px) {
        margin-top: 80px;
    }
    @media (min-width: 1200px) {
        margin-top: 90px;
    }
    border-top: 1px solid rgba(167, 130, 233, 0.06);
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    height: 90px;
    width: 100%;
    margin-top: 60px;
    a {
        width: 130px;
        height: auto;
    }
    span {
        a {
            color: #dbdada;
        }
        a:hover {
            color: #a782e9;
        }
        font-size: 12px;
        line-height: 20px;
        color: #dbdada;
        text-align: right;
    }
`

const Logo = styled(Link)`
    display: block;
    width: 120px;
    height: auto;
    img {
        width: 100%;
        height: 100%;
    }
`

export function Footer() {
    return (
        <StyledFooter>
            <Container>
                <Navs>
                    <Nav1>
                        <Title>
                            <IconTriangleSquareCircle />
                            <span>GSpot Info</span>
                        </Title>
                        <List>
                            <a href="#About">О нас</a>
                            <a href="#Catalog">Каталог</a>
                            <a href="#News">Новости</a>
                            <a href="#FAQ">Центр помощи</a>
                            <a href="#Contacts">Контакты</a>
                        </List>
                    </Nav1>

                    <Nav2>
                        <Title>
                            <IconDeviceGamepad2 />
                            <span>Game</span>
                        </Title>
                        <List_double>
                            <a href="#dota2">Dota 2</a>
                            <a href="#pubg">Pubg</a>
                            <a href="#COD">Call of Duty</a>
                            <a href="#CS">CS:GO</a>
                            <a href="#Mine">Minecraft</a>
                        </List_double>
                        <List_double>
                            <a href="#Portal2">Portal 2</a>
                            <a href="#GOW">God Of War</a>
                            <a href="#NFS">Need For Speed</a>
                            <a href="#Metro">Metro Exodus</a>
                            <a href="#Fortnite">Fortnite</a>
                        </List_double>
                    </Nav2>

                    <Nav3>
                        <Title>
                            <IconBuildingSkyscraper />
                            <span>For partners</span>
                        </Title>

                        <List>
                            <a href="#">Партнерская программа</a>
                            <a href="#">Продажа</a>
                            <a href="#">Условия и положени</a>
                            <a href="#">Политика </a>
                            <a href="#">Партнерство</a>
                        </List>

                        <Contacts>
                            <FooterLink href="tel:">+3 301 234-52-48</FooterLink>
                            <FooterLink href="mail:">support@gmail.com</FooterLink>
                            <Social>
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
                            </Social>
                        </Contacts>
                    </Nav3>
                </Navs>
            </Container>

            <Wrap>
                <Logo href="/">
                    <Image src={LogoPNG} alt="Logo" loading="eager" />
                </Logo>
                <span>
                    © GSpot, 2020—2021
                    <br /> Create by <a href="">GSpot Team</a>
                </span>
            </Wrap>
        </StyledFooter>
    )
}

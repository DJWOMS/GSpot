'use client'

import { useEffect, useState } from 'react'
import { IconHeart, IconLogin, IconSearch, IconShoppingCart } from '@tabler/icons-react'
import Image from 'next/image'
import Link from 'next/link'
import styled from 'styled-components'
import LogoPNG from 'assets/img/logo.png'

interface HeaderComponentProps {
    hide: boolean
}
const HeaderComponent = styled.header<HeaderComponentProps>`
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #1b222e;
    z-index: 99;
    transition: 0.5s, margin 0s;

    ${(props) =>
        props.hide &&
        `
        top: -71px;
    `}
`
const Wrap = styled.div`
    border-bottom: 1px solid rgba(167, 130, 233, 0.06);
`
const Content = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    position: relative;
    height: 70px;
    width: 100%;
`
const Logo = styled(Link)`
    display: block;
    margin-left: 30px;
    height: auto;

    img {
        width: 120px;
        height: auto;
    }

    @media (min-width: 360px) {
        margin-left: 40px;
    }
    @media (min-width: 1200px) {
        margin-left: 0;
        width: 196px;
    }

    @media (min-width: 1310px) {
        width: 232px;
    }
`

interface MenuProps {
    open: boolean
}
const Menu = styled.button<MenuProps>`
    position: absolute;
    width: 24px;
    height: 22px;
    display: block;
    left: 0;
    top: 24px;

    span {
        position: absolute;
        left: 0;
        width: 24px;
        height: 2px;
        background-color: #fff;
        border-radius: 3px;
        transition: 0.5s;
        opacity: 1;

        ${(props) =>
            props.open
                ? `
            :first-child {
                transform: rotate(45deg);
                top: 10px;
            }
            :nth-child(2) {
                opacity: 0;
            }
            :last-child {
                width: 24px;
                transform: rotate(-45deg);
                top: 10px;
            }
        }
    `
                : `
            :first-child {
                top: 0;
            }
            :nth-child(2) {
                top: 10px;
                width: 16px;
            }
            :last-child {
                top: 20px;
                width: 8px;
            }`}
    }

    @media (min-width: 1200px) {
        display: none;
    }
`

interface NavProps {
    open: boolean
}
const Nav = styled.ul<NavProps>`
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    position: fixed;
    background-color: #1b222e;
    top: 71px;
    bottom: 0;
    left: ${(props) => (props.open ? '0' : '-100%')};
    width: 100%;
    z-index: 100;
    padding: 20px 15px 15px;
    transition: 0.5s ease;

    @media (min-width: 576px) {
        padding-left: calc((100% - 510px) / 2);
        padding-top: 20px;
    }
    @media (min-width: 768px) {
        padding-left: calc((100% - 690px) / 2);
    }
    @media (min-width: 992px) {
        padding-left: calc((100% - 930px) / 2);
    }
    @media (min-width: 1200px) {
        flex-direction: row;
        align-items: center;
        top: auto;
        left: auto;
        bottom: auto;
        position: relative;
        height: 70px;
        padding: 0;
        width: auto;
        z-index: 2;
        background-color: transparent;
        margin-right: auto;
        margin-left: 30px;

        :before {
            content: '';
            position: absolute;
            display: block;
            top: 24px;
            bottom: 24px;
            width: 1px;
            background-color: rgba(167, 130, 233, 0.06);
            left: -29px;
            pointer-events: none;
        }
    }
`
const NavItem = styled.li`
    margin-bottom: 20px;
    position: relative;

    @media (min-width: 1200px) {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        height: 70px;
        margin-bottom: 0;
        margin-right: 60px;

        :last-child {
            margin-right: 0;
        }
    }
`
const NavLink = styled(Link)`
    font-size: 12px;
    color: #fff;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    line-height: 22px;
    height: 22px;
    display: inline-flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;

    svg {
        stroke: #dbdada;
        width: 10px;
        height: auto;
        transition: stroke 0.5s ease;
        margin-left: 4px;
    }

    :hover {
        color: #a782e9;

        svg {
            color: #a782e9;
        }
    }
`
const Actions = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: end;
    align-items: center;
    height: 70px;
    width: 120px;

    :has(> :last-child:nth-child(2)) {
        justify-content: space-between;
    }

    @media (min-width: 576px) {
        width: 230px;
    }
    @media (min-width: 768px) {
        width: 240px;
    }
    @media (min-width: 1200px) {
        width: 230px;
    }
    @media (min-width: 1310px) {
        width: 262px;
    }
`

const LoginButton = styled.a`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 44px;
    height: 44px;
    background-color: rgba(167, 130, 233, 0.03);
    border: 1px solid rgba(167, 130, 233, 0.4);
    border-radius: 6px;

    svg {
        stroke: #fff;
        width: 22px;
        height: auto;
        transition: 0.5s;
    }
    span {
        display: none;
    }
    :hover {
        background-color: rgba(167, 130, 233, 0.04);
        border-color: rgba(167, 130, 233, 0.5);

        svg {
            stroke: #a782e9;
        }
    }

    @media (min-width: 576px) {
        width: 114px;

        svg {
            display: none;
        }
        span {
            display: block;
            font-size: 12px;
            color: #fff;
            letter-spacing: 0.4px;
            text-transform: uppercase;
            transition: 0.5s;
        }
        :hover span {
            color: #a782e9;
        }
    }
    @media (min-width: 768px) {
        width: 120px;
    }
    @media (min-width: 1200px) {
        width: 114px;
    }
    @media (min-width: 1310px) {
        width: 130px;
    }
`
const Form = styled.form`
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    height: 44px;
    width: 220px;
    background-color: rgba(167, 130, 233, 0.03);
    border: 1px solid rgba(167, 130, 233, 0.06);
    border-radius: 6px;
    position: relative;

    @media (min-width: 768px) {
        width: 260px;
    }
    @media (min-width: 1200px) {
        width: 426px;

        :before {
            content: '';
            position: absolute;
            display: block;
            top: 10px;
            bottom: 10px;
            width: 1px;
            background-color: rgba(167, 130, 233, 0.06);
            left: 196px;
            pointer-events: none;
        }
    }
    @media (min-width: 1310px) {
        width: 494px;

        :before {
            left: 232px;
        }
    }
`
const Select = styled.select`
    display: none;

    @media (min-width: 1200px) {
        display: block;
        width: 115px;
        height: 44px;
        border: none;
        background-color: transparent;
        font-size: 14px;
        color: #fff;
        padding: 0;
        background: url('/svg/arrow2.svg') no-repeat center right;
        background-size: 12px auto;
        cursor: pointer;

        option {
            padding: 0;
            margin: 0;
            color: #000;
        }
    }
    @media (min-width: 1310px) {
        width: 150px;
    }
`
const Input = styled.input`
    width: calc(100% - 50px);
    height: 44px;
    border-radius: 6px 0 0 6px;
    border: none;
    background-color: transparent;
    font-size: 14px;
    color: #fff;
    padding: 0 20px;

    @media (min-width: 1200px) {
        width: 196px;
    }
    @media (min-width: 1310px) {
        width: 232px;
    }
`
const SearchButton = styled.button`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 50px;
    height: 44px;
    position: relative;

    :before {
        content: '';
        position: absolute;
        display: block;
        top: 10px;
        bottom: 10px;
        width: 1px;
        background-color: rgba(167, 130, 233, 0.06);
        left: 0;
        pointer-events: none;
    }
    svg {
        width: 18px;
        height: auto;
        stroke: #a782e9;
    }
`
const ActionLink = styled(Link)`
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;

    svg {
        stroke: #a782e9;
        width: 22px;
        height: auto;
        transition: stroke 0.5s;
    }
    span {
        display: none;
    }

    @media (min-width: 576px) {
        span {
            display: block;
            font-size: 12px;
            color: #fff;
            text-transform: uppercase;
            letter-spacing: 0.4px;
            margin-left: 10px;
            transition: color 0.5s;
        }
        :hover span {
            color: #a782e9;
        }
    }
`

type HeaderLink = {
    href: string
    title: string
}
interface HeaderProps {
    links: Array<HeaderLink>
}
export function Header({ links }: HeaderProps) {
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
        setCurrentTop(window.pageYOffset)
    }

    const [openHeader, setOpenHeader] = useState(false)
    const toggleOpen = () => setOpenHeader((state) => !state)

    useEffect(() => {
        window.onscroll = () => (openHeader ? window.scrollTo(window.scrollX, window.scrollY) : () => void 0)
    }, [openHeader])

    return (
        <HeaderComponent hide={hideHeader}>
            <Wrap>
                <div className="container">
                    <Content>
                        <Menu open={openHeader} type="button" onClick={toggleOpen}>
                            <span></span>
                            <span></span>
                            <span></span>
                        </Menu>

                        <Logo href="/">
                            <Image src={LogoPNG} alt="Logo" loading="eager" />
                        </Logo>

                        <Nav open={openHeader}>
                            {links.map(({ href, title }, index) => (
                                <NavItem onClick={() => setOpenHeader(false)} key={index}>
                                    <NavLink href={href}>{title}</NavLink>
                                </NavItem>
                            ))}
                        </Nav>

                        <Actions>
                            <LoginButton href="/signin">
                                <IconLogin />
                                <span>Авторизация</span>
                            </LoginButton>
                        </Actions>
                    </Content>
                </div>
            </Wrap>

            <Wrap>
                <div className="container">
                    <Content>
                        <Form>
                            <Input type="text" placeholder="Я ищу..." />
                            <Select>
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
                            </Select>
                            <SearchButton>
                                <IconSearch />
                            </SearchButton>
                        </Form>

                        <Actions>
                            <ActionLink href="/favorite">
                                <IconHeart />
                                <span>Favorites</span>
                            </ActionLink>

                            <ActionLink href="/cart">
                                <IconShoppingCart />
                                <span>$00.00</span>
                            </ActionLink>
                        </Actions>
                    </Content>
                </div>
            </Wrap>
        </HeaderComponent>
    )
}

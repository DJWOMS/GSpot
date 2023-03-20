'use client'

import Link from 'next/link'
import styled from 'styled-components'

const StyledComponent = styled.ul`
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    margin-top: 30px;

    @media (min-width: 768px) {
        margin-top: 0;
    }
`

interface ItemProps {
    active?: boolean
}

const BreadcrumbItem = styled.li<ItemProps>`
    font-size: 14px;
    line-height: 22px;
    color: #dbdada;
    transition: 0.5s;
    position: relative;
    margin-right: 40px;
    letter-spacing: 0.4px;

    :first-child {
        padding-left: 25px;

        :after {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            height: 22px;
            width: 25px;
            background: url('/svg/home.svg') no-repeat center left/16px auto;
        }
    }

    :before {
        content: '';
        position: absolute;
        left: 100%;
        top: 0;
        height: 22px;
        width: 40px;
        background: url('/svg/breadcrumb.svg') no-repeat center/14px auto;
        opacity: 0.8;
    }

    :hover {
        color: #dbdada;
    }

    ${(props) =>
        props.active &&
        `
          cursor: default;
          margin-right: 0;

          :before {
              display: none;
          }

          :hover {
              color: #dbdada;
          }
      `}
`
const LinkBtn = styled(Link)`
    color: #fff;

    :hover {
        color: #a782e9;
    }
`

interface Item {
    name: string
    link?: string
}

type ItemType = {
    items: Item[]
}

export function Breadcrumbs(props: ItemType) {
    return (
        <StyledComponent>
            <BreadcrumbItem>
                <LinkBtn href="/">Главная</LinkBtn>
            </BreadcrumbItem>

            {props.items.map(({ name, link }, index, arr) => (
                <BreadcrumbItem active={arr.length - 1 === index} key={index}>
                    {link !== undefined ? <LinkBtn href={link}>{name}</LinkBtn> : name}
                </BreadcrumbItem>
            ))}
        </StyledComponent>
    )
}

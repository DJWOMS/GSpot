import { IconHeart } from '@tabler/icons-react'
import Link from 'next/link'
import styled from 'styled-components'

const CardCatalog = styled.div`
    position: relative;
    display: block;
    margin-top: 30px;
    border-radius: 6px;
    overflow: hidden;
    background-color: #1b222e;

    @media (min-width: 360px) {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: flex-start;
        flex-wrap: wrap;
        border-right: 1px solid rgba(167, 130, 233, 0.06);
    }

    @media (min-width: 576px) {
        flex-direction: column;
        border-right: none;
    }
`

const BadgeNew = styled.span`
    position: absolute;
    bottom: 20px;
    left: 15px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    color: #fff;
    background-color: #a782e9;
    border-radius: 6px;
    height: 24px;
    padding: 0 13px;
    font-family: var(--font-montserrat);
    font-size: 12px;
    font-weight: 500;
    z-index: 2;
    pointer-events: none;
`

const BadgePreorder = styled.span`
    position: absolute;
    bottom: 20px;
    left: 15px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    color: #fff;
    background-color: #f26c2a;
    border-radius: 6px;
    height: 24px;
    padding: 0 13px;
    font-family: var(--font-montserrat);
    font-size: 12px;
    font-weight: 500;
    z-index: 2;
    pointer-events: none;
`

const Cover = styled(Link)`
    position: relative;
    display: block;

    img {
        width: 100%;
        position: relative;
        z-index: 1;
        transition: 0.5s;
    }

    :hover img {
        opacity: 0.6;
    }

    @media (min-width: 360px) {
        width: 165px;
    }

    @media (min-width: 576px) {
        width: 100%;
    }
`

const colors: any = {
    ps: '#665cbe',
    xb: '#0e7a0d',
    wn: '#00aef0',
    ap: '#555',
}
interface PlatformItemProps {
    type: string;
}
const PlatformItem =
    styled.li <
    PlatformItemProps >
    `
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    margin-right: 10px;
    background-color: ${(props) => colors[props.type]};

    svg {
        fill: #fff;
        width: 14px;
        height: auto;
      }


      :last-child {
        margin-right: 0;
      }
`

const Platforms = styled.ul`
    position: absolute;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    top: 20px;
    left: 15px;
    z-index: 2;
    pointer-events: none;

    @media (min-width: 360px) {
        top: 15px;
        left: 15px;
    }

    @media (min-width: 576px) {
        top: 20px;
        left: 20px;
    }
`

const Title = styled.h3`
    overflow: hidden;
    white-space: nowrap;
    -o-text-overflow: ellipsis;
    text-overflow: ellipsis;
    word-wrap: break-word;
    width: 100%;
    margin-bottom: 15px;
    color: #fff;
    font-size: 16px;
    font-weight: 400;
    transition: 0.5s;

    :hover {
        color: #a782e9;
    }
`

const TitleWrap = styled.div`
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 15px;
    border-left: 1px solid rgba(167, 130, 233, 0.06);
    border-right: 1px solid rgba(167, 130, 233, 0.06);
    width: 100%;

    :last-child {
        border-bottom: 1px solid rgba(167, 130, 233, 0.06);
        border-radius: 0 0 6px 6px;
    }

    @media (min-width: 360px) {
        width: calc(100% - 165px);
        padding: 15px;
        border-left: none;
        border-right: none;
        border-top: 1px solid rgba(167, 130, 233, 0.06);

        ${Title} {
            white-space: normal;
        }

        :last-child {
            border-radius: 0 6px 6px 0;
            position: absolute;
            bottom: 0;
            top: 0;
            right: 0;
            justify-content: flex-start;
        }
    }

    @media (min-width: 576px) {
        width: 100%;
        padding: 20px;
        border-left: 1px solid rgba(167, 130, 233, 0.06);
        border-right: 1px solid rgba(167, 130, 233, 0.06);
        border-top: none;

        ${Title} {
            white-space: nowrap;
        }

        :last-child {
            position: relative;
            top: auto;
            bottom: auto;
            right: auto;
            border-radius: 0 0 6px 6px;
        }
    }
`

const TitleLink = styled(Link)`
    color: #fff;

    :hover {
        color: #a782e9;
    }
`

const Price = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-end;
    font-weight: 600;
    font-size: 16px;
    color: #fff;
    letter-spacing: 0.5px;
    line-height: 100%;

    s {
        font-size: 12px;
        color: #dbdada;
        margin-left: 10px;
        font-weight: 400;
        line-height: 100%;
    }
`

const Actions = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0 15px 15px;
    width: 100%;
    border-left: 1px solid rgba(167, 130, 233, 0.06);
    border-right: 1px solid rgba(167, 130, 233, 0.06);
    border-bottom: 1px solid rgba(167, 130, 233, 0.06);
    border-radius: 0 0 6px 6px;

    @media (min-width: 360px) {
        position: absolute;
        width: calc(100% - 165px);
        bottom: 0;
        right: 0;
        padding: 0 15px 15px;
        border-left: none;
        border-right: none;
        border-radius: 0;
    }

    @media (min-width: 576px) {
        position: relative;
        bottom: auto;
        right: auto;
        width: 100%;
        padding: 0 20px 20px;
        border-left: 1px solid rgba(167, 130, 233, 0.06);
        border-right: 1px solid rgba(167, 130, 233, 0.06);
        border-radius: 0 0 6px 6px;
    }
`

const ActionBuy = styled.button`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: calc(100% - 59px);
    height: 44px;
    border-radius: 6px;
    background-color: #29b474;
    color: #fff;
    font-weight: 600;
    font-size: 14px;
    letter-spacing: 0.8px;
    line-height: 16px;

    :hover {
        background-color: #a782e9;
        color: #fff;
    }
`

const ActionFavorite = styled.button`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 44px;
    height: 44px;
    background-color: rgba(167, 130, 233, 0.03);
    border: 1px solid rgba(167, 130, 233, 0.06);
    border-radius: 6px;

    svg {
        stroke: #a782e9;
        width: 22px;
        height: auto;
        transition: 0.5s;
    }

    :hover {
        background-color: rgba(167, 130, 233, 0.04);
        border-color: rgba(167, 130, 233, 0.07);

        svg {
            stroke: #fd6060;
        }
    }
`

interface CardProps {
    badge?: string;
    title: string;
    link: string;
    price: number;
    sale?: number;
}
export function Card({ badge, title, link, price, sale }: CardProps) {
    const rand = () => {
        return Math.floor(Math.random() * (1000 - 900 + 1) + 900)
    }

    return (
        <CardCatalog>
            <Cover href="/#">
                <img src={`https://picsum.photos/${rand()}`} alt="" />
                {badge && <BadgeNew>{badge}</BadgeNew>}
            </Cover>

            <Platforms>
                <PlatformItem type="ps" />
                <PlatformItem type="xb" />
                <PlatformItem type="wn" />
                <PlatformItem type="ap" />
            </Platforms>

            <TitleWrap>
                <Title>
                    <TitleLink href={link}>{title}</TitleLink>
                </Title>

                <Price>
                    {sale ? sale : price}
                    {sale && <s>{price}</s>}
                </Price>
            </TitleWrap>

            <Actions>
                <ActionBuy>Buy</ActionBuy>

                <ActionFavorite>
                    <IconHeart />
                </ActionFavorite>
            </Actions>
        </CardCatalog>
    )
}

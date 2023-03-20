'use client'

import Link from 'next/link'
import styled from 'styled-components'

export const Card = styled.div`
    position: relative;
    display: block;
    margin-top: 30px;
    border-radius: 6px;
    overflow: hidden;
    background-color: #1b222e;
`

export const CardCover = styled(Link)`
    position: relative;
    display: block;

    img {
        width: 100%;
        position: relative;
        max-height: 300px;
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

export const CardCatalog = styled(Card)`
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

export const CardBadgeNew = styled.span`
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

export const CardBadgePreorder = styled.span`
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

type ColorCodes<T extends string> = {
    [key in T]: string
} & { [key: string]: string }

const colors: ColorCodes<'ps' | 'xb' | 'wn' | 'ap'> = {
    ps: '#665cbe',
    xb: '#0e7a0d',
    wn: '#00aef0',
    ap: '#555',
}
interface PlatformItemProps {
    type: 'ps' | 'xb' | 'wn' | 'ap'
}
export const CardPlatformItem = styled.li<PlatformItemProps>`
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

export const CardPlatforms = styled.ul`
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

export const CardTitle = styled.h3`
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

export const CardTitleWrap = styled.div`
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

        ${CardTitle} {
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

        ${CardTitle} {
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

export const CardTitleLink = styled(Link)`
    color: #fff;

    :hover {
        color: #a782e9;
    }
`

export const CardPrice = styled.div`
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

export const CardWrap = styled.div`
    position: relative;
    width: 100%;
`

export const CardActions = styled.div`
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

export const CardActionBuy = styled.button`
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

export const CardActionFavorite = styled.button`
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

export const CardBig = styled(Card)`
    padding: 15px;
    border: 1px solid rgba(167, 130, 233, 0.06);

    ${CardCover} {
        border-radius: 6px;
        overflow: hidden;
    }
    ${CardTitle} {
        padding: 15px 0;
        border: none;

        h3 {
            font-size: 18px;
            margin-bottom: 0;
        }
    }
    ${CardActions} {
        padding: 0;
        margin-top: 20px;
        border: none;
    }
    ${CardPlatforms} {
        position: relative;
        top: auto;
        left: auto;
        margin-top: 20px;
    }

    @media (min-width: 360px) {
        padding: 20px;
    }

    @media (min-width: 768px) {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: stretch;

        ${CardTitle} {
            height: auto;
            width: 100%;
            padding: 0;

            h3 {
                font-size: 22px;
            }
        }
        ${CardCover} {
            width: 230px;
        }
        ${CardWrap} {
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: flex-start;
            width: calc(100% - 250px);
        }
        ${CardPrice} {
            margin-top: auto;
        }
        ${CardActionBuy} {
            width: 160px;
        }
    }

    @media (min-width: 1200px) {
        ${CardCover} {
            width: 240px;
        }
        ${CardWrap} {
            width: calc(100% - 260px);
        }
        ${CardTitle} {
            h3 {
                white-space: normal;
            }
        }
    }
`

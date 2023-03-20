'use client'

import { IconArrowLeft, IconArrowRight } from '@tabler/icons-react'
import Link from 'next/link'
import styled from 'styled-components'

const StyledComponent = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin-top: 40px;

    @media (min-width: 576px) {
        margin-top: 50px;
        justify-content: space-between;
    }
`

const Counter = styled.div`
    display: none;

    @media (min-width: 576px) {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        background-color: rgba(167, 130, 233, 0.03);
        border: 1px solid rgba(167, 130, 233, 0.06);
        height: 44px;
        padding: 0 20px;
        border-radius: 6px;
        font-size: 14px;
        color: #dbdada;
    }
`

const Wrap = styled.ul`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 44px;
    max-width: 100%;
`

const LinkBtn = styled(Link)`
    font-size: 14px;
    height: 44px;
    width: 44px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    background-color: rgba(167, 130, 233, 0.03);
    border: 1px solid rgba(167, 130, 233, 0.06);
    border-radius: 6px;
    color: #dbdada;
    text-align: center;
    position: relative;
`

const Item = styled.li`
    margin-right: 15px;

    :last-child {
        margin-right: 0;
    }

    :hover ${LinkBtn} {
        color: #fff;
        background-color: rgba(167, 130, 233, 0.04);
        border-color: rgba(167, 130, 233, 0.07);
    }
`

const ActiveItem = styled(Item)`
    cursor: default;

    ${LinkBtn} {
        color: #fff;
        cursor: default;
        border-color: rgba(167, 130, 233, 0.5);
    }

    :hover ${LinkBtn} {
        background-color: rgba(167, 130, 233, 0.04);
        border-color: rgba(167, 130, 233, 0.5);
        color: #fff;
    }

    @media (min-width: 576px) {
        margin-right: 20px;

        :last-child {
            margin-right: 0;
        }
    }
`

export function Pagination() {
    return (
        <div className="col-12">
            <StyledComponent>
                <Counter>12 from 144</Counter>

                <Wrap>
                    <Item>
                        <LinkBtn href="/prev">
                            <IconArrowLeft />
                        </LinkBtn>
                    </Item>
                    <ActiveItem>
                        <LinkBtn href="/1">1</LinkBtn>
                    </ActiveItem>
                    <Item>
                        <LinkBtn href="/2">2</LinkBtn>
                    </Item>
                    <Item>
                        <LinkBtn href="/3">3</LinkBtn>
                    </Item>
                    <Item>
                        <LinkBtn href="/next">
                            <IconArrowRight />
                        </LinkBtn>
                    </Item>
                </Wrap>
            </StyledComponent>
        </div>
    )
}

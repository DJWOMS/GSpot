'use client'

import React, { FC } from 'react'
import BlockCards from './BlockCards/blockCards'
import styled from 'styled-components'

export const SectionTitleWrap = styled.div`
    margin-top: 40px;
    position: relative;
    display: flex;
    flex-wrap: wrap;
    align-atems: center;
    justify-content: flex-start;
    align-items: flex-start;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
`

const mockData = [
    [
        {
            title: 'Gaming cards',
            content: [
                { title: 'The Evil Within: The Assignment', price: 1.99, sale: 60 },
                { title: 'DROD 4: Gunthro and the Epic Blunder', price: 4.99, sale: 50 },
                { title: 'Conquests of the Longbow: The Legend of Robin Hood', price: 3.59, sale: 40 },
            ],
        },
    ],
    [
        {
            title: 'Gift cards',
            content: [
                { title: 'Phantasmagoria 2: A Puzzle of Flesh', price: 3.89, sale: 60 },
                { title: 'Shadowrun Hong Kong - Extended Edition Deluxe Upgrade', price: 4.99, sale: 50 },
                { title: 'We are the Dwarves', price: 3.59, sale: 40 },
            ],
        },
    ],
    [
        {
            title: 'Subscriptions',
            content: [
                { title: 'Gabriel Knight: Sins of the Fathers', price: 3.89, sale: 60 },
                { title: 'Unrest Special Edition', price: 7.49, sale: 50 },
                { title: 'Gabriel Knight 3: Blood of the Sacred, Blood of the Damned', price: 3.89, sale: 40 },
            ],
        },
    ],
]

const CardsIndex: FC = ({}): JSX.Element => {
    return (
        <SectionTitleWrap>
            {mockData.map((item, id: number) => (
                <BlockCards key={id} item={item} />
            ))}
        </SectionTitleWrap>
    )
}

export default CardsIndex

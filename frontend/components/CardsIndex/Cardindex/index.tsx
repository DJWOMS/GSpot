'use client'
import React, { FC } from 'react'
import styled from 'styled-components'

interface cardItem {
    content: cardItemContent;
}

interface cardItemContent {
    title: string;
    price: number;
    sale: number;
}

const Wrapper = styled.div`
    width: 350px;
    border-radius: 10px;
    // border: 1px solid inherit;
    padding: 20px;
    display: flex;
    gap: 20px;
    cursor: pointer;
    opacity: 0.7;
    &:hover {
        opacity: 1;
    }
`

const Image = styled.div`
    width: 120px;
    height: 140px;
    background-color: #444;
    border-radius: 10px;
`

const Description = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
`

const TitleCard = styled.p`
    font-weight: 15px;
    color: white;
`

const DescriptionActive = styled.div`
    display: flex;
    justify-content: space-between;
`

const DescriptionPrice = styled.div`
    color: white;
    font-size: 30px;
`

const DescriptionSale = styled.div`
    color: red;
`

const DescriptionOldPrice = styled.span`
    color: white;
    text-decoration: line-through;
    padding-right: 10px;
`

const AddCart = styled.button`
    margin-top: 20px;
    width: 50px;
    height: 50px;
    background: #29b474;
    border-radius: 10px;
    color: white;
    font-size: 40px;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 100;
    &:hover {
        background: #a782e9;
    }
`

const CardIndex: FC<cardItem> = ({ content: { title, price, sale } }) => {
    return (
        <Wrapper>
            <Image />
            <Description>
                <TitleCard>{title}</TitleCard>
                <DescriptionActive>
                    <div>
                        <DescriptionPrice>${price}</DescriptionPrice>
                        <DescriptionSale>
                            <DescriptionOldPrice>${sale}</DescriptionOldPrice>
                            60% OFF
                        </DescriptionSale>
                    </div>
                    <AddCart>+</AddCart>
                </DescriptionActive>
            </Description>
        </Wrapper>
    )
}

export default CardIndex

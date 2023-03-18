'use client'

import styled from 'styled-components'

export const Wrapper = styled.div`
    width: 350px;
    border-radius: 10px;
    // border: 1px solid inherit;
    padding: 20px;
    display: flex;
    gap: 20px;
    cursor: pointer;
    opacity: 0.7;
    &:hover {
        // border: 1px solid white;
        opacity: 1;
    }
`

export const Image = styled.div`
    width: 120px;
    height: 140px;
    background-color: #444;
    border-radius: 10px;
`

export const Description = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
`

export const TitleCard = styled.p`
    font-weight: 15px;
    color: white;
`

export const DescriptionActive = styled.div`
    display: flex;
    justify-content: space-between;
`

export const DescriptionPrice = styled.div`
    color: white;
    font-size: 30px;
`

export const DescriptionSale = styled.div`
    color: red;
`

export const DescriptionOldPrice = styled.span`
    color: white;
    text-decoration: line-through;
    padding-right: 10px;
`

export const AddCart = styled.button`
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

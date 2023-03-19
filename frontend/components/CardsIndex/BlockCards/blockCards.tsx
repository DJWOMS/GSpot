import React, { FC } from 'react'
import CardIndex from '../Cardindex'
import styled from 'styled-components'

const Wrapper = styled.div`
    width: 350px;
`

const TitleCards = styled.div`
    display: flex;
    justify-content: space-between;
    color: #fff;
    margin: 10px;
    font-weight: 100;
`
const ButtonTitle = styled.button`
    width: 80px;
    height: 20x;
    border-radius: 5px;
    color: #fff;
    border: 1px solid #333;
    &:hover {
        color: #a782e9;
    }
`

const WrapperCards = styled.div`
    display: flex;
    flex-direction: column;
    hieght: 1000px;
    border: 1px solid #333;
    border-radius: 10px;
    &:hover {
        border: 1px solid white;
    }
`

const BlockCards: FC<any> = ({ item }): JSX.Element => {
    const { content, title } = item[0]
    return (
        <Wrapper>
            <TitleCards>
                <h3>{title}</h3>
                <ButtonTitle>View All</ButtonTitle>
            </TitleCards>
            <WrapperCards>
                {content.map((content: any, id: number) => (
                    <CardIndex key={id} content={content} />
                ))}
            </WrapperCards>
        </Wrapper>
    )
}

export default BlockCards

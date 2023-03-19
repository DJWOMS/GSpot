'use client'

import { Section, SectionNavWrap, SectionTitle, SectionTitleWrapSingle, SectionView } from '@/components'
import { IconPlus } from '@tabler/icons-react'
import styled from 'styled-components'

const List = styled.ul`
    position: relative;
    display: block;
    padding: 15px;
    border-radius: 6px;
    border: 1px solid rgba(167, 130, 233, 0.06);
    margin-top: 30px;

    margin-bottom: 40px;

    @media (min-width: 360px) {
        padding: 20px;
    }

    @media (min-width: 768px) {
        margin-bottom: 60px;
    }

    @media (min-width: 1200px) {
        margin-bottom: 0;
    }
`

const Item = styled.li`
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: stretch;
    padding-top: 15px;
    margin-top: 15px;
    border-top: 1px solid rgba(167, 130, 233, 0.06);
    position: relative;

    :first-child {
        margin-top: 0;
        padding-top: 0;
        border: none;
    }

    @media (min-width: 360px) {
        padding-top: 20px;
        margin-top: 20px;

        :first-child {
            margin-top: 0;
            padding-top: 0;
        }
    }
`

const Cover = styled.a`
    position: relative;
    display: block;
    border-radius: 6px;
    overflow: hidden;
    width: 90px;

    img {
        width: 100%;
        position: relative;
        z-index: 1;
        transition: 0.5s;
    }

    :hover img {
        opacity: 0.6;
    }

    @media (min-width: 576px) {
        width: 105px;
    }
`

const Wrap = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    width: calc(100% - 105px);

    @media (min-width: 576px) {
        width: calc(100% - 125px);
    }
`

const Title = styled.h3`
    width: 100%;
    margin-bottom: 10px;
    color: #fff;
    font-size: 16px;
    font-weight: 400;
    transition: 0.5s;

    :hover {
        color: #a782e9;
    }

    a {
        color: #fff;

        :hover {
            color: #a782e9;
        }
    }
`

const Price = styled.div`
    margin-top: auto;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    flex-wrap: wrap;
    width: 100%;

    span {
        width: 100%;
        font-size: 24px;
        color: #fff;
        font-weight: 600;
        line-height: 100%;
        display: block;
    }

    s {
        font-size: 13px;
        color: #dbdada;
        margin-top: 7px;
        margin-right: 15px;
    }

    b {
        font-size: 13px;
        color: #fd6060;
        margin-top: 7px;
        margin-right: 15px;
        font-weight: 600;
    }
`

const Buy = styled.button`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 44px;
    height: 44px;
    border-radius: 6px;
    background-color: #29b474;
    position: absolute;
    right: 0;
    bottom: 0;

    svg {
        stroke: #fff;
        width: 24px;
        height: auto;
    }

    :hover {
        background-color: #a782e9;
    }
`

function ListItem() {
    return (
        <Item>
            <Cover>
                <img src="https://picsum.photos/240/340" alt="" />
            </Cover>

            <Wrap>
                <Title>
                    <a href="#">The Evil Within: The Assignment</a>
                </Title>

                <Price>
                    <span>$1.99</span>
                    <s>$4.99</s>
                    <b>60% OFF</b>
                </Price>

                <Buy>
                    <IconPlus />
                </Buy>
            </Wrap>
        </Item>
    )
}

export function OtherGames() {
    return (
        <Section>
            <div className="container">
                <div className="row">
                    <div className="col-12 col-md-6 col-xl-4">
                        <SectionTitleWrapSingle>
                            <SectionTitle small>Gaming Cards</SectionTitle>
                            <SectionNavWrap>
                                <SectionView>View All</SectionView>
                            </SectionNavWrap>
                        </SectionTitleWrapSingle>

                        <List>
                            <ListItem />
                            <ListItem />
                            <ListItem />
                        </List>
                    </div>

                    <div className="col-12 col-md-6 col-xl-4">
                        <SectionTitleWrapSingle>
                            <SectionTitle small>Gift Cards</SectionTitle>
                            <SectionNavWrap>
                                <SectionView>View All</SectionView>
                            </SectionNavWrap>
                        </SectionTitleWrapSingle>

                        <List>
                            <ListItem />
                            <ListItem />
                            <ListItem />
                        </List>
                    </div>

                    <div className="col-12 col-md-6 col-xl-4">
                        <SectionTitleWrapSingle>
                            <SectionTitle small>Subscriptions</SectionTitle>
                            <SectionNavWrap>
                                <SectionView>View All</SectionView>
                            </SectionNavWrap>
                        </SectionTitleWrapSingle>

                        <List>
                            <ListItem />
                            <ListItem />
                            <ListItem />
                        </List>
                    </div>
                </div>
            </div>
        </Section>
    )
}

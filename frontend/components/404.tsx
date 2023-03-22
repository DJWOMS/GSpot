import Link from 'next/link'
import { FC } from 'react'
import styled from 'styled-components'

const Page404 = styled.div`
    display: block;
    position: relative;
`
const Wrap = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    min-height: 100vh;
    padding: 40px 0;
`
const Content = styled.div`
    background-color: #1b222e;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 1px solid rgba(167, 130, 233, 0.06);
    border-radius: 6px;
    padding: 40px 20px;
    position: relative;
    width: 100%;
    max-width: 400px;

    @media (min-width: 576px) {
        padding: 50px;
    }
`
const Title = styled.h1`
    position: relative;
    color: #a782e9;
    line-height: 100%;
    font-size: 120px;
    margin-bottom: 20px;
    font-weight: 500;
    font-family: var(--font-montserrat);
`
const Text = styled.p`
    text-align: center;
    display: block;
    width: 100%;
    color: #fff;
    font-size: 14px;
    line-height: 26px;
    margin-bottom: 40px;
`
const LinkBtn = styled(Link)`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 140px;
    height: 44px;
    border-radius: 6px;
    background-color: #29b474;
    color: #fff;
    font-weight: 600;
    font-size: 13px;
    letter-spacing: 0.6px;
    text-transform: uppercase;

    :hover {
        background-color: #a782e9;
        color: #fff;
    }
`

const PageNotFound: FC = () => {
    return (
        <Page404>
            <Wrap>
                <Content>
                    <Title>404</Title>
                    <Text>The page you are looking for not available!</Text>
                    <LinkBtn href="/">go back</LinkBtn>
                </Content>
            </Wrap>
        </Page404>
    )
}

export default PageNotFound

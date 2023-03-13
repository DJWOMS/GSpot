/* eslint-disable no-unexpected-multiline */
/* eslint-disable @typescript-eslint/no-explicit-any */
'use client'

import styled from 'styled-components'

interface SectionProps {
    first?: boolean;
    last?: boolean;
}

export const Section =
    styled.section <
    SectionProps >
    `
    position: relative;
    padding-top: ${(props) => (props.first ? '200px' : '60px')};
    padding-bottom: ${(props) => (props.last ? '60px' : null)};

    @media (min-width: 576px) {
        padding-top: ${(props) => (props.first ? '210px' : '70px')};
        padding-bottom: ${(props) => (props.last ? '70px' : null)};
    }
    @media (min-width: 768px) {
        padding-top: ${(props) => (props.first ? '220px' : '80px')};
        padding-bottom: ${(props) => (props.last ? '80px' : null)};
    }
    @media (min-width: 1200px) {
        padding-top: ${(props) => (props.first ? '230px' : '90px')};
        padding-bottom: ${(props) => (props.last ? '90px' : null)};
    }
`

export const SectionBg = styled(Section)`
    overflow: hidden;
    :before {
        content: '';
        position: absolute;
        display: block;
        z-index: 1;
        top: 140px;
        left: 0;
        right: 0;
        height: 500px;
        pointer-events: none;
        background: -webkit-linear-gradient(top, rgba(27, 34, 46, 0.7) 0%, #1b222e 100%);
        background: -ms-linear-gradient(top, rgba(27, 34, 46, 0.7) 0%, #1b222e 100%);
        background: linear-gradient(to bottom, rgba(27, 34, 46, 0.7) 0%, #1b222e 100%);
    }

    .container {
        position: relative;
        z-index: 2;
    }
`

export const SectionFullBg = styled.section`
    overflow: hidden;
    :before {
        content: '';
        position: absolute;
        display: block;
        z-index: 1;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
        background-color: rgba(27, 34, 46, 0.7);
    }

    .container {
        position: relative;
        z-index: 2;
    }
`

export const SectionHead = styled(Section)`
    overflow: hidden;
    :before {
        content: '';
        position: absolute;
        display: block;
        z-index: 1;
        top: 140px;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
        background-color: rgba(27, 34, 46, 0.7);
    }

    .container {
        position: relative;
        z-index: 2;
    }
`

export const SectionCategory = styled(Section)`
    padding-top: 40px;
`

export const SectionNavWrap = styled.div`
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    width: 100%;
    margin-top: 20px;
    gap: 10px;

    @media (min-width: 768px) {
        margin-top: 0;
        width: auto;
        gap: 15px;
    }
`

export const SectionNav = styled.button`
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 30px;
    height: 30px;
    background-color: rgba(167, 130, 233, 0.03);
    border: 1px solid rgba(167, 130, 233, 0.06);
    border-radius: 6px;

    svg {
        stroke: #dbdada;
        transition: 0.5s;
        width: 18px;
        height: auto;
    }

    :hover {
        background-color: rgba(167, 130, 233, 0.04);
        border-color: rgba(167, 130, 233, 0.07);

        svg {
            stroke: #a782e9;
        }
    }
`

export const SectionTitleWrap = styled.div`
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;

    @media (min-width: 768px) {
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 5px;
    }
`

interface SectionTitleProps {
    uppercase?: boolean;
    small?: boolean;
    pre?: boolean;
    downloads?: boolean;
}
export const SectionTitle =
    styled.h2 <
    SectionTitleProps >
    `
    color: #fff;
    font-weight: ${(props) => (props.uppercase ? '300' : '400')};
    font-size: ${(props) => (props.small ? '26px' : '28px')};
    line-height: ${(props) => (props.uppercase ? '130%' : '110%')};
    margin-bottom: 0;
    position: relative;
    padding-left: ${(props) => (props.small ? '0px' : '30px')};
    font-family: 'Montserrat', sans-serif;
    text-transform: ${(props) => (props.uppercase ? 'uppercase' : null)};

    :before {
        content: '';
        position: absolute;
        display: block;
        top: 2px;
        bottom: 2px;
        left: 0;
        width: 3px;
        background-color: ${(props) => (props.pre ? '#f26c2a' : props.downloads ? '#5074e1' : '#a782e9')};
        border-radius: 4px;
    }

    b {
        font-weight: 500;
    }
    span {
        font-size: 14px;
        color: #dbdada;
        font-family: 'Open Sans', sans-serif;
        letter-spacing: 0.4px;
    }
`

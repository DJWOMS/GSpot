'use client'

import Image from 'next/image'
import { IconMessages, IconClockHour4, IconPlayerPlay } from '@tabler/icons-react'
import React, { FC } from 'react'
import styled from 'styled-components'

const PostStyle = styled.div`
    display: flex;
    flex-direction: column;
    position: relative;
    border-radius: 6px;
    border: 1px solid rgba(167, 130, 233, 0.06);
    margin: 10px;
    margin-bottom: 10px;
`

const PostCover = styled.a`
    display: block;
    width: 100%;
    position: relative;
    // box-sizing: border-box;
    // overflow: hidden;
    img {
        width: 100%;
        position: relative;
        z-index: 1;
        transition: opacity 0.5s ease;
        opacity: 0.8;
        // width: 300px;
    }
    img:hover {
        opacity: 0.6;
    }
`

const PostVideo = styled.a`
    position: absolute;
    top: 10px;
    left: 10px;
    z-index: 2;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 55px;
    height: 55px;
    border-radius: 50%;
    border: 1px solid rgba(167, 130, 233, 0.4);
    background-color: rgba(167, 130, 233, 0.15);
    margin: 20px;
    svg {
        stroke: #a782e9;
        width: 22px;
        height: auto;
        margin-left: 2px;
        position: relative;
        z-index: 2;
    }
    &:before {
        content: '';
        position: absolute;
        display: block;
        z-index: 1;
        pointer-events: none;
        top: 5px;
        left: 5px;
        bottom: 5px;
        right: 5px;
        border-radius: 50%;
        background-color: #1b222e;
    }
    &:hover {
        border-color: rgba(167, 130, 233, 0.6);
        background-color: rgba(167, 130, 233, 0.3);
    }
`

const PostContent = styled.div`
    display: block;
    padding: 20px 15px;
`

const PostTitle = styled.h3`
    display: block;
    height: 66px;
    margin-top: 15px;
    font-size: 22px;
    color: #fff;
    font-weight: 400;
    margin-bottom: 0;
    overflow: hidden;
    a {
        display: block;
        color: #fff;
    }
    a:hover {
        color: #a782e9;
    }
`

const PostDate = styled.span`
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    font-size: 13px;
    color: #dbdada;

    svg {
        stroke: #a782e9;
        width: 16px;
        height: auto;
        margin-right: 5px;
    }
`

const PostCategory = styled.a`
    display: inline-flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 24px;
    min-width: 74px;
    width: auto;
    color: #dbdada;
    font-size: 12px;
    border: 1px solid rgba(167, 130, 233, 0.4);
    background-color: rgba(167, 130, 233, 0.15);
    border-radius: 6px;
    padding: 0 13px;
    letter-spacing: 0.4px;

    &:hover {
        color: #fff;
        border-color: rgba(167, 130, 233, 0.6);
        background-color: rgba(167, 130, 233, 0.3);
    }
`

const PostComments = styled.span`
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    font-size: 13px;
    color: #dbdada;

    svg {
        stroke: #a782e9;
        width: 16px;
        height: auto;
        margin-right: 5px;
    }
`

const PostMeta = styled.div`
    margin-top: 15px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    height: 20px;
`

const Post: FC = (): JSX.Element => (
    <div className="col-md-6 col-xl-4">
        <PostStyle>
            <PostCover href="#">
                <Image width={240} height={340} src="https://picsum.photos/240/340" alt="Logo" loading="eager" />
            </PostCover>
            <PostVideo href="#">
                <IconPlayerPlay />
            </PostVideo>
            <PostContent>
                <PostCategory href="#">CS:GO</PostCategory>
                <PostTitle>
                    <a href="interview.html">Главные 20 CS:GO игроков of 2023 согласно to Gspot.tv</a>
                </PostTitle>
                <PostMeta>
                    <PostDate>
                        <IconClockHour4 />2 часа назад
                    </PostDate>
                    <PostComments>
                        <IconMessages />
                        34
                    </PostComments>
                </PostMeta>
            </PostContent>
        </PostStyle>
    </div>
)

export default Post

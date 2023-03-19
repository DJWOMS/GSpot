'use client'

import { IconClockHour4, IconMessages, IconPlayerPlay } from '@tabler/icons-react'
import { SectionNavWrap, SectionTitle, SectionTitleWrapSingle, SectionView } from '@/components/Section'
import styled from 'styled-components'

const Section = styled.section`
    position: relative;
    padding-top: 60px;
`

const Post = styled.div`
    position: relative;
    margin-top: 30px;
    border-radius: 6px;
    border: 1px solid rgba(167, 130, 233, 0.06);
    overflow: hidden;
`

const PostContent = styled.div`
    display: block;
    padding: 20px 15px;

    @media (min-width: 360px) {
        padding: 20px;
    }
`

const PostImg = styled.a`
    display: block;
    width: 100%;
    position: relative;
    padding: 15px 15px 0;

    img {
        width: 100%;
        position: relative;
        z-index: 1;
        transition: opacity 0.5s ease;
        border-radius: 6px;
        opacity: 0.8;
    }

    :hover img {
        opacity: 0.6;
    }

    @media (min-width: 360px) {
        padding: 20px 20px 0;
    }
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

        :hover {
            color: #a782e9;
        }
    }
`

const PostBig = styled(Post)`
    ${PostImg} {
        padding: 0;

        :before {
            content: '';
            position: absolute;
            display: block;
            z-index: 2;
            bottom: 0;
            left: 0;
            right: 0;
            top: 0;
            pointer-events: none;
            background: -webkit-linear-gradient(top, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.6) 100%);
            background: -ms-linear-gradient(top, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.6) 100%);
            background: linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.6) 100%);
        }
        img {
            border-radius: 0;
        }
    }

    @media (min-width: 768px) {
        ${PostContent} {
            position: absolute;
            z-index: 2;
            bottom: 0;
            left: 0;
            right: 0;
            width: 100%;
        }
        ${PostImg} {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            width: 100%;
            height: 360px;
            cursor: default;

            img {
                width: auto;
                height: auto;
                min-width: 100%;
                min-height: 100%;
            }
        }

        :hover {
            ${PostImg} {
                img {
                    opacity: 0.6;
                }
            }
        }
    }
    @media (min-width: 768px) {
        ${PostTitle} {
            padding-right: 30%;
        }
    }

    @media (min-width: 992px) {
        ${PostTitle} {
            padding-right: 0;
        }
    }

    @media (min-width: 1200px) {
        ${PostTitle} {
            padding-right: 33%;
        }
    }
`

const PostCover = styled.a`
    display: block;
    width: 100%;
    position: relative;

    img {
        width: 100%;
        position: relative;
        z-index: 1;
        transition: opacity 0.5s ease;
        opacity: 0.8;
    }

    :hover img {
        opacity: 0.6;
    }

    @media (min-width: 768px) {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        width: 100%;
        height: 200px;

        img {
            width: auto;
            height: auto;
            min-width: 100%;
            min-height: 100%;
        }
    }

    @media (min-width: 992px) {
        height: 275px;
    }

    @media (min-width: 1200px) {
        height: 212px;
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

    :hover {
        color: #fff;
        border-color: rgba(167, 130, 233, 0.6);
        background-color: rgba(167, 130, 233, 0.3);
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

    svg {
        stroke: #a782e9;
        width: 22px;
        height: auto;
        margin-left: 2px;
        position: relative;
        z-index: 2;
    }
    :before {
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
    :hover {
        border-color: rgba(167, 130, 233, 0.6);
        background-color: rgba(167, 130, 233, 0.3);
    }

    @media (min-width: 360px) {
        left: 15px;
        top: 15px;
    }
`

export function LatestNews() {
    return (
        <Section>
            <div className="container">
                <div className="row">
                    <div className="col-12">
                        <SectionTitleWrapSingle>
                            <SectionTitle>Latest news</SectionTitle>

                            <SectionNavWrap>
                                <SectionView>View All</SectionView>
                            </SectionNavWrap>
                        </SectionTitleWrapSingle>
                    </div>

                    <div className="col-12 col-md-12 col-lg-6">
                        <PostBig>
                            <PostImg>
                                <img src="https://picsum.photos/1001" alt="" />
                            </PostImg>

                            <PostContent>
                                <PostCategory>NFS</PostCategory>
                                <PostTitle>
                                    <a href="article.html">New hot race from your favorite computer games studio</a>
                                </PostTitle>
                                <PostMeta>
                                    <PostDate>
                                        <IconClockHour4 />3 h ago
                                    </PostDate>
                                    <PostComments>
                                        <IconMessages />3
                                    </PostComments>
                                </PostMeta>
                            </PostContent>
                        </PostBig>
                    </div>

                    <div className="col-12 col-md-12 col-lg-6">
                        <PostBig>
                            <PostImg>
                                <img src="https://picsum.photos/1002" alt="" />
                            </PostImg>

                            <PostVideo>
                                <IconPlayerPlay />
                            </PostVideo>

                            <PostContent>
                                <PostCategory>CS:GO</PostCategory>
                                <PostTitle>
                                    <a href="article.html">New hot race from your favorite computer games studio</a>
                                </PostTitle>
                                <PostMeta>
                                    <PostDate>
                                        <IconClockHour4 />3 h ago
                                    </PostDate>
                                    <PostComments>
                                        <IconMessages />
                                        10
                                    </PostComments>
                                </PostMeta>
                            </PostContent>
                        </PostBig>
                    </div>

                    <div className="col-12 col-md-6 col-xl-4">
                        <Post>
                            <PostCover>
                                <img src="https://picsum.photos/1003" alt="" />
                            </PostCover>

                            <PostVideo>
                                <IconPlayerPlay />
                            </PostVideo>

                            <PostContent>
                                <PostCategory>Overview</PostCategory>
                                <PostTitle>
                                    <a href="article.html">New hot race from your favorite computer games studio</a>
                                </PostTitle>
                                <PostMeta>
                                    <PostDate>
                                        <IconClockHour4 />3 h ago
                                    </PostDate>
                                    <PostComments>
                                        <IconMessages />2
                                    </PostComments>
                                </PostMeta>
                            </PostContent>
                        </Post>
                    </div>

                    <div className="col-12 col-md-6 col-xl-4">
                        <Post>
                            <PostCover>
                                <img src="https://picsum.photos/1004" alt="" />
                            </PostCover>

                            <PostContent>
                                <PostCategory>PC</PostCategory>
                                <PostTitle>
                                    <a href="article.html">New hot race from your favorite computer games studio</a>
                                </PostTitle>
                                <PostMeta>
                                    <PostDate>
                                        <IconClockHour4 />3 h ago
                                    </PostDate>
                                    <PostComments>
                                        <IconMessages />0
                                    </PostComments>
                                </PostMeta>
                            </PostContent>
                        </Post>
                    </div>

                    <div className="col-12 col-md-6 col-xl-4">
                        <Post>
                            <PostCover>
                                <img src="https://picsum.photos/1005" alt="" />
                            </PostCover>

                            <PostContent>
                                <PostCategory>VR</PostCategory>
                                <PostTitle>
                                    <a href="article.html">New hot race from your favorite computer games studio</a>
                                </PostTitle>
                                <PostMeta>
                                    <PostDate>
                                        <IconClockHour4 />3 h ago
                                    </PostDate>

                                    <PostComments>
                                        <IconMessages />
                                        50
                                    </PostComments>
                                </PostMeta>
                            </PostContent>
                        </Post>
                    </div>
                </div>
            </div>
        </Section>
    )
}

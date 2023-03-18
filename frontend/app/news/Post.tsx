import React, { FC } from 'react'
import styled from 'styled-components'

const Post_style = styled.div`
    display: flex;
    flex-direction: column;
    margin-top: 200px;
    position: relative;
    padding: 20px;
    border-radius: 6px;
    border: 1px solid rgba(167, 130, 233, 0.06);
    margin-bottom: 10px;
`

const Post__cover = styled.a`
    display: block;
    width: 100%;
    position: relative;
    box-sizing: border-box;
    overflow: hidden;
    img {
        width: 100%;
        position: relative;
        z-index: 1;
        transition: opacity 0.5s ease;
        opacity: 0.8;
        width: 300px;
    }
    img:hover {
        opacity: 0.6;
    }
`

const Post__video = styled.a`
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

const Post__content = styled.div`
    display: block;
    padding: 20px 15px;
`

const Post__title = styled.h3`
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

const Post__meta = styled.div`
    margin-top: 15px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    height: 20px;
`

const Post__date = styled.span`
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    font-size: 13px;
    color: #dbdada;
`

const Post__category = styled.a`
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

const Post: FC<any> = ({}): JSX.Element => {
    return (
        <div className="col-md-6 col-xl-4">
            <Post_style>
                <Post__cover href="interview.html">
                    <img src="https://www.freecodecamp.org/news/content/images/2019/12/ubuntu-1479782_1280.jpg" alt="" />
                </Post__cover>
                <Post__video href="#">
                    <svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
                        <path d="M112,111V401c0,17.44,17,28.52,31,20.16l247.9-148.37c12.12-7.25,12.12-26.33,0-33.58L143,90.84C129,82.48,112,93.56,112,111Z" />
                    </svg>
                </Post__video>
                <Post__content>
                    <Post__category href="#">CS:GO</Post__category>
                    <Post__title>
                        <a href="interview.html">Top 20 CS:GO players of 2020 according to HOTFLIX.tv</a>
                    </Post__title>
                    <Post__meta>
                        <Post__date>
                            {/* <svg xmlns='http://www.w3.org/2000/svg' width='512' height='512' viewBox='0 0 512 512'> */}
                            {/* <path d='M256,64C150,64,64,150,64,256s86,192,192,192,192-86,192-192S362,64,256,64Z' style='fill:none;stroke-miterlimit:10;stroke-width:32px'/> */}
                            {/* <polyline points='256 128 256 272 352 272' style='fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px'/></svg> */}
                            3 hours ago
                        </Post__date>
                        {/* <span className="post__comments">
                        <svg xmlns='http://www.w3.org/2000/svg' width='512' height='512' viewBox='0 0 512 512'>
                        <path d='M431,320.6c-1-3.6,1.2-8.6,3.3-12.2a33.68,33.68,0,0,1,2.1-3.1A162,162,0,0,0,464,215c.3-92.2-77.5-167-173.7-167C206.4,48,136.4,105.1,120,180.9a160.7,160.7,0,0,0-3.7,34.2c0,92.3,74.8,169.1,171,169.1,15.3,0,35.9-4.6,47.2-7.7s22.5-7.2,25.4-8.3a26.44,26.44,0,0,1,9.3-1.7,26,26,0,0,1,10.1,2L436,388.6a13.52,13.52,0,0,0,3.9,1,8,8,0,0,0,8-8,12.85,12.85,0,0,0-.5-2.7Z'/><path d='M66.46,232a146.23,146.23,0,0,0,6.39,152.67c2.31,3.49,3.61,6.19,3.21,8s-11.93,61.87-11.93,61.87a8,8,0,0,0,2.71,7.68A8.17,8.17,0,0,0,72,464a7.26,7.26,0,0,0,2.91-.6l56.21-22a15.7,15.7,0,0,1,12,.2c18.94,7.38,39.88,12,60.83,12A159.21,159.21,0,0,0,284,432.11'/>
                        </svg> 50</span> */}
                    </Post__meta>
                </Post__content>
            </Post_style>
        </div>
    )
}

export default Post

'use client'

import { useState, useEffect } from 'react'
import { Card, CardBig } from '@/components/Card'
import { Swiper, SwiperSlide } from 'swiper/react'
import SwiperCore, { Autoplay } from 'swiper'
import { Swiper as SwiperType } from 'swiper/types'
import 'swiper/swiper.css'

import styled from 'styled-components'

const CarouselComponent = styled.div`
    position: relative;
    width: 100%;
    padding-left: 15px;
    overflow: hidden;

    img {
        width: auto;
        max-width: 100%;
    }

    ${Card} {
        width: 220px;
    }

    ${CardBig} {
        width: 270px;
    }

    @media (min-width: 576px) {
        padding-left: calc((100% - 510px) / 2);

        ${CardBig} {
            width: 280px;
        }
    }

    @media (min-width: 768px) {
        padding-left: 0;
        width: 690px;
        margin: 0 auto;

        ${Card} {
            width: 100%;
        }

        ${CardBig} {
            width: 100%;
        }
    }

    @media (min-width: 992px) {
        width: 930px;
    }

    @media (min-width: 1200px) {
        width: 1110px;
    }

    @media (min-width: 1310px) {
        width: 1280px;
    }

    .swiper-wrapper {
        box-sizing: border-box;
    }
`

interface CarouselProps {
    prevRef?: React.RefObject<HTMLElement>;
    nextRef?: React.RefObject<HTMLElement>;
    breakpoints: object;
    children: Array<React.ReactNode>;
}

SwiperCore.use([Autoplay])

export const Carousel = ({ prevRef, nextRef, breakpoints, children }: CarouselProps) => {
    const [swiper, setSwiper] = useState<SwiperType | null>(null)

    // event: click prevButton
    useEffect(() => {
        const prevBtn = prevRef?.current
        const prevSlide = () => {
            swiper?.slidePrev()
        }

        if (prevBtn) {
            prevBtn.addEventListener('click', prevSlide)
        }

        return () => {
            if (prevBtn) {
                prevBtn.removeEventListener('click', prevSlide)
            }
        }
    }, [swiper, prevRef])

    // event: click nextButton
    useEffect(() => {
        const nextBtn = nextRef?.current
        const nextSlide = () => swiper?.slideNext()

        if (nextBtn) {
            nextBtn.addEventListener('click', nextSlide)
        }

        return () => {
            if (nextBtn) {
                nextBtn.removeEventListener('click', nextSlide)
            }
        }
    }, [swiper, nextRef])

    return (
        <CarouselComponent>
            <Swiper
                onSwiper={(swiper) => setSwiper(swiper)}
                spaceBetween={30}
                loop={true}
                allowTouchMove={false}
                speed={400}
                autoplay={{
                    delay: 4000,
                }}
                breakpoints={breakpoints}
            >
                {children.map((child, index) => (
                    <SwiperSlide key={index}>{child}</SwiperSlide>
                ))}
            </Swiper>
        </CarouselComponent>
    )
}

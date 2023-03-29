'use client'

import { Swiper, SwiperSlide } from 'swiper/react'
import { Autoplay } from 'swiper'
import { SwiperOptions } from 'swiper/types'
import s from './Carousel.module.scss'
import 'swiper/scss'

interface CarouselProps {
  breakpoints: SwiperOptions['breakpoints']
  children: Array<React.ReactNode>
}

const Carousel = ({ breakpoints, children }: CarouselProps) => {
  return (
    <div className={s.container}>
      <Swiper
        spaceBetween={30}
        loop={true}
        allowTouchMove={false}
        speed={400}
        modules={[Autoplay]}
        autoplay={{
          delay: 4000,
          stopOnLastSlide: true,
        }}
        breakpoints={breakpoints}
      >
        {children && children.map((child, index) => <SwiperSlide key={index}>{child}</SwiperSlide>)}
      </Swiper>
    </div>
  )
}

export default Carousel

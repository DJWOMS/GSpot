'use client'

import { useState, useEffect } from 'react'
import { Autoplay } from 'swiper'
import { Swiper, SwiperSlide } from 'swiper/react'
import 'swiper/scss'
import { Swiper as SwiperType, SwiperOptions } from 'swiper/types'
import s from './Carousel.module.scss'

interface CarouselProps {
  prevRef?: React.RefObject<HTMLElement>
  nextRef?: React.RefObject<HTMLElement>
  breakpoints: SwiperOptions['breakpoints']
  children: Array<React.ReactNode>
}

const Carousel = ({ prevRef, nextRef, breakpoints, children }: CarouselProps) => {
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
    <div className={s.container}>
      <Swiper
        modules={[Autoplay]}
        onSwiper={(swiper) => setSwiper(swiper)}
        spaceBetween={30}
        loop={true}
        speed={400}
        autoplay={{
          delay: 5000,
          stopOnLastSlide: true,
        }}
        breakpoints={breakpoints}
      >
        {children.map((child, index) => (
          <SwiperSlide key={index}>{child}</SwiperSlide>
        ))}
      </Swiper>
    </div>
  )
}

export default Carousel

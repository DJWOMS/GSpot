'use client'

import { useEffect, useState } from 'react'
import { Autoplay, Navigation } from 'swiper'
import 'swiper/css'
import { Swiper, SwiperSlide } from 'swiper/react'
import type { Swiper as SwiperType, SwiperOptions } from 'swiper/types'
import s from './Carousel.module.css'
import CarouselArrow from './CarouselArrow'

interface CarouselProps {
  prevRef?: React.RefObject<HTMLElement>
  nextRef?: React.RefObject<HTMLElement>
  navigation?: boolean
  breakpoints: SwiperOptions['breakpoints']
  children: Array<React.ReactNode>
}

const Carousel = ({ prevRef, nextRef, breakpoints, children, navigation }: CarouselProps) => {
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
        modules={[Autoplay, Navigation]}
        onSwiper={(swiper) => setSwiper(swiper)}
        spaceBetween={30}
        loop={true}
        speed={400}
        autoplay={{
          delay: 4000,
          stopOnLastSlide: true,
        }}
        breakpoints={breakpoints}
      >
        {children.map((child, index) => (
          <SwiperSlide key={index}>{child}</SwiperSlide>
        ))}
        {navigation && <CarouselArrow nextClass={s.next} prevClass={s.prev} />}
      </Swiper>
    </div>
  )
}

export default Carousel

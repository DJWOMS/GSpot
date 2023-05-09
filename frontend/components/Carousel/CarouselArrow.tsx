'use client'

import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import { useSwiper } from 'swiper/react'

interface CarouselArrow {
  nextClass: string
  prevClass: string
}

function CarouselArrow({ nextClass, prevClass }: CarouselArrow) {
  const swipe = useSwiper()
  return (
    <>
      <button className={prevClass} onClick={() => swipe.slideNext()}>
        <IconChevronRight />
      </button>
      <button className={nextClass} onClick={() => swipe.slidePrev()}>
        <IconChevronLeft />
      </button>
    </>
  )
}

export default CarouselArrow

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
      <button className={nextClass} onClick={() => swipe.slideNext()}>
        <IconChevronLeft />
      </button>
      <button className={prevClass} onClick={() => swipe.slidePrev()}>
        <IconChevronRight />
      </button>
    </>
  )
}

export default CarouselArrow

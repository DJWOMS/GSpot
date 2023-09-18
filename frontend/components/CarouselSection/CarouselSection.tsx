'use client'

import { FC, ReactNode, useRef } from 'react'
import Carousel from 'components/Carousel'
import Section from 'components/Section'

type Props = {
  showBig?: boolean
  title?: string | ReactNode
  children: ReactNode[]
}

const CarouselSection: FC<Props> = ({ showBig, title, children }) => {
  const prevRef = useRef(null)
  const nextRef = useRef(null)

  return (
    <Section bg={showBig} first={showBig} title={title} navPrev={prevRef} navNext={nextRef}>
      <Carousel
        prevRef={prevRef}
        nextRef={nextRef}
        breakpoints={{
          0: {
            slidesPerView: showBig ? 1.5 : 2,
          },
          576: {
            slidesPerView: 2,
          },
          768: {
            slidesPerView: showBig ? 1 : 3,
          },
          1200: {
            slidesPerView: showBig ? 2 : 5,
          },
        }}
      >
        {children}
      </Carousel>
    </Section>
  )
}

export default CarouselSection

'use client'

import Carousel from 'components/Carousel'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import { useRef } from 'react'
import Section from 'components/Section'
import CardBig from 'components/CardBig'

export function BestGames() {
  const prevRef = useRef(null)
  const nextRef = useRef(null)

  return (
    <Section
      bg
      first
      items={[
        {
          title: {
            children: (
              <>
                <b>Лучшие игры</b> этого месяца
              </>
            ),
            uppercase: true,
          },
          navigation: [
            {
              ref: prevRef,
              children: <IconChevronLeft />,
            },
            {
              ref: nextRef,
              children: <IconChevronRight />,
            },
          ],
          children: (
            <Carousel
              prevRef={prevRef}
              nextRef={nextRef}
              breakpoints={{
                0: {
                  slidesPerView: 1,
                },
                576: {
                  slidesPerView: 2,
                },
                768: {
                  slidesPerView: 1,
                },
                1200: {
                  slidesPerView: 2,
                },
              }}
            >
              {[1, 2, 3, 4, 5].map((i) => (
                <CardBig key={i} coverImg={'https://picsum.photos/1000'} link={'#'} title={'Test'} price={100} />
              ))}
            </Carousel>
          ),
        },
      ]}
    />
  )
}

'use client'

import { useRef } from 'react'
import Section from 'components/Section'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import Carousel from 'components/Carousel'
import { GameCard } from 'features/games'
import { GameCardInterface } from 'features/games'

async function getData(): Promise<GameCardInterface[]> {
  const res = await fetch('http://localhost:3100/api/latest-games')
  if (!res.ok) {
    throw new Error('Failed to fetch data')
  }
  return res.json()
}

const LatestGames = async () => {
  const data = await getData()

  const prevRef = useRef(null)
  const nextRef = useRef(null)

  return (
    <Section
      items={[
        {
          children: (
            <Carousel
              prevRef={prevRef}
              nextRef={nextRef}
              breakpoints={{
                0: {
                  slidesPerView: 2,
                },
                576: {
                  slidesPerView: 2,
                },
                768: {
                  slidesPerView: 3,
                },
                1200: {
                  slidesPerView: 5,
                },
              }}
            >
              {data.map((i, id) => (
                <GameCard
                  key={id}
                  title={i.title}
                  link="/"
                  badge={i.badge}
                  coverImg={i.coverImg}
                  price={i.price}
                  sale={i.sale}
                  available={i.available}
                  currency={i.currency}
                />
              ))}
            </Carousel>
          ),
          title: 'Latest releases',
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
        },
      ]}
    />
  )
}

export default LatestGames

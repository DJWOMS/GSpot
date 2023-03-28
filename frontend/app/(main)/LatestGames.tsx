'use client'

import { FC, useRef } from 'react'
import Section from 'components/Section'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import Carousel from 'components/Carousel'
import { GameCard } from 'features/games'
import { GameCardInterface } from 'features/games'

interface Props {
  games: GameCardInterface[]
}

const LatestGames: FC<Props> = ({ games }) => {
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
              {games.map((game, index) => (
                <GameCard key={index} {...game} />
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

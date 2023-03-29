'use client'

import { FC, useRef } from 'react'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import CardBig from 'components/CardBig'
import Carousel from 'components/Carousel'
import Section from 'components/Section'
import { GameCardInterface } from 'features/games'

interface Props {
  games: GameCardInterface[]
}

const BestGames: FC<Props> = ({ games }) => {
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
              {games.map((game, index) => (
                <CardBig key={index} {...game} />
              ))}
            </Carousel>
          ),
        },
      ]}
    />
  )
}

export default BestGames

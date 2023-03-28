'use client'
import Carousel from 'components/Carousel'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import { useRef } from 'react'
import Section from 'components/Section'
import CardBig from 'components/CardBig'
import { GameCardInterface } from 'features/games'

const BestGames = (bestGamesData: Array<GameCardInterface>) => {
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
              {bestGamesData?.map((i, id) => (
                <CardBig
                  key={id}
                  coverImg={'https://picsum.photos/1000'}
                  link={'#'}
                  title={i.title}
                  price={i.price}
                  sale={i.sale}
                  platform={i.platform}
                />
              ))}
            </Carousel>
          ),
        },
      ]}
    />
  )
}

export default BestGames

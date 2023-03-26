'use client'
import Carousel from 'components/Carousel'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import { useEffect, useRef, useState } from 'react'
import Section from 'components/Section'
import CardBig from 'components/CardBig'
import { GameCardInterface } from 'features/games'

const BestGames = () => {
  const prevRef = useRef(null)
  const nextRef = useRef(null)

  const [data, setData] = useState<GameCardInterface[]>([])

  async function getData() {
    try {
      const res = await fetch('http://127.0.0.1:3100/api/best-games')

      if (!res.ok) {
        throw new Error('Failed to fetch data!')
      }

      const json = await res.json()
      setData(json)
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    getData()
  }, [])

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
              {data?.map((i, id) => (
                <CardBig
                  key={id}
                  coverImg={'https://picsum.photos/1000'}
                  link={'#'}
                  title={i.title}
                  price={i.price}
                  sale={i.sale}
                  available={i.available}
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

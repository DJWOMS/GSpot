'use client'

import { useRef } from 'react'
import Section from 'components/Section'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import Carousel from 'components/Carousel'
import GameCard from 'features/games'

export function LatestGames() {
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
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
                            <GameCard title="Test" price={100} link="/" />
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

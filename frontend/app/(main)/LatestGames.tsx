'use client'

import { FC, useEffect, useRef, useState } from 'react'
import Section from 'components/Section'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import Carousel from 'components/Carousel'
import { GameCard } from 'features/games'
import { GameCardInterface } from 'features/games/components/types'
import { GetServerSideProps, GetServerSidePropsContext } from 'next'

const LatestGames: FC<Array<GameCardInterface>> = (): JSX.Element => {
    const [data, setData] = useState([])

    async function fetchData() {
        const res = await fetch('http://localhost:3100/api/latest-games')
        const json = await res.json()
        setData(json)
    }

    useEffect(() => {
        fetchData()
    }, [])
    console.log(data)

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
                            {data.length &&
                                data.map(({ title, badge, coverImg, price, sale, avalible, currency }: GameCardInterface, id: number) => (
                                    <GameCard
                                        key={id}
                                        title={title}
                                        link="/"
                                        badge={badge}
                                        coverImg={coverImg}
                                        price={price}
                                        sale={sale}
                                        avalible={avalible}
                                        currency={currency}
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

export { LatestGames }

export const getServerSideProps: GetServerSideProps<GameCardInterface[]> = async (
    context: GetServerSidePropsContext
): Promise<{ props: GameCardInterface[] }> => {
    const res = await fetch('http://localhost:3100/api/latest-games')
    const data = await res.json()
    return {
        props: data,
    }
}

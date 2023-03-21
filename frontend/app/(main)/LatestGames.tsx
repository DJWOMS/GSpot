'use client'

import { FC, useRef } from 'react'
import { GetServerSideProps, GetServerSidePropsContext } from 'next'
import { Section, SectionNavWrap, SectionNav, SectionTitle, SectionTitleWrap, SectionView } from '../../components/Section'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import { Carousel } from '../../components/Carousel'
import { GameCard } from '../../features/games'

const LatestGameMockState: GameCardInterface[] = [
    { title: 'Desperados III Digital De', link: '/', image: '', price: 49.0, badge: 'New', avalible: ['ps', 'xb', 'ap'] },
    { title: 'Red Dead Redemptio', link: '/', image: '', price: 19.99, sale: 12.0, badge: 'Pre-order', avalible: ['ap', 'wn'] },
    { title: 'Dandara: Trials of Fear Editi', link: '/', image: '', price: 18.0, sale: 12.0, badge: 'New', avalible: ['xb', 'ap'] },
    { title: 'Druidstone: The Secret of t', link: '/', image: '', price: 58.49, sale: 20.0, avalible: ['xb'] },
    { title: "Baldur's Gate II: Enhanced ", link: '/', image: '', price: 38.99, avalible: ['xb', 'ap'] },
    { title: "Baldur's Gate: Enhanced", link: '/', image: '', price: 9.99, avalible: ['xb', 'ps'] },
    { title: 'SteamWorld Quest: Hand ', link: '/', image: '', price: 12.49, badge: 'Pre-order', avalible: ['xb', 'wn'] },
]

export interface GameCardInterface {
    title: string
    link: string
    image: string
    price: number
    sale?: number
    badge?: 'New' | 'Pre-order'
    avalible?: Array<'ps' | 'xb' | 'wn' | 'ap'>
}

const LatestGames: FC<Array<GameCardInterface>> = (): JSX.Element => {
    const prevRef = useRef(null)
    const nextRef = useRef(null)
    return (
        <Section>
            <div className="container">
                <SectionTitleWrap>
                    <SectionTitle>Последние выпуски</SectionTitle>
                    <SectionNavWrap>
                        <SectionView>Посмотреть все</SectionView>
                        <SectionNavWrap>
                            <SectionNav ref={prevRef}>
                                <IconChevronLeft />
                            </SectionNav>

                            <SectionNav ref={nextRef}>
                                <IconChevronRight />
                            </SectionNav>
                        </SectionNavWrap>
                    </SectionNavWrap>
                </SectionTitleWrap>
            </div>

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
                {LatestGameMockState.map(({ title, badge, image, price, sale, avalible }: GameCardInterface, id: number) => (
                    <GameCard key={id} title={title} link="/" badge={badge} image={image} price={price} sale={sale} avalible={avalible} />
                ))}
                {/* <GameCard title="Test" price={100} link="/" />
                <GameCard title="Test" price={100} link="/" /> */}
            </Carousel>
        </Section>
    )
}

export { LatestGames }

export const getServerSideProps: GetServerSideProps<GameCardInterface[]> = async (
    context: GetServerSidePropsContext
): Promise<{ props: GameCardInterface[] }> => {
    const res = await fetch('https://api.com/LatestGames')
    const data = await res.json()

    return {
        props: LatestGameMockState,
    }
}

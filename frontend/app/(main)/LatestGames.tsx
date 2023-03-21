'use client'

import { useRef } from 'react'
import { Section, SectionNavWrap, SectionNav, SectionTitle, SectionTitleWrap, SectionView } from 'components/Section'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import Carousel from 'components/Carousel'
import GameCard from 'features/games'

export function LatestGames() {
    const prevRef = useRef(null)
    const nextRef = useRef(null)

    return (
        <Section>
            <div className="container">
                <SectionTitleWrap>
                    <SectionTitle>Latest releases</SectionTitle>

                    <SectionNavWrap>
                        <SectionView>View All</SectionView>

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
        </Section>
    )
}

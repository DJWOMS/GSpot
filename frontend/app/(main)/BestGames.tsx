'use client'

import { Carousel } from 'components/Carousel'
import { SectionTitleWrap, SectionTitle, SectionNavWrap, SectionBg, SectionNav } from 'components/Section'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import { useRef } from 'react'
import { BestGame } from './BestGame'

export function BestGames() {
    const prevRef = useRef(null)
    const nextRef = useRef(null)

    return (
        <SectionBg first>
            <div className="container">
                <SectionTitleWrap>
                    <SectionTitle uppercase>
                        <b>Лучшие игры</b> этого месяца
                    </SectionTitle>

                    <SectionNavWrap>
                        <SectionNav ref={prevRef}>
                            <IconChevronLeft />
                        </SectionNav>

                        <SectionNav ref={nextRef}>
                            <IconChevronRight />
                        </SectionNav>
                    </SectionNavWrap>
                </SectionTitleWrap>
            </div>

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
                <BestGame title="Test" price={100} link="/" />
                <BestGame title="Test" price={100} link="/" />
                <BestGame title="Test" price={100} link="/" />
                <BestGame title="Test" price={100} link="/" />
                <BestGame title="Test" price={100} link="/" />
            </Carousel>
        </SectionBg>
    )
}

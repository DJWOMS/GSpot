import { SectionTitleWrap, SectionTitle, SectionNavWrap, SectionBg, SectionNav } from '@/components'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import { FC } from 'react'
import { LatestNews } from './LatestNews'
import CardsIndex from '@/components/CardsIndex/cardsIndex'

const Home: FC = (): JSX.Element => {
    return (
        <>
            <SectionBg first>
                <div className="container">
                    <SectionTitleWrap>
                        <SectionTitle uppercase>
                            <b>Лучшие игры</b> этого месяца
                        </SectionTitle>

                        <SectionNavWrap>
                            <SectionNav>
                                <IconChevronLeft />
                            </SectionNav>

                            <SectionNav>
                                <IconChevronRight />
                            </SectionNav>
                        </SectionNavWrap>
                    </SectionTitleWrap>
                    <CardsIndex />
                </div>
            </SectionBg>

            <LatestNews />
        </>
    )
}

export default Home

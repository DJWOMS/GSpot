import { Header } from '@/components'
import { SectionTitleWrap, SectionTitle, SectionNavWrap, SectionBg, SectionNav } from '@/components'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import { FC } from 'react'
import { Footer } from '@/components'
import { LatestNews } from './LatestNews'

const Home: FC = (): JSX.Element => {
    return (
        <>
            <Header />
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
                </div>
            </SectionBg>

            <LatestNews />

            <Footer />
        </>
    )
}

export default Home

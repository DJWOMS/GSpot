import { SectionTitleWrap, SectionTitle, SectionNavWrap, SectionBg, SectionNav } from '@/components'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'

export function BestGames() {
    return (
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
    )
}

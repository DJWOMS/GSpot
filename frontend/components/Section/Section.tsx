import { FC, MutableRefObject } from 'react'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import cn from 'classnames'
import Container from '../Container'
import s from './Section.module.css'

interface SectionProps {
  first?: boolean
  last?: boolean
  bg?: boolean
  full?: boolean
  title?: string | React.ReactNode
  children?: React.ReactNode | React.ReactNode[]
  navPrev?: MutableRefObject<null>
  navNext?: MutableRefObject<null>
  viewAll?: string
}

const Section: FC<SectionProps> = ({ full, bg, last, first, title, children, navPrev, navNext, viewAll }) => {
  return (
    <div
      className={cn(
        s.section,
        { [s.sectionBg]: bg && !full },
        { [s.sectionBgFull]: bg && full },
        { [s.sectionLast]: last },
        { [s.sectionFirst]: first }
      )}
    >
      <Container>
        <div className={s.sectionTitleWrapper}>
          <h2 className={cn(s.sectionTitle, s.sectionTitleSmall, {})}>{title}</h2>

          <div className={s.sectionNavWrapper}>
            {viewAll && (
              <a href="#" className={s.sectionView}>
                View All
              </a>
            )}

            {navPrev && (
              <button className={s.sectionNav} ref={navPrev}>
                <IconChevronLeft />
              </button>
            )}

            {navNext && (
              <button className={s.sectionNav} ref={navNext}>
                <IconChevronRight />
              </button>
            )}
          </div>
        </div>

        {children}
      </Container>
    </div>
  )
}

export default Section

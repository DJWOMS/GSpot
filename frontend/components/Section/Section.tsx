import { FC, MutableRefObject } from 'react'
import { IconChevronLeft, IconChevronRight } from '@tabler/icons-react'
import cn from 'classnames'
import s from './Section.module.scss'

interface Props {
  first?: boolean
  last?: boolean
  bg?: boolean
  full?: boolean
  title?: string | React.ReactNode
  children: React.ReactNode | React.ReactNode[]
  navPrev?: MutableRefObject<null>
  navNext?: MutableRefObject<null>
  viewAll?: string
}

const Section: FC<Props> = ({ full, bg, last, first, title, children, navPrev, navNext, viewAll }) => {
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
    </div>
  )
}

export default Section

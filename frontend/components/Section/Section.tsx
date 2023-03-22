import s from './styles.module.scss'
import { FC, MutableRefObject } from 'react'
import cn from 'classnames'

type ITitle = {
    uppercase?: boolean
    children: React.ReactNode
}

interface Item {
    children: React.ReactNode
    navigation?: {
        ref?: MutableRefObject<null>
        children: React.ReactNode
    }[]
    title: string | ITitle
}

interface Props {
    items: Item[]
    first?: boolean
    last?: boolean
    bg?: boolean
    full?: boolean
}

const Section: FC<Props> = ({ items, full, bg, last, first }) => {
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
            {items.map((i, index) => {
                return (
                    <div key={index} className="container">
                        <div className="row">
                            <div className="col-12 col-md-6 col-xl-4">
                                <div className={i.navigation?.length ? s.sectionTitleWrapper : s.sectionTitleWrapperSingle}>
                                    <h2
                                        className={cn(s.sectionTitle, s.sectionTitleSmall, {
                                            [s.sectionTitleUppercase]: typeof i.title !== 'string' && i.title.uppercase,
                                        })}
                                    >
                                        {typeof i.title === 'string' ? i.title : i.title.children}
                                    </h2>

                                    {i.navigation?.length === 1 && !i.navigation[0].ref ? (
                                        i.navigation[0].children
                                    ) : (
                                        <div className={s.sectionNavWrapper}>
                                            <a href="#" className={s.sectionView}>
                                                View All
                                            </a>

                                            {i.navigation?.length && (
                                                <>
                                                    {i.navigation.map((i, index) => (
                                                        <button key={index} className={s.sectionNav} ref={i.ref}>
                                                            {i.children}
                                                        </button>
                                                    ))}
                                                </>
                                            )}
                                        </div>
                                    )}
                                </div>

                                {i.children}
                            </div>
                        </div>
                    </div>
                )
            })}
        </div>
    )
}

export default Section

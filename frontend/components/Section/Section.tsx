import s from './styles.module.scss'
import { FC } from 'react'
import cn from 'classnames'

interface Item {
    children: React.ReactNode
    title: string
}

interface Props {
    items: Item[]
}

const Section: FC<Props> = ({ items }) => {
    return (
        <div className={s.section}>
            {items.map((i, index) => {
                return (
                    <div key={index} className="container">
                        <div className="row">
                            <div className="col-12 col-md-6 col-xl-4">
                                <div className={s.sectionTitleWrapperSingle}>
                                    <h3 className={cn(s.sectionTitle, s.sectionTitleSmall)}>{i.title}</h3>
                                    <div className={s.sectionNavWrapper}>
                                        <button className={s.sectionView}>View All</button>
                                    </div>
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

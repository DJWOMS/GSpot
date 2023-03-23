import { IconArrowLeft, IconArrowRight } from '@tabler/icons-react'
import Link from 'next/link'
import s from './Pagination.module.scss'

const Pagination = () => {
    return (
        <div className="col-12">
            <div className={s.container}>
                <div className={s.counter}>12 from 144</div>

                <ul className={s.wrapper}>
                    <li className={s.item}>
                        <Link className={s.linkBtn} href="/prev">
                            <IconArrowLeft />
                        </Link>
                    </li>
                    <li className={s.itemActive}>
                        <Link className={s.linkBtn} href="/1">
                            1
                        </Link>
                    </li>
                    <li className={s.item}>
                        <Link className={s.linkBtn} href="/2">
                            2
                        </Link>
                    </li>
                    <li className={s.item}>
                        <Link className={s.linkBtn} href="/3">
                            3
                        </Link>
                    </li>
                    <li className={s.item}>
                        <Link className={s.linkBtn} href="/next">
                            <IconArrowRight />
                        </Link>
                    </li>
                </ul>
            </div>
        </div>
    )
}

export default Pagination

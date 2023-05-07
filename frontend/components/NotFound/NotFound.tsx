import { FC } from 'react'
import Link from 'next/link'
import s from './NotFound.module.css'

const NotFound: FC = () => {
  return (
    <div className={s.page}>
      <div className={s.wrap}>
        <div className={s.content}>
          <h1 className={s.title}>404</h1>
          <p className={s.text}>The page you are looking for not available!</p>
          <Link href="/" className={s.link}>
            go back
          </Link>
        </div>
      </div>
    </div>
  )
}

export default NotFound

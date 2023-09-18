import { FC } from 'react'
import cn from 'classnames'
import Link from 'next/link'
import s from './Breadcrumbs.module.css'

interface Item {
  name: string
  link?: string
}

type Props = {
  items: Item[]
}

const Breadcrumbs: FC<Props> = ({ items }) => {
  return (
    <div className={s.components}>
      <div className={s.breadcrumb}>
        <Link className={s.linkBtn} href="/">
          Главная
        </Link>
      </div>

      {items.map((i, index) => (
        <div className={cn(s.breadcrumb, { [s.breadcrumbActive]: index === items.length - 1 })} key={index}>
          {i.link !== undefined ? (
            <Link className={s.linkBtn} href={i.link}>
              {i.name}
            </Link>
          ) : (
            i.name
          )}
        </div>
      ))}
    </div>
  )
}

export default Breadcrumbs

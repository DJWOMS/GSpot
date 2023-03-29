import { FC } from 'react'
import { IconPlus } from '@tabler/icons-react'
import Image from 'next/image'
import s from './List.module.scss'

interface Props {
  coverImg: string
  title: string
  price: number
  sale?: number
}

const List: FC<Props> = ({ coverImg, title, price, sale }) => {
  return (
    <div className={s.listItem}>
      <div className={s.listCover}>
        <Image width={240} height={340} src={coverImg} alt="Logo" loading="eager" />
      </div>

      <div className={s.listWrap}>
        <h3 className={s.listTitle}>
          <a href="#">{title}</a>
        </h3>

        <div className={s.listPrice}>
          <span>${price}</span>
          <s>${sale}</s>
          <b>{sale}% OFF</b>
        </div>

        <div className={s.listBuy}>
          <IconPlus />
        </div>
      </div>
    </div>
  )
}

interface ListProps {
  children: React.ReactNode[]
}

export const ListWrapper: FC<ListProps> = ({ children }) => {
  return <div className={s.list}>{children}</div>
}

export default List

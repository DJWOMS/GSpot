import { FC } from 'react'
import { IconPlus } from '@tabler/icons-react'
import { GamingCards } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'
import Image from 'next/image'
import { notFound } from 'next/navigation'
import s from './List.module.scss'

const List = async () => {
  const cards = await fetchServerSide<GamingCards>({
    path: '/games/cards',
    cache: 'no-cache',
  })
  if (!cards) {
    notFound()
  }

  return (
    <div className={s.listItem}>
      <div className={s.listCover}>
        <Image width={240} height={340} src={cards.coverImg} alt="Logo" loading="eager" />
      </div>

      <div className={s.listWrap}>
        <h3 className={s.listTitle}>
          <a href="#">{cards.title}</a>
        </h3>

        <div className={s.listPrice}>
          <span>${cards.price}</span>
          <s>${cards.sale}</s>
          <b>{cards.sale}% OFF</b>
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

import { FC } from 'react'
import { IconPlus } from '@tabler/icons-react'
import Image from 'next/image'
import type { GameListInterface } from '../../types'
import s from './ListGame.module.css'

const ListGame: FC<GameListInterface> = ({ title, price, sale, coverImg }) => {
  return (
    <div className={s.item}>
      <div className={s.cover}>
        <Image width={240} height={340} src={coverImg} alt="Logo" loading="eager" />
      </div>

      <div className={s.wrap}>
        <h3 className={s.title}>
          <a href="#">{title}</a>
        </h3>

        <div className={s.price}>
          <span>${price}</span>
          <s>${sale}</s>
          <b>{sale}% OFF</b>
        </div>

        <div className={s.buy}>
          <IconPlus />
        </div>
      </div>
    </div>
  )
}
export { ListGame }

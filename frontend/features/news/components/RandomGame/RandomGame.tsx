import { FC } from 'react'
import { IconPlus } from '@tabler/icons-react'
import { RandomGameInterface } from 'features/games'
import Image from 'next/image'
import s from './RandomGame.module.scss'

const RandomGame: FC<RandomGameInterface> = ({ title, price, sale, coverImg }) => {
  return (
    <div className={s.item}>
      <div className={s.image}>
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
export { RandomGame }

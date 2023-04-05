import { FC } from 'react'
import cn from 'classnames'
import s from './SkeletonListCheckBoxes.module.scss'

interface SkeletonListCheckBoxesProps {
  count: number
}

const SkeletonListCheckBoxes: FC<SkeletonListCheckBoxesProps> = ({ count = 5 }) => {
  const sizes = ['w-40', 'w-24', 'w-32', 'w-28', 'w-36']

  return (
    <ul className={s.animate}>
      {[...new Array(count)].map((_, index) => (
        <li className={s.checkbox} key={index}>
          <div className={s.square} />
          <div className={cn(s.line, sizes[index % 5])} />
        </li>
      ))}
    </ul>
  )
}

export { SkeletonListCheckBoxes }

import { FC } from 'react'
import SkeletonCheckBox from '../SkeletonCheckBox'
import s from './SkeletonListCheckBoxes.module.css'

interface SkeletonListCheckBoxesProps {
  count: number
}

const SkeletonListCheckBoxes: FC<SkeletonListCheckBoxesProps> = ({ count = 5 }) => {
  const sizes = ['w-40', 'w-24', 'w-32', 'w-28', 'w-36']

  return (
    <div className={s.animate}>
      {[...new Array(count)].map((_, index) => (
        <SkeletonCheckBox className={sizes[index % 5]} key={index} />
      ))}
    </div>
  )
}

export default SkeletonListCheckBoxes

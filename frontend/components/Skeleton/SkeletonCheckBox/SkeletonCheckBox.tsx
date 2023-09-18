import { FC } from 'react'
import cn from 'classnames'
import s from './SkeletonCheckBox.module.css'

interface SkeletonCheckBoxProps {
  className: string
}

const SkeletonCheckBox: FC<SkeletonCheckBoxProps> = ({ className }) => {
  return (
    <div className={s.checkbox}>
      <div className={s.square} />
      <div className={cn(s.line, className)} />
    </div>
  )
}

export default SkeletonCheckBox

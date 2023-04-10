import { FC } from 'react'
import cn from 'classnames'
import s from './SkeletonInput.module.scss'

interface SkeletonInputProps {
  size?: '24' | '28' | '32' | '36' | '40' | '44' | 'full'
}

const SkeletonInput: FC<SkeletonInputProps> = ({ size = 'full' }) => {
  return (
    <div className={s.animate}>
      <div className={cn(s.line, `w-${size}`)} />
    </div>
  )
}

export { SkeletonInput }

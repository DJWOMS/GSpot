import { FC } from 'react'
import cn from 'classnames'
import s from './SkeletonInput.module.scss'

interface SkeletonInputProps {
  size?: '24' | '28' | '32' | '36' | '40' | '44' | 'full'
  height?: string
}

const SkeletonText: FC<SkeletonInputProps> = ({ size = 'full', height }) => {
  return (
    <div className={s.animate}>
      <div className={cn(s.line, `w-${size} h-${height}`)} />
    </div>
  )
}

export { SkeletonText }

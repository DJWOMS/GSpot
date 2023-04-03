import { FC } from 'react'
import s from './Label.module.scss'

interface LabelProps {
  children: React.ReactNode
}

const Label: FC<LabelProps> = ({ children, ...props }) => {
  return (
    <label className={s.label} {...props}>
      {children}
    </label>
  )
}

export { Label }

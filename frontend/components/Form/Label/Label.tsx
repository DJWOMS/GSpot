import { FC } from 'react'
import s from './Label.module.css'

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

export default Label

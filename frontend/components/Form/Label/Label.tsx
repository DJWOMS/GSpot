import { DetailedHTMLProps, FC } from 'react'
import cn from 'classnames'
import s from './Label.module.css'

const Label: FC<DetailedHTMLProps<React.LabelHTMLAttributes<HTMLLabelElement>, HTMLLabelElement>> = ({
  className,
  ...props
}) => {
  return <label className={cn(s.label, className)} {...props} />
}

export default Label

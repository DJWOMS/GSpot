import { FC } from 'react'
import cn from 'classnames'
import s from './Group.module.css'

const Group: FC<React.DetailedHTMLProps<React.HTMLAttributes<HTMLDivElement>, HTMLDivElement>> = ({
  className,
  ...props
}) => {
  return <div className={cn(s.group, className)} {...props} />
}

export default Group

import { FC, InputHTMLAttributes } from 'react'
import cn from 'classnames'
import s from './Input.module.css'

const Input: FC<InputHTMLAttributes<HTMLInputElement>> = ({ className, ...props }) => {
  return <input className={cn(s.input, className)} {...props} />
}

export default Input

import { forwardRef, ForwardRefRenderFunction } from 'react'
import s from './Input.module.scss'

type InputProps = React.InputHTMLAttributes<HTMLInputElement>

const Input: ForwardRefRenderFunction<HTMLInputElement, InputProps> = ({ ...props }, ref) => {
  return <input className={s.input} ref={ref} {...props} />
}

export default forwardRef(Input)

import { forwardRef, ForwardRefRenderFunction } from 'react'
import s from './Select.module.scss'

interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  children: React.ReactNode
}

const Select: ForwardRefRenderFunction<HTMLSelectElement, SelectProps> = ({ children, ...props }, ref) => {
  return (
    <select className={s.select} ref={ref} {...props}>
      <option value="" disabled selected>
        Выберите вариант
      </option>

      {children}
    </select>
  )
}

export default forwardRef(Select)

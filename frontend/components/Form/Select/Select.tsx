import { forwardRef, ForwardRefRenderFunction } from 'react'
import s from './Select.module.scss'

type SelectOption = {
  value: string
  option: string
}

interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  options: SelectOption[]
}

const Select: ForwardRefRenderFunction<HTMLSelectElement, SelectProps> = ({ options, ...props }, ref) => {
  return (
    <select className={s.select} ref={ref} {...props}>
      <option value="" disabled selected>
        Выберите вариант
      </option>

      {options.map(({ value, option }) => (
        <option value={value} key={value}>
          {option}
        </option>
      ))}
    </select>
  )
}

export default forwardRef(Select)

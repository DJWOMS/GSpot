import { FC } from 'react'
import s from './Select.module.scss'

type SelectOption = {
  value: string
  option: string
}

interface SelectProps extends React.HTMLAttributes<HTMLSelectElement> {
  options: SelectOption[]
}

const Select: FC<SelectProps> = ({ options, ...props }) => {
  return (
    <select className={s.select} {...props}>
      {options.map(({ value, option }) => (
        <option value={value} key={value}>
          {option}
        </option>
      ))}
    </select>
  )
}

export { Select }

import { useId, FC, InputHTMLAttributes, DetailedHTMLProps } from 'react'
import s from './CheckBox.module.css'

interface Props extends DetailedHTMLProps<InputHTMLAttributes<HTMLInputElement>, HTMLInputElement> {
  label?: string
}

const CheckBox: FC<Props> = ({ label, ...props }) => {
  const uid = useId()

  return (
    <div className={s.checkbox}>
      <input id={uid} type="checkbox" {...props} />
      <label htmlFor={uid}>{label}</label>
    </div>
  )
}

export default CheckBox

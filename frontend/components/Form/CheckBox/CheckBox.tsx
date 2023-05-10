import { HTMLAttributes, useId, FC } from 'react'
import s from './CheckBox.module.css'

interface Props extends HTMLAttributes<HTMLInputElement> {
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

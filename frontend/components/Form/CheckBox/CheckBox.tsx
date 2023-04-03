import { FC, useId } from 'react'
import s from './CheckBox.module.scss'

interface CheckBoxProps extends React.HTMLAttributes<HTMLInputElement> {
  label: string
}

const CheckBox: FC<CheckBoxProps> = ({ label, ...props }) => {
  const uid = useId()

  return (
    <div className={s.checkbox}>
      <input id={uid} type="checkbox" {...props} />
      <label htmlFor={uid}>{label}</label>
    </div>
  )
}

export { CheckBox }

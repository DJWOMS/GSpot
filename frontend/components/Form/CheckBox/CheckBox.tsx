import { forwardRef, ForwardRefRenderFunction, useId } from 'react'
import s from './CheckBox.module.scss'

interface CheckBoxProps extends React.HTMLAttributes<HTMLInputElement> {
  label: string
}

const CheckBox: ForwardRefRenderFunction<HTMLInputElement, CheckBoxProps> = ({ label, ...props }, ref) => {
  const uid = useId()

  return (
    <div className={s.checkbox}>
      <input id={uid} type="checkbox" ref={ref} {...props} />
      <label htmlFor={uid}>{label}</label>
    </div>
  )
}

export default forwardRef(CheckBox)

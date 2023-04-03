import s from './Input.module.scss'

const Input = ({ ...props }) => {
  return <input className={s.input} {...props} />
}

export { Input }

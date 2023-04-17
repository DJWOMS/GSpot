import { FC } from 'react'
import s from './Container.module.scss'

interface ContainerProps {
  children: React.ReactNode
}

const Container: FC<ContainerProps> = ({ children }) => {
  return <div className={s.component}>{children}</div>
}

export { Container }
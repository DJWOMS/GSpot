import { FC } from 'react'
import s from './Group.module.scss'

interface GroupProps {
  children: React.ReactNode
}

const Group: FC<GroupProps> = ({ children }) => {
  return <div className={s.group}>{children}</div>
}

export default Group

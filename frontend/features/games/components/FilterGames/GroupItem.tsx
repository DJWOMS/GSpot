import { FC, ReactNode } from 'react'
import { Group, Label } from 'components/Form'

interface Props {
  label: string
  children: ReactNode
}

const GroupItem: FC<Props> = ({ label, children }) => {
  return (
    <Group>
      <Label>{label}</Label>
      {children}
    </Group>
  )
}

export default GroupItem

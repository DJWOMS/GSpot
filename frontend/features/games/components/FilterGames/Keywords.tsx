import { FC } from 'react'
import { Group, Input, Label } from 'components/Form'

interface KeywordsProps {
  onChange: (data: string) => void
}

const Keywords: FC<KeywordsProps> = ({ onChange }) => {
  const onChangeInput = (e: React.ChangeEvent<HTMLInputElement>) => onChange(e.target.value)

  return (
    <Group>
      <Label>Ключевые слова: </Label>
      <Input type="text" placeholder="Keyword" onChange={onChangeInput} />
    </Group>
  )
}

export { Keywords }

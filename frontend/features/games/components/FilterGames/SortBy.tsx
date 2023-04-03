import { FC } from 'react'
import { Group, Label, Select } from 'components/Form'

interface SortByProps {
  onChange: (data: string) => void
}

const mocks = [
  {
    value: '0',
    option: 'По интересам',
  },
  {
    value: '1',
    option: 'От новых к старым',
  },
  {
    value: '2',
    option: 'От старых к новым',
  },
]

const SortBy: FC<SortByProps> = ({ onChange }) => {
  const onChangeSection = (e: React.ChangeEvent<HTMLSelectElement>) => {
    onChange(e.currentTarget.value)
  }

  return (
    <Group>
      <Label>Сортировать: </Label>

      <Select onChange={onChangeSection} options={mocks} />
    </Group>
  )
}

export { SortBy }

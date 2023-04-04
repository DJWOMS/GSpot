import { Group, Label, Select } from 'components/Form'
import { useFilter } from 'features/games/store'

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

const SortBy = () => {
  const setFilter = useFilter((state) => state.setFilter)
  const onChangeSection = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setFilter('sortby', e.currentTarget.value)
  }

  return (
    <Group>
      <Label>Сортировать: </Label>

      <Select onChange={onChangeSection} options={mocks} />
    </Group>
  )
}

export { SortBy }

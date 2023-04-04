import { Group, Input, Label } from 'components/Form'
import { useFilter } from 'features/games/store'

const Keywords = () => {
  const { value, setFilter } = useFilter((state) => ({ value: state.keywords, setFilter: state.setFilter }))
  const onChangeInput = (e: React.ChangeEvent<HTMLInputElement>) => setFilter('keywords', e.target.value)

  return (
    <Group>
      <Label>Ключевые слова: </Label>
      <Input type="text" placeholder="Keyword" defaultValue={value} onChange={onChangeInput} />
    </Group>
  )
}

export { Keywords }

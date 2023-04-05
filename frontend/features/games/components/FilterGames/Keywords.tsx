import { Group, Input, Label } from 'components/Form'
import { useFilter } from 'features/games/store'

const Keywords = () => {
  const keywords = useFilter((state) => state.keywords)
  const setFilter = useFilter((state) => state.setFilter)

  const onChangeInput = (e: React.ChangeEvent<HTMLInputElement>) => setFilter('keywords', e.target.value)

  return (
    <Group>
      <Label>Ключевые слова: </Label>
      <Input type="text" placeholder="Keyword" defaultValue={keywords} onChange={onChangeInput} />
    </Group>
  )
}

export { Keywords }

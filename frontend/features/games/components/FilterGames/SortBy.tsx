import { useState, useEffect } from 'react'
import { Group, Label, Select } from 'components/Form'
import { SkeletonSelect } from 'components/Skeleton'
import { FormSortByType } from 'features/games'
import { useFilter } from 'features/games/store'
import { fetchServerSide } from 'lib/fetchServerSide'

const SortBy = () => {
  const [sorts, setSorts] = useState<FormSortByType[] | null>(null)

  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FormSortByType[]>({
        path: '/games/filters/sorts',
      })

      if (response) {
        setSorts(response)
      }
    }

    loadData()
  }, [])

  const setFilter = useFilter((state) => state.setFilter)
  const onChangeSection = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setFilter('sortby', e.currentTarget.value)
  }

  return (
    <Group>
      <Label>Сортировать: </Label>

      {sorts === null ? <SkeletonSelect /> : <Select onChange={onChangeSection} options={sorts} />}
    </Group>
  )
}

export { SortBy }

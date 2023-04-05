import { useState, useEffect } from 'react'
import { Group, Label, Select } from 'components/Form'
import { SkeletonSelect } from 'components/Skeleton'
import { FormSortByType } from 'features/games'
import { useFilter } from 'features/games/store'
import { fetchServerSide } from 'lib/fetchServerSide'

interface FormSortByTypeState extends FormSortByType {
  selected: boolean
}

const SortBy = () => {
  const [sorts, setSorts] = useState<FormSortByTypeState[] | null>(null)
  const { getFilter, setFilter } = useFilter((state) => ({ getFilter: state.getFilter, setFilter: state.setFilter }))

  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FormSortByType[]>({
        path: '/games/filters/sorts',
      })

      if (response) {
        const selectedSortBy = getFilter('sortby')
        setSorts(response.map((sort) => ({ ...sort, selected: sort.value === selectedSortBy })))
      }
    }

    loadData()
  }, [getFilter])

  const onChangeSection = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setFilter('sortby', e.currentTarget.value)
  }

  return (
    <Group>
      <Label>Сортировать: </Label>

      {sorts === null ? (
        <SkeletonSelect />
      ) : (
        <Select defaultValue={sorts?.find(({ selected }) => selected)?.value} onChange={onChangeSection} options={sorts} />
      )}
    </Group>
  )
}

export { SortBy }

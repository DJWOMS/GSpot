import { useState, useEffect } from 'react'
import { useFormContext } from 'react-hook-form'
import { Group, Label, Select } from 'components/Form'
import { SkeletonSelect } from 'components/Skeleton'
import { FilterSortByInterface } from 'features/games/types'
import { fetchServerSide } from 'lib/fetchServerSide'

const SortBy = () => {
  const { register } = useFormContext()
  const [sorts, setSorts] = useState<FilterSortByInterface[] | null>(null)

  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FilterSortByInterface[]>({
        path: '/games/filters/sorts',
      })

      if (response) {
        setSorts(response)
      }
    }

    loadData()
  }, [])

  return (
    <Group>
      <Label>Сортировать: </Label>

      {sorts === null ? (
        <SkeletonSelect />
      ) : (
        <Select {...register('sortby')}>
          {sorts.map(({ id, name }) => (
            <option value={id} key={id}>
              {name}
            </option>
          ))}
        </Select>
      )}
    </Group>
  )
}

export { SortBy }

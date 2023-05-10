import { useState, useEffect } from 'react'
import { useFormContext, Controller } from 'react-hook-form'
import { Group, Label } from 'components/Form'
import Select from 'components/Select'
import { SkeletonSelect } from 'components/Skeleton'
import type { FilterSortByInterface } from 'features/games/types'
import { fetchServerSide } from 'lib/fetchServerSide'

const SortBy = () => {
  const { control } = useFormContext()
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
        <Controller
          name="sortby"
          control={control}
          render={({ field }) => (
            <Select {...field} options={sorts.map((i) => ({ name: i.name, value: i.id }))} />
          )}
        />
      )}
    </Group>
  )
}

export { SortBy }

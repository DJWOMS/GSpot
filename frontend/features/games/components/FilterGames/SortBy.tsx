import { useState, useEffect } from 'react'
import { useFormContext } from 'react-hook-form'
import { Group, Label, Select } from 'components/Form'
import { SkeletonSelect } from 'components/Skeleton'
import { fetchServerSide } from 'lib/fetchServerSide'

type SortByState = {
  value: string
  option: string
}

const SortBy = () => {
  const { register } = useFormContext()
  const [sorts, setSorts] = useState<SortByState[] | null>(null)

  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<SortByState[]>({
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

      {sorts === null ? <SkeletonSelect /> : <Select options={sorts} {...register('sortby')} />}
    </Group>
  )
}

export { SortBy }

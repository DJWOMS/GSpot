import { useState, useEffect } from 'react'
import { useFormContext } from 'react-hook-form'
import { CheckBox, Group, Label } from 'components/Form'
import { SkeletonListCheckBoxes } from 'components/Skeleton'
import { FilterPlatformInterface } from 'features/games/types'
import { fetchServerSide } from 'lib/fetchServerSide'

const Platforms = () => {
  const [platforms, setPlatforms] = useState<FilterPlatformInterface[] | null>(null)

  const { register } = useFormContext()

  // get list of platforms from api and set {selected: true} for selected (from url query params)
  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FilterPlatformInterface[]>({
        path: '/games/filters/platforms',
      })

      if (response) {
        setPlatforms(
          response.map((platform) => ({
            ...platform,
          }))
        )
      }
    }

    loadData()
  }, [])

  return (
    <Group>
      <Label>Платформа: </Label>

      {platforms === null ? (
        <SkeletonListCheckBoxes count={4} />
      ) : (
        platforms.map(({ id, name }) => <CheckBox label={name} key={id} defaultValue={id} {...register('platforms')} />)
      )}
    </Group>
  )
}

export { Platforms }

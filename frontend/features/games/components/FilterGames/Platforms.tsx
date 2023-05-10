import { useState, useEffect } from 'react'
import { useFormContext, Controller } from 'react-hook-form'
import { CheckBox, Group, Label } from 'components/Form'
import { SkeletonListCheckBoxes } from 'components/Skeleton'
import type { FilterPlatformInterface } from 'features/games/types'
import { fetchServerSide } from 'lib/fetchServerSide'

const Platforms = () => {
  const [platforms, setPlatforms] = useState<FilterPlatformInterface[] | null>(null)

  const { control } = useFormContext()

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
        platforms.map(({ id, name }) => (
          <Controller
            key={id}
            control={control}
            name="platforms"
            render={({ field }) => <CheckBox label={name} defaultValue={id} {...field} />}
          />
        ))
      )}
    </Group>
  )
}

export { Platforms }

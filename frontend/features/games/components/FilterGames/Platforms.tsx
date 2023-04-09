import { useState, useEffect } from 'react'
import { useFormContext } from 'react-hook-form'
import { CheckBox, Group, Label } from 'components/Form'
import { SkeletonListCheckBoxes } from 'components/Skeleton'
import { fetchServerSide } from 'lib/fetchServerSide'

type PlatformState = {
  slug: string
  name: string
}

const Platforms = () => {
  const [platforms, setPlatforms] = useState<PlatformState[] | null>(null)

  const { register } = useFormContext()

  // get list of platforms from api and set {selected: true} for selected (from url query params)
  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<PlatformState[]>({
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
        platforms.map(({ name, slug }, index) => <CheckBox label={name} key={index} defaultValue={slug} {...register('platforms')} />)
      )}
    </Group>
  )
}

export { Platforms }

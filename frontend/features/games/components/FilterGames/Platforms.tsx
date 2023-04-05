import { useState, useEffect } from 'react'
import { CheckBox, Group, Label } from 'components/Form'
import { SkeletonListCheckBoxes } from 'components/Skeleton'
import { FormPlatformType } from 'features/games'
import { useFilter } from 'features/games/store'
import { fetchServerSide } from 'lib/fetchServerSide'

const Platforms = () => {
  const [platforms, setPlatforms] = useState<FormPlatformType[] | null>(null)

  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<FormPlatformType[]>({
        path: '/games/filters/platforms',
      })

      if (response) {
        setPlatforms(response)
      }
    }

    loadData()
  }, [])

  const toggleFilter = useFilter((state) => state.toggleFilter)

  return (
    <Group>
      <Label>Платформа: </Label>

      {platforms === null ? (
        <SkeletonListCheckBoxes count={4} />
      ) : (
        platforms.map(({ slug, name }, index) => (
          <CheckBox
            label={name}
            onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
              toggleFilter('platforms', slug, e.target.checked)
            }}
            key={index}
          />
        ))
      )}
    </Group>
  )
}

export { Platforms }
